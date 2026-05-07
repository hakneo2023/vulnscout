import phonenumbers
from phonenumbers import carrier, geocoder, number_type, PhoneNumberType


def _is_probably_temp(number_str):
    digits = "".join(c for c in number_str if c.isdigit())
    if len(digits) < 8:
        return True
    if digits.count(digits[0]) >= len(digits) - 1:
        return True
    return False


def _is_probably_premium(num_obj):
    t = number_type(num_obj)
    return t in (
        PhoneNumberType.PREMIUM_RATE,
        PhoneNumberType.SHARED_COST,
        PhoneNumberType.UAN,
    )


def _is_probably_voip(num_obj):
    t = number_type(num_obj)
    return t in (
        PhoneNumberType.VOIP,
        PhoneNumberType.PERSONAL_NUMBER,
    )


def _whatsapp_probability(num_obj, raw):
    digits = "".join(c for c in raw if c.isdigit())
    t = number_type(num_obj)

    score = 0

    if t == PhoneNumberType.MOBILE:
        score += 3

    if t == PhoneNumberType.VOIP:
        score += 2

    if t == PhoneNumberType.PREMIUM_RATE:
        score -= 3

    if 9 <= len(digits) <= 12:
        score += 1

    if _is_probably_temp(raw):
        score -= 1

    if score >= 4:
        return "Molto probabile"
    elif score >= 2:
        return "Probabile"
    elif score >= 1:
        return "Possibile"
    else:
        return "Improbabile"


def run(target):
    results = []

    raw = str(target).strip()

    if raw.startswith("http://") or raw.startswith("https://"):
        results.append({
            "module": "phone_osint",
            "severity": "low",
            "title": "Input non telefonico",
            "description": "L'input fornito sembra essere un URL, non un numero di telefono.",
            "evidence": raw,
            "remediation": "Usa questo modulo solo con numeri di telefono (es: +393491234567)."
        })
        return results

    try:
        num = phonenumbers.parse(raw, None)
    except Exception as e:
        results.append({
            "module": "phone_osint",
            "severity": "low",
            "title": "Numero non valido",
            "description": f"Impossibile interpretare il numero: {e}",
            "evidence": raw,
            "remediation": "Verifica il prefisso internazionale e il formato del numero."
        })
        return results

    if not phonenumbers.is_possible_number(num):
        results.append({
            "module": "phone_osint",
            "severity": "low",
            "title": "Numero improbabile",
            "description": "Il numero non rientra nei range possibili per la nazione.",
            "evidence": raw,
            "remediation": "Controlla che il numero sia scritto correttamente."
        })

    if not phonenumbers.is_valid_number(num):
        results.append({
            "module": "phone_osint",
            "severity": "medium",
            "title": "Numero non valido",
            "description": "Il numero non risulta valido secondo il piano di numerazione.",
            "evidence": raw,
            "remediation": "Verifica il numero con una fonte affidabile."
        })

    region = geocoder.description_for_number(num, "it") or "Sconosciuto"
    results.append({
        "module": "phone_osint",
            "severity": "info",
            "title": "Informazioni geografiche",
            "description": f"Il numero risulta associato a: {region}",
            "evidence": region,
            "remediation": None
    })

    carrier_name = carrier.name_for_number(num, "it") or "Sconosciuto"
    results.append({
        "module": "phone_osint",
        "severity": "info",
        "title": "Operatore telefonico",
        "description": f"Operatore rilevato: {carrier_name}",
        "evidence": carrier_name,
        "remediation": None
    })

    t = number_type(num)
    type_map = {
        PhoneNumberType.MOBILE: "Mobile",
        PhoneNumberType.FIXED_LINE: "Fisso",
        PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fisso o Mobile",
        PhoneNumberType.TOLL_FREE: "Numero verde",
        PhoneNumberType.PREMIUM_RATE: "Tariffazione speciale",
        PhoneNumberType.SHARED_COST: "Costo condiviso",
        PhoneNumberType.VOIP: "VoIP",
        PhoneNumberType.PERSONAL_NUMBER: "Personale",
        PhoneNumberType.PAGER: "Pager",
        PhoneNumberType.UAN: "UAN",
        PhoneNumberType.UNKNOWN: "Sconosciuto",
    }
    type_label = type_map.get(t, "Sconosciuto")

    results.append({
        "module": "phone_osint",
        "severity": "info",
        "title": "Tipo di linea",
        "description": f"Tipo di linea rilevato: {type_label}",
        "evidence": type_label,
        "remediation": None
    })

    if _is_probably_voip(num):
        results.append({
            "module": "phone_osint",
            "severity": "medium",
            "title": "Possibile numero VoIP",
            "description": "Il numero sembra appartenere a un servizio VoIP.",
            "evidence": type_label,
            "remediation": "I numeri VoIP sono spesso usati per registrazioni rapide."
        })

    if _is_probably_premium(num):
        results.append({
            "module": "phone_osint",
            "severity": "high",
            "title": "Possibile numero a tariffazione speciale",
            "description": "Il numero potrebbe essere associato a servizi a pagamento.",
            "evidence": type_label,
            "remediation": "Evita di chiamare se non sei sicuro della provenienza."
        })

    if _is_probably_temp(raw):
        results.append({
            "module": "phone_osint",
            "severity": "medium",
            "title": "Possibile numero temporaneo o fake",
            "description": "Il formato suggerisce che possa essere un numero temporaneo.",
            "evidence": raw,
            "remediation": "Non usarlo per comunicazioni critiche."
        })

    wa_status = _whatsapp_probability(num, raw)
    results.append({
        "module": "phone_osint",
        "severity": "info",
        "title": "Probabilità presenza WhatsApp",
        "description": f"Valutazione OSINT: {wa_status}",
        "evidence": wa_status,
        "remediation": None
    })

    return results

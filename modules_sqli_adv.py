import requests

ERROR_PATTERNS = [
    "SQL syntax",
    "mysql_fetch",
    "ORA-01756",
    "SQLSTATE",
    "Unclosed quotation mark",
    "Warning: pg_",
]

PAYLOADS = [
    "'",
    "\"",
    "' OR '1'='1",
    "\" OR \"1\"=\"1",
]

def test_errors(text):
    for p in ERROR_PATTERNS:
        if p.lower() in text.lower():
            return p
    return None

def run(target):
    results = []

    # GET
    try:
        for payload in PAYLOADS:
            r = requests.get(target + payload, timeout=10)
            err = test_errors(r.text)
            if err:
                results.append({
                    "module": "sqli_adv",
                    "severity": "high",
                    "title": "SQL Injection (GET)",
                    "description": "Possibile SQLi tramite GET.",
                    "evidence": f"Pattern: {err}",
                    "remediation": "Usa query parametrizzate e sanifica i parametri."
                })
                break
    except:
        pass

    # POST
    try:
        for payload in PAYLOADS:
            r = requests.post(target, data={"test": payload}, timeout=10)
            err = test_errors(r.text)
            if err:
                results.append({
                    "module": "sqli_adv",
                    "severity": "high",
                    "title": "SQL Injection (POST)",
                    "description": "Possibile SQLi tramite POST.",
                    "evidence": f"Payload: {payload} — Pattern: {err}",
                    "remediation": "Valida e sanifica i dati in input."
                })
                break
    except:
        pass

    # JSON
    try:
        for payload in PAYLOADS:
            r = requests.post(target, json={"test": payload}, timeout=10)
            err = test_errors(r.text)
            if err:
                results.append({
                    "module": "sqli_adv",
                    "severity": "critical",
                    "title": "SQL Injection (JSON API)",
                    "description": "Possibile SQLi tramite endpoint JSON.",
                    "evidence": f"Payload: {payload} — Pattern: {err}",
                    "remediation": "Valida e sanifica i payload JSON lato server."
                })
                break
    except:
        pass

    return results

import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

ERROR_PATTERNS = [
    "You have an error in your SQL syntax",
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

def inject_url(url, param, payload):
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)
    if param not in qs:
        return None
    qs[param] = [qs[param][0] + payload]
    new_query = urlencode(qs, doseq=True)
    return urlunparse(parsed._replace(query=new_query))

def run(target):
    results = []

    parsed = urlparse(target)
    params = parse_qs(parsed.query)
    if not params:
        return results

    for param in params:
        for payload in PAYLOADS:
            test_url = inject_url(target, param, payload)
            if not test_url:
                continue
            try:
                r = requests.get(test_url, timeout=10)
                body = r.text
                for pattern in ERROR_PATTERNS:
                    if pattern.lower() in body.lower():
                        results.append({
                            "module": "sqli",
                            "severity": "high",
                            "title": "Possibile SQL Injection (GET)",
                            "description": f"Parametro vulnerabile: {param}",
                            "evidence": f"Payload: {payload} — Pattern: {pattern}",
                            "remediation": "Usa query parametrizzate e sanifica i parametri."
                        })
                        break
            except:
                continue

    return results

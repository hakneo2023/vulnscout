import requests
from urllib.parse import urljoin

WORDLIST = [
    "admin",
    "login",
    "backup",
    "old",
    ".git",
    ".env",
]

def run(target):
    results = []

    for path in WORDLIST:
        url = urljoin(target.rstrip("/") + "/", path)
        try:
            r = requests.get(url, timeout=5, allow_redirects=False)
            if r.status_code in (200, 301, 302, 403):
                results.append({
                    "module": "dirs",
                    "severity": "info",
                    "title": "Percorso interessante trovato",
                    "description": f"{url} restituisce status {r.status_code}",
                    "evidence": None,
                    "remediation": None
                })
        except:
            continue

    return results

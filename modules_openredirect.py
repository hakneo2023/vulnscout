import requests

def run(target):
    results = []

    payloads = [
        "?redirect=http://evil.com",
        "?url=http://evil.com",
        "?next=http://evil.com",
        "?dest=http://evil.com"
    ]

    for p in payloads:
        try:
            r = requests.get(target + p, allow_redirects=False, timeout=5)
            if "evil.com" in str(r.headers).lower():
                results.append(f"Possibile Open Redirect: {target+p}")
        except:
            pass

    if not results:
        results.append("Nessun Open Redirect rilevato.")

    return results

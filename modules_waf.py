import requests

def run(target):
    results = []

    waf_signatures = {
        "cloudflare": "cloudflare",
        "sucuri": "sucuri",
        "mod_security": "mod_security",
        "imperva": "incapsula"
    }

    try:
        r = requests.get(target, timeout=5)
        headers = str(r.headers).lower()

        for waf, sig in waf_signatures.items():
            if sig in headers:
                results.append(f"WAF rilevato: {waf}")

        if not results:
            results.append("Nessun WAF rilevato.")

    except Exception as e:
        results.append(f"Errore WAF: {e}")

    return results

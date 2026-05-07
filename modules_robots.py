import requests

def run(target):
    results = []

    if not target.endswith("/"):
        target += "/"

    url = target + "robots.txt"

    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            lines = r.text.splitlines()
            for l in lines:
                if "disallow" in l.lower():
                    results.append(f"Robots entry: {l}")
        else:
            results.append("robots.txt non trovato.")
    except Exception as e:
        results.append(f"Errore robots.txt: {e}")

    return results

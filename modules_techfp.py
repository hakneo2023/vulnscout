import requests

def run(target):
    results = []

    try:
        r = requests.get(target, timeout=5)
        headers = r.headers

        tech = []

        if "server" in headers:
            tech.append(f"Server: {headers['server']}")

        if "x-powered-by" in headers:
            tech.append(f"Powered-By: {headers['x-powered-by']}")

        if "set-cookie" in headers:
            if "php" in headers["set-cookie"].lower():
                tech.append("PHP detected")
            if "asp" in headers["set-cookie"].lower():
                tech.append("ASP.NET detected")

        if "<meta name=\"generator\"" in r.text.lower():
            tech.append("CMS detected (generator tag)")

        if tech:
            results.extend(tech)
        else:
            results.append("Nessuna tecnologia rilevata.")

    except Exception as e:
        results.append(f"Errore Fingerprinting: {e}")

    return results

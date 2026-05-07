import requests

def run(target):
    results = []

    # Normalizzazione URL
    if not target.startswith("http://") and not target.startswith("https://"):
        target = "https://" + target

    # Tentativo HTTPS → fallback HTTP
    try:
        r = requests.get(target, timeout=10, allow_redirects=True)
    except:
        # Se HTTPS fallisce → prova HTTP
        if target.startswith("https://"):
            target = target.replace("https://", "http://", 1)
            try:
                r = requests.get(target, timeout=10, allow_redirects=True)
            except Exception as e:
                results.append({
                    "module": "headers",
                    "severity": "low",
                    "title": "Errore analisi header",
                    "description": str(e),
                    "evidence": None,
                    "remediation": None
                })
                return results
        else:
            results.append({
                "module": "headers",
                "severity": "low",
                "title": "Errore analisi header",
                "description": "Impossibile connettersi al target.",
                "evidence": None,
                "remediation": None
            })
            return results

    # DEBUG — per capire cosa succede davvero
import requests

def run(target):
    results = []

    try:
        r = requests.get(target, timeout=10)
        acao = r.headers.get("Access-Control-Allow-Origin")

        if acao == "*":
            results.append({
                "module": "cors",
                "severity": "medium",
                "title": "CORS troppo permissivo",
                "description": "Access-Control-Allow-Origin è impostato su '*'.",
                "evidence": f"Access-Control-Allow-Origin: {acao}",
                "remediation": "Restringi l'origine a domini specifici."
            })

    except Exception as e:
        results.append({
            "module": "cors",
            "severity": "low",
            "title": "Errore analisi CORS",
            "description": str(e),
            "evidence": None,
            "remediation": None
        })

    return results

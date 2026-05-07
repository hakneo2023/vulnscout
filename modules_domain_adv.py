import requests

def run(target):
    results = []

    dominio = target.replace("https://", "").replace("http://", "").split("/")[0]
    results.append(f"[DOM-ADV] Dominio analizzato: {dominio}")

    # Subdomain enumeration via crt.sh (scraping pubblico)
    try:
        url = f"https://crt.sh/?q=%25.{dominio}&output=json"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            try:
                data = r.json()
                subdomains = set()
                for entry in data:
                    name = entry.get("name_value", "")
                    for line in name.split("\n"):
                        if line.endswith(dominio):
                            subdomains.add(line.strip())
                if subdomains:
                    for s in sorted(subdomains):
                        results.append(f"[DOM-ADV] Subdomain: {s}")
                else:
                    results.append("[DOM-ADV] Nessun subdomain trovato.")
            except:
                results.append("[DOM-ADV] Impossibile parsare risposta crt.sh.")
        else:
            results.append("[DOM-ADV] crt.sh non disponibile.")
    except Exception as e:
        results.append(f"[DOM-ADV] Errore crt.sh: {e}")

    return results

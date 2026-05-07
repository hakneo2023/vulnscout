# modules_osint_ip_adv.py

import requests

def add(results, title, description, severity="info"):
    results.append({
        "severity": severity,
        "module": "osint_ip_adv",
        "title": title,
        "description": description
    })

def run(ip):
    results = []

    # IPINFO
    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        data = r.json()
        for k, v in data.items():
            add(results, f"IPInfo: {k}", str(v))
    except:
        add(results, "IPInfo", "Errore durante la richiesta")

    # SHODAN InternetDB
    try:
        r = requests.get(f"https://internetdb.shodan.io/{ip}", timeout=5)
        data = r.json()

        ports = data.get("ports", [])
        vulns = data.get("vulns", [])

        add(results, "Porte aperte", str(ports))
        add(results, "Vulnerabilità note", str(vulns), severity="medium" if vulns else "info")

    except:
        add(results, "Shodan InternetDB", "Errore durante la richiesta")

    # GEOIP
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = r.json()

        if data.get("status") == "success":
            add(results, "Geolocalizzazione", f"{data.get('country')} - {data.get('city')} (ISP: {data.get('isp')})")
        else:
            add(results, "Geolocalizzazione", "Non disponibile")
    except:
        add(results, "Geolocalizzazione", "Errore durante la richiesta")

    return results

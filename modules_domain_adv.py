# modules_domain_adv.py

import dns.resolver
import whois
import requests

def add(results, title, description, severity="info"):
    results.append({
        "severity": severity,
        "module": "domain_adv",
        "title": title,
        "description": description
    })

def run(target):
    results = []

    dominio = target.replace("https://", "").replace("http://", "").split("/")[0]
    add(results, "Dominio analizzato", dominio)

    # WHOIS
    try:
        w = whois.whois(dominio)

        add(results, "WHOIS - Registrar", str(w.get("registrar", "N/A")))
        add(results, "WHOIS - Organization", str(w.get("org", "N/A")))
        add(results, "WHOIS - Country", str(w.get("country", "N/A")))
        add(results, "WHOIS - Creation Date", str(w.get("creation_date", "N/A")))
        add(results, "WHOIS - Expiration Date", str(w.get("expiration_date", "N/A")))

        email = w.get("emails")
        add(results, "WHOIS - Email registrant", str(email) if email else "Non disponibile")

    except Exception as e:
        add(results, "WHOIS", f"Errore WHOIS: {e}")

    # DNS A
    try:
        a = dns.resolver.resolve(dominio, "A")
        for r in a:
            add(results, "Record A", r.address)
    except:
        add(results, "Record A", "Nessun record A")

    # DNS AAAA
    try:
        aaaa = dns.resolver.resolve(dominio, "AAAA")
        for r in aaaa:
            add(results, "Record AAAA", r.address)
    except:
        add(results, "Record AAAA", "Nessun record AAAA")

    # DNS MX
    try:
        mx = dns.resolver.resolve(dominio, "MX")
        for r in mx:
            add(results, "Record MX", str(r.exchange))
    except:
        add(results, "Record MX", "Nessun MX")

    # DNS NS
    try:
        ns = dns.resolver.resolve(dominio, "NS")
        for r in ns:
            add(results, "Record NS", str(r.target))
    except:
        add(results, "Record NS", "Nessun NS")

    # DNS TXT
    try:
        txt = dns.resolver.resolve(dominio, "TXT")
        for r in txt:
            add(results, "Record TXT", str(r))
    except:
        add(results, "Record TXT", "Nessun TXT")

    # Domini correlati
    try:
        url = f"https://api.hackertarget.com/hostsearch/?q={dominio}"
        r = requests.get(url, timeout=5).text.strip()

        if "error" not in r.lower():
            lines = r.split("\n")
            for line in lines[:10]:
                add(results, "Dominio correlato", line)
        else:
            add(results, "Domini correlati", "Nessun risultato")
    except:
        add(results, "Domini correlati", "Errore durante la ricerca")

    return results

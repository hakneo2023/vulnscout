import re
import socket
import requests
import dns.resolver
import whois

def add(results, title, description, severity="info"):
    results.append({
        "severity": severity,
        "module": "osint_adv",
        "title": title,
        "description": description
    })

def run(target):
    results = []

    # -------------------------
    # 1) EMAIL CHECK
    # -------------------------
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(email_regex, target):
        add(results, "Email rilevata", target)

        dominio = target.split("@")[1]
        add(results, "Dominio email", dominio)

        # MX
        try:
            mx = dns.resolver.resolve(dominio, "MX")
            for r in mx:
                add(results, "Record MX", str(r.exchange))
        except:
            add(results, "Record MX", "Nessun MX trovato")

        # SPF
        try:
            spf = dns.resolver.resolve(dominio, "TXT")
            for r in spf:
                if "spf" in str(r).lower():
                    add(results, "Record SPF", str(r))
        except:
            add(results, "Record SPF", "Nessun SPF trovato")

        # DMARC
        try:
            dmarc = dns.resolver.resolve("_dmarc." + dominio, "TXT")
            for r in dmarc:
                add(results, "Record DMARC", str(r))
        except:
            add(results, "Record DMARC", "Nessun DMARC trovato")

        return results

    # -------------------------
    # 2) IP CHECK
    # -------------------------
    ip_regex = r"^\d{1,3}(\.\d{1,3}){3}$"
    if re.match(ip_regex, target):
        add(results, "IP rilevato", target)

        # Reverse DNS
        try:
            rev = socket.gethostbyaddr(target)
            add(results, "Reverse DNS", rev[0])
        except:
            add(results, "Reverse DNS", "Nessun reverse DNS")

        # ASN lookup
        try:
            r = requests.get(f"https://ipinfo.io/{target}/json", timeout=5)
            data = r.json()
            for k, v in data.items():
                add(results, f"IP info: {k}", str(v))
        except:
            add(results, "ASN Lookup", "Fallito")

        return results

    # -------------------------
    # 3) DOMINIO CHECK
    # -------------------------
    add(results, "Dominio/URL rilevato", target)

    dominio = target.replace("https://", "").replace("http://", "").split("/")[0]

    # WHOIS
    try:
        w = whois.whois(dominio)
        add(results, "WHOIS - Org", str(w.get("org", "N/A")))
        add(results, "WHOIS - Country", str(w.get("country", "N/A")))
        add(results, "WHOIS - Registrar", str(w.get("registrar", "N/A")))
    except:
        add(results, "WHOIS", "Non disponibile")

    # DNS A
    try:
        a = dns.resolver.resolve(dominio, "A")
        for r in a:
            add(results, "Record A", r.address)
    except:
        add(results, "Record A", "Nessun record A")

    # MX
    try:
        mx = dns.resolver.resolve(dominio, "MX")
        for r in mx:
            add(results, "Record MX", str(r.exchange))
    except:
        add(results, "Record MX", "Nessun MX")

    # NS
    try:
        ns = dns.resolver.resolve(dominio, "NS")
        for r in ns:
            add(results, "Record NS", str(r.target))
    except:
        add(results, "Record NS", "Nessun NS")

    # SPF
    try:
        spf = dns.resolver.resolve(dominio, "TXT")
        for r in spf:
            if "spf" in str(r).lower():
                add(results, "Record SPF", str(r))
    except:
        add(results, "Record SPF", "Nessun SPF")

    # Server web
    try:
        r = requests.get("http://" + dominio, timeout=5)
        if "server" in r.headers:
            add(results, "Web Server", r.headers["server"])
        else:
            add(results, "Web Server", "Header server non presente")
    except:
        add(results, "Web Server", "Nessuna risposta HTTP")

    return results

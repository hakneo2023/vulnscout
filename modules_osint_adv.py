import re
import socket
import requests
import dns.resolver
import whois

def run(target):
    results = []

    # -------------------------
    # 1) EMAIL CHECK
    # -------------------------
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(email_regex, target):
        results.append(f"[EMAIL] Rilevata email: {target}")
        dominio = target.split("@")[1]
        results.append(f"[EMAIL] Dominio estratto: {dominio}")

        # MX
        try:
            mx = dns.resolver.resolve(dominio, "MX")
            for r in mx:
                results.append(f"[EMAIL] MX: {r.exchange}")
        except:
            results.append("[EMAIL] Nessun MX trovato")

        # SPF
        try:
            spf = dns.resolver.resolve(dominio, "TXT")
            for r in spf:
                if "spf" in str(r).lower():
                    results.append(f"[EMAIL] SPF: {r}")
        except:
            results.append("[EMAIL] Nessun SPF trovato")

        # DMARC
        try:
            dmarc = dns.resolver.resolve("_dmarc." + dominio, "TXT")
            for r in dmarc:
                results.append(f"[EMAIL] DMARC: {r}")
        except:
            results.append("[EMAIL] Nessun DMARC trovato")

        return results

    # -------------------------
    # 2) IP CHECK
    # -------------------------
    ip_regex = r"^\d{1,3}(\.\d{1,3}){3}$"
    if re.match(ip_regex, target):
        results.append(f"[IP] Rilevato IP: {target}")

        # Reverse DNS
        try:
            rev = socket.gethostbyaddr(target)
            results.append(f"[IP] Reverse DNS: {rev[0]}")
        except:
            results.append("[IP] Nessun reverse DNS")

        # ASN lookup (via API pubblica)
        try:
            r = requests.get(f"https://ipinfo.io/{target}/json", timeout=5)
            data = r.json()
            for k, v in data.items():
                results.append(f"[IP] {k}: {v}")
        except:
            results.append("[IP] ASN lookup fallito")

        return results

    # -------------------------
    # 3) DOMINIO CHECK
    # -------------------------
    results.append(f"[DOMINIO] Rilevato dominio/URL: {target}")

    dominio = target.replace("https://", "").replace("http://", "").split("/")[0]

    # WHOIS
    try:
        w = whois.whois(dominio)
        results.append(f"[WHOIS] Registrant: {w.get('org', 'N/A')}")
        results.append(f"[WHOIS] Country: {w.get('country', 'N/A')}")
        results.append(f"[WHOIS] Registrar: {w.get('registrar', 'N/A')}")
    except:
        results.append("[WHOIS] WHOIS non disponibile")

    # DNS A
    try:
        a = dns.resolver.resolve(dominio, "A")
        for r in a:
            results.append(f"[DNS] A: {r.address}")
    except:
        results.append("[DNS] Nessun record A")

    # MX
    try:
        mx = dns.resolver.resolve(dominio, "MX")
        for r in mx:
            results.append(f"[DNS] MX: {r.exchange}")
    except:
        results.append("[DNS] Nessun MX")

    # NS
    try:
        ns = dns.resolver.resolve(dominio, "NS")
        for r in ns:
            results.append(f"[DNS] NS: {r.target}")
    except:
        results.append("[DNS] Nessun NS")

    # SPF
    try:
        spf = dns.resolver.resolve(dominio, "TXT")
        for r in spf:
            if "spf" in str(r).lower():
                results.append(f"[DNS] SPF: {r}")
    except:
        results.append("[DNS] Nessun SPF")

    # Server web
    try:
        r = requests.get("http://" + dominio, timeout=5)
        if "server" in r.headers:
            results.append(f"[WEB] Server: {r.headers['server']}")
    except:
        results.append("[WEB] Nessuna risposta HTTP")

    return results

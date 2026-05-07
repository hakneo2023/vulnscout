import re
import socket
import requests

def run(target):
    results = []

    ip_regex = r"^\d{1,3}(\.\d{1,3}){3}$"
    if not re.match(ip_regex, target):
        results.append(f"[IP-ADV] '{target}' non sembra un IP valido.")
        return results

    ip = target.strip()
    results.append(f"[IP-ADV] IP analizzato: {ip}")

    # Reverse DNS
    try:
        rev = socket.gethostbyaddr(ip)
        results.append(f"[IP-ADV] Reverse DNS: {rev[0]}")
    except:
        results.append("[IP-ADV] Nessun reverse DNS.")

    # GeoIP free (ipinfo.io)
    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        data = r.json()
        for k in ["city", "region", "country", "org", "loc"]:
            if k in data:
                results.append(f"[IP-ADV] {k}: {data[k]}")
    except:
        results.append("[IP-ADV] GeoIP non disponibile.")

    # Porte base 80/443
    for port in [80, 443]:
        try:
            s = socket.socket()
            s.settimeout(2)
            res = s.connect_ex((ip, port))
            if res == 0:
                results.append(f"[IP-ADV] Porta aperta: {port}")
            s.close()
        except:
            pass

    return results

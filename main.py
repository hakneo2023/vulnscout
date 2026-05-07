import sys
from banner import matrix_banner, HACK_NEO_ASCII
import modules_lookup
import report
import report_html

# -------------------------
# COLORI ANSI PER MODULO
# -------------------------
def color_for_module(name):
    colors = {
        "headers": "\033[92m",
        "cors": "\033[93m",
        "dirs": "\033[96m",
        "sqli": "\033[91m",
        "sqli_adv": "\033[31m",
        "xss": "\033[95m",
        "phone_osint": "\033[94m",
        "fingerprinting": "\033[36m",
        "ssl": "\033[92m",
        "techfp": "\033[96m",
        "waf": "\033[33m",
        "openredirect": "\033[95m",
        "robots": "\033[90m",
        "osint_adv": "\033[92m",
        "osint_social": "\033[95m",
        "osint_ip_adv": "\033[94m",
        "osint_domain_adv": "\033[96m",
        "osint_email_breach": "\033[93m"
    }
    return colors.get(name, "\033[0m")


def show_menu():
    print("\nSeleziona il modulo da eseguire:")
    print("1) Headers")
    print("2) CORS")
    print("3) Directory Scanner")
    print("4) SQLi (base)")
    print("5) SQLi Avanzato")
    print("6) XSS")
    print("7) Phone OSINT PRO")
    print("8) Fingerprinting ULTRA")
    print("9) Tutti i moduli")
    print("10) TEST (debug)")
    print("11) SSL Analyzer")
    print("12) Technology Fingerprinting PRO")
    print("13) WAF Detector")
    print("14) Open Redirect Scanner")
    print("15) Robots.txt Analyzer")
    print("16) OSINT Avanzato (email/IP/dominio)")
    print("17) OSINT Social (username)")
    print("18) OSINT IP Avanzato")
    print("19) OSINT Dominio Avanzato (subdomains)")
    print("20) OSINT Email Breach Check")
    print("0) Esci")

    scelta = input("\nInserisci il numero del modulo: ")

    mapping = {
        "1": "headers",
        "2": "cors",
        "3": "dirs",
        "4": "sqli",
        "5": "sqli_adv",
        "6": "xss",
        "7": "phone_osint",
        "8": "fingerprinting",
        "9": "all",
        "10": "test",
        "11": "ssl",
        "12": "techfp",
        "13": "waf",
        "14": "openredirect",
        "15": "robots",
        "16": "osint_adv",
        "17": "osint_social",
        "18": "osint_ip_adv",
        "19": "osint_domain_adv",
        "20": "osint_email_breach"
    }

    return mapping.get(scelta, None)


def main():
    matrix_banner(HACK_NEO_ASCII)

    selected_module = show_menu()

    if selected_module is None:
        print("Scelta non valida. Uscita.")
        sys.exit(0)

    target = input("\nInserisci il target (URL, IP, email, username o numero di telefono): ")

    if not target.strip():
        print("Errore: target non valido.")
        sys.exit(1)

    all_modules = modules_lookup.MODULES

    print("\n[DEBUG] Moduli caricati dal lookup:", list(all_modules
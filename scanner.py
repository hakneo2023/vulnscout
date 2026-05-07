import argparse
import requests
import random
import time

import modules_lookup
import report
import report_html


class Scanner:
    def __init__(self, url):
        self.url = url

        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Version/17.0 Safari/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/124.0",
        ]

    def normalize_url(self, url):
        url = url.strip()
        if url.startswith("http://") or url.startswith("https://"):
            return url
        return "https://" + url

    def fetch(self, url=None, retries=3):
        if url is None:
            url = self.url
        url = self.normalize_url(url)

        for attempt in range(retries):
            try:
                headers = {
                    "User-Agent": random.choice(self.user_agents),
                    "Accept-Language": "en-US,en;q=0.9",
                    "Accept": "*/*"
                }
                response = requests.get(
                    url,
                    headers=headers,
                    timeout=10,
                    allow_redirects=True
                )
                return response
            except Exception as e:
                print(f"[!] Tentativo {attempt+1} fallito: {e}")
                time.sleep(1)

        print("[!] Nessuna risposta dopo vari tentativi.")
        return None


def parse_args():
    parser = argparse.ArgumentParser(
        description="VulnScout - Web Scanner & Phone OSINT"
    )
    parser.add_argument("target", help="URL o numero di telefono")
    parser.add_argument(
        "--modules",
        nargs="+",
        default=["all"],
        help="Moduli da eseguire (es: headers cors dirs sqli xss phone_osint sqli_adv)"
    )
    parser.add_argument(
        "--report",
        choices=["console", "html", "both"],
        default="console",
        help="Tipo di report"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    target = args.target
    selected_modules = args.modules

    print(f"[+] Target: {target}")
    print(f"[+] Moduli richiesti: {', '.join(selected_modules)}")

    all_modules = modules_lookup.MODULES

    if "all" in selected_modules:
        to_run = list(all_modules.keys())
    else:
        to_run = [m for m in selected_modules if m in all_modules]

    if not to_run:
        print("[!] Nessun modulo valido selezionato.")
        return

    results = []

    for name in to_run:
        module = all_modules[name]
        print(f"\n[+] Esecuzione modulo: {name}")
        try:
            findings = module.run(target)
            if findings:
                results.extend(findings)
        except Exception as e:
            print(f"[!] Errore nel modulo {name}: {e}")

    # Report
    if args.report in ("console", "both"):
        report.print_console_report(target, results)

    if args.report in ("html", "both"):
        report_html.generate_html_report(target, results)


if __name__ == "__main__":
    main()

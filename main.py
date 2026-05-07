import sys
from banner import matrix_banner, HACK_NEO_ASCII
import modules_lookup
import report
import report_html


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
        "10": "test"
    }

    return mapping.get(scelta, None)


def main():
    # Banner iniziale (non blocca nulla)
    matrix_banner(HACK_NEO_ASCII)

    selected_module = show_menu()

    if selected_module is None:
        print("Scelta non valida. Uscita.")
        sys.exit(0)

    target = input("\nInserisci il target (URL o numero di telefono): ")

    if not target.strip():
        print("Errore: target non valido.")
        sys.exit(1)

    all_modules = modules_lookup.MODULES

    print("\n[DEBUG] Moduli caricati dal lookup:", list(all_modules.keys()))

    if selected_module == "all":
        to_run = list(all_modules.keys())
    else:
        if selected_module not in all_modules:
            print("[!] Modulo non valido.")
            sys.exit(1)
        to_run = [selected_module]

    print(f"\n[+] Target: {target}")
    print(f"[+] Moduli richiesti: {', '.join(to_run)}")

    results = []

    # Esecuzione moduli
    for name in to_run:
        module = all_modules[name]
        print(f"\n[+] Esecuzione modulo: {name}")

        try:
            findings = module.run(target)
            print(f"[DEBUG] Il modulo '{name}' ha restituito {len(findings) if findings else 0} risultati")

            if findings:
                results.extend(findings)

        except Exception as e:
            print(f"[!] Errore nel modulo {name}: {e}")

    print(f"\n[DEBUG] Totale risultati raccolti: {len(results)}")

    # Stampa report
    report.print_console_report(target, results)
    report_html.generate_html_report(target, results)

    print("\n[+] Scansione completata.\n")


if __name__ == "__main__":
    main()

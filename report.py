def print_console_report(target, results):
    print("\n================ REPORT VULNSCOUT ================")
    print(f"Target: {target}")
    print(f"Totale risultati: {len(results)}")
    print("--------------------------------------------------")

    if not results:
        print("Nessun problema rilevato.")
        return

    for r in results:
        # Se r è una stringa, stampala direttamente
        if isinstance(r, str):
            print(f"[INFO] {r}")
            print("--------------------------------------------------")
            continue

        # Se r è un dizionario, stampa i dettagli
        print(f"[{r.get('severity', 'info').upper()}] ({r.get('module', 'unknown')}) {r.get('title', '')}")
        print(f" - {r.get('description', '')}")
        if r.get("evidence"):
            print(f"   Evidence: {r['evidence']}")
        if r.get("remediation"):
            print(f"   Fix: {r['remediation']}")
        print("--------------------------------------------------")

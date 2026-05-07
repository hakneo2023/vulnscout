def print_console_report(target, results):
    print("\n================= REPORT VULNSCOUT =================")
    print(f"Target: {target}")
    print(f"Totale risultati: {len(results)}")
    print("----------------------------------------------------")

    if not results:
        print("Nessun problema rilevato.")
        return

    for r in results:
        print(f"[{r['severity'].upper()}] ({r['module']}) {r['title']}")
        print(f"  - {r['description']}")
        if r.get("evidence"):
            print(f"    Evidence: {r['evidence']}")
        if r.get("remediation"):
            print(f"    Fix: {r['remediation']}")
        print("----------------------------------------------------")

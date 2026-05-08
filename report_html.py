def generate_html_report(target, results):
    from datetime import datetime
    filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("<html><head><meta charset='utf-8'><title>VulnScout Report</title></head><body>")
        f.write(f"<h1>VulnScout Report</h1>")
        f.write(f"<p><b>Target:</b> {target}</p>")
        f.write(f"<p><b>Totale risultati:</b> {len(results)}</p><hr>")

        if not results:
            f.write("<p><b>Nessun problema rilevato.</b></p>")
        else:
            for r in results:
                if isinstance(r, str):
                    f.write(f"<p>[INFO] {r}</p><hr>")
                    continue

                f.write(f"<h3>[{r.get('severity', 'info').upper()}] ({r.get('module', 'unknown')}) {r.get('title', '')}</h3>")
                f.write(f"<p>{r.get('description', '')}</p>")
                if r.get("evidence"):
                    f.write(f"<p><b>Evidence:</b> {r['evidence']}</p>")
                if r.get("remediation"):
                    f.write(f"<p><b>Fix:</b> {r['remediation']}</p>")
                f.write("<hr>")

        f.write("</body></html>")

    print(f"[+] Report HTML generato: {filename}")

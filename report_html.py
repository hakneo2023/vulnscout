from datetime import datetime

def generate_html_report(target, results):
    filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("<html><head><meta charset='utf-8'>")
        f.write("<title>VulnScout Report</title></head><body>")
        f.write(f"<h1>VulnScout Report</h1>")
        f.write(f"<p><b>Target:</b> {target}</p>")
        f.write(f"<p><b>Totale risultati:</b> {len(results)}</p>")
        f.write("<hr>")

        if not results:
            f.write("<p>Nessun problema rilevato.</p>")
        else:
            for r in results:
                f.write(f"<h3>[{r['severity'].upper()}] ({r['module']}) {r['title']}</h3>")
                f.write(f"<p>{r['description']}</p>")
                if r.get("evidence"):
                    f.write(f"<p><b>Evidence:</b> {r['evidence']}</p>")
                if r.get("remediation"):
                    f.write(f"<p><b>Fix:</b> {r['remediation']}</p>")
                f.write("<hr>")

        f.write("</body></html>")

    print(f"[+] Report HTML generato: {filename}")

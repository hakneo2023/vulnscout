# modules_robots.py

import requests

def add(results, title, description, severity="info"):
    results.append({
        "severity": severity,
        "module": "robots",
        "title": title,
        "description": description
    })

def run(target):
    results = []

    # Normalizza dominio
    if not target.startswith("http"):
        target = "http://" + target

    robots_url = target.rstrip("/") + "/robots.txt"

    try:
        r = requests.get(robots_url, timeout=5)

        if r.status_code == 200:
            add(results, "robots.txt trovato", robots_url)
            lines = r.text.split("\n")

            for line in lines:
                line = line.strip()
                if line:
                    add(results, "Entry robots.txt", line)
        else:
            add(results, "robots.txt", f"Non trovato (HTTP {r.status_code})")

    except Exception as e:
        add(results, "Errore robots.txt", str(e), severity="low")

    return results

# modules_osint_social.py

import requests

def add(results, title, description, severity="info"):
    results.append({
        "severity": severity,
        "module": "osint_social",
        "title": title,
        "description": description
    })

def run(username):
    results = []

    platforms = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://x.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}"
    }

    for name, url in platforms.items():
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                add(results, f"Profilo trovato su {name}", url)
            else:
                add(results, f"{name}", "Nessun profilo trovato")
        except:
            add(results, f"{name}", "Errore durante la verifica")

    return results

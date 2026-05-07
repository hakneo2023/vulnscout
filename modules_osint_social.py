import re
import requests

def run(target):
    results = []

    username = target.strip()

    # Controllo formato base
    if not re.match(r"^[a-zA-Z0-9_.-]{3,32}$", username):
        results.append(f"[SOCIAL] '{username}' non sembra uno username valido.")
        return results

    results.append(f"[SOCIAL] Username analizzato: {username}")

    piattaforme = {
        "Twitter/X": f"https://x.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "GitLab": f"https://gitlab.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
    }

    for nome, url in piattaforme.items():
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                results.append(f"[SOCIAL] Possibile profilo su {nome}: {url}")
        except:
            pass

    if len(results) == 1:
        results.append("[SOCIAL] Nessun profilo evidente trovato.")

    return results

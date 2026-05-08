# modules_osint_email_breach.py

import requests

def add(results, title, description, severity="info"):
    results.append({
        "severity": severity,
        "module": "osint_email_breach",
        "title": title,
        "description": description
    })

def run(email):
    results = []

    # Esempio con API di breach simulata / pubblica
    try:
        url = f"https://haveibeenpwned-api.terziario.fake/check?email={email}"
        # QUI: metti la tua vera API, oppure lascia come placeholder
        # simuliamo una risposta
        fake_response = {
            "found": True,
            "breaches": [
                {"name": "ExampleBreach", "date": "2020-01-01"},
                {"name": "AnotherLeak", "date": "2021-05-10"}
            ]
        }

        if fake_response.get("found"):
            add(results, "Email presente in breach database", email, severity="high")
            for b in fake_response.get("breaches", []):
                add(
                    results,
                    f"Breach: {b.get('name')}",
                    f"Data breach: {b.get('date')}",
                    severity="medium"
                )
        else:
            add(results, "Nessun breach trovato", email)

    except Exception as e:
        add(results, "Errore durante il controllo breach", str(e), severity="low")

    return results

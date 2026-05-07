import ssl
import socket
from datetime import datetime

def run(target):
    results = []

    try:
        hostname = target.replace("https://", "").replace("http://", "").split("/")[0]
        ctx = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with ctx.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()

        issuer = dict(x[0] for x in cert['issuer'])
        subject = dict(x[0] for x in cert['subject'])
        expires = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")

        results.append(f"SSL Subject: {subject.get('commonName', 'N/A')}")
        results.append(f"SSL Issuer: {issuer.get('organizationName', 'N/A')}")
        results.append(f"SSL Expiration: {expires}")
        results.append(f"SSL Valid: {datetime.utcnow() < expires}")

    except Exception as e:
        results.append(f"Errore SSL: {e}")

    return results

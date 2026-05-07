import requests
import hashlib
from urllib.parse import urljoin, urlparse


def _safe_get(url, allow_redirects=True):
    try:
        return requests.get(url, timeout=7, verify=False, allow_redirects=allow_redirects)
    except:
        return None


# ============================
#   FAVICON HASH DATABASE (DEMO)
# ============================

FAVICON_HASHES = {
    # Demo / placeholder hashes (esempi)
    "d41d8cd98f00b204e9800998ecf8427e": "Favicon vuota / mancante",
    "5d41402abc4b2a76b9719d911017c592": "Possibile WordPress",
    "9e107d9d372bb6826bd81d3542a419d6": "Possibile Joomla",
    "e4d909c290d0fb1ca068ffaddf22cbd0": "Possibile Drupal",
    "7c4ff521986b4ff8d2948a8c2a0d3f5d": "Possibile Magento",
    "8f14e45fceea167a5a36dedd4bea2543": "Possibile Shopify",
    "cf23df2207d99a74fbe169e3eba035e6": "Possibile Cloudflare",
    "45c48cce2e2d7fbdea1afc51c7c6ad26": "Possibile Akamai",
    "6512bd43d9caa6e02c990b0a82652dca": "Possibile Fastly",
}


def _fingerprint_favicon(url):
    favicon_url = urljoin(url, "/favicon.ico")
    r = _safe_get(favicon_url)
    if not r or not r.content:
        return None, None

    h_md5 = hashlib.md5(r.content).hexdigest()
    tech = FAVICON_HASHES.get(h_md5)
    return h_md5, tech


# ============================
#   HEADER FINGERPRINTING
# ============================

def _detect_headers(headers):
    findings = []

    server = headers.get("Server")
    powered = headers.get("X-Powered-By")
    via = headers.get("Via")
    alpn = headers.get("Alt-Svc")
    hsts = headers.get("Strict-Transport-Security")

    if server:
        findings.append(("Server", server))

    if powered:
        findings.append(("X-Powered-By", powered))

    if via:
        findings.append(("Via", via))

    if alpn:
        findings.append(("ALPN / Alt-Svc", alpn))

    if hsts:
        findings.append(("HSTS", hsts))

    # CDN detection
    if "x-akamai-transformed" in headers:
        findings.append(("CDN", "Akamai"))

    if "x-cache" in headers and "cloudfront" in headers.get("x-cache", "").lower():
        findings.append(("CDN", "CloudFront"))

    if any(h.lower().startswith("cf-") for h in headers.keys()):
        findings.append(("Reverse Proxy", "Cloudflare"))

    return findings


# ============================
#   COOKIE FINGERPRINTING
# ============================

def _detect_cookies(cookies):
    findings = []

    cookie_map = {
        "PHPSESSID": "PHP Session",
        "JSESSIONID": "Java Session",
        "ASP.NET_SessionId": "ASP.NET Session",
        "laravel_session": "Laravel",
        "csrftoken": "Django",
        "express.sid": "ExpressJS",
        "cfduid": "Cloudflare (storico)",
    }

    for c in cookies.keys():
        if c in cookie_map:
            findings.append(f"{c} ({cookie_map[c]})")

    return findings


# ============================
#   HTML / JS / CMS FINGERPRINTING
# ============================

def _detect_html(body):
    findings = []

    lower = body.lower()

    # Meta generator
    if 'meta name="generator"' in lower or "meta name='generator'" in lower:
        findings.append("Meta generator rilevato (possibile CMS)")

    # Backend framework
    if "laravel" in lower:
        findings.append("Framework backend: Laravel")

    if "symfony" in lower:
        findings.append("Framework backend: Symfony")

    if "django" in lower:
        findings.append("Framework backend: Django")

    if "express" in lower:
        findings.append("Framework backend: ExpressJS")

    # JS libs
    libs = {
        "jQuery": "jquery",
        "React": "react",
        "Vue.js": "vue",
        "Angular": "angular",
        "Bootstrap": "bootstrap",
    }

    for name, key in libs.items():
        if key in lower:
            findings.append(f"Libreria JS: {name}")

    return findings


def _detect_cms(body):
    findings = []
    lower = body.lower()

    if "wp-content" in lower or "wp-includes" in lower:
        findings.append("CMS: WordPress")

    if "/components/" in lower or "/modules/" in lower:
        findings.append("CMS: Joomla")

    if "/sites/default/" in lower:
        findings.append("CMS: Drupal")

    return findings


# ============================
#   STATIC RESOURCES FINGERPRINTING
# ============================

def _check_resource(url, path):
    full = urljoin(url, path)
    r = _safe_get(full)
    if r and r.status_code == 200:
        return True
    return False


def _detect_static_resources(url):
    findings = []

    resources = {
        "/robots.txt": "robots.txt presente",
        "/sitemap.xml": "sitemap.xml presente",
        "/manifest.json": "manifest.json presente (possibile PWA)",
        "/browserconfig.xml": "browserconfig.xml presente",
    }

    for path, desc in resources.items():
        if _check_resource(url, path):
            findings.append(desc)

    return findings


# ============================
#   TLS / PROTOCOL (BEST EFFORT)
# ============================

def _infer_protocol_info(response):
    findings = []

    # Non abbiamo accesso diretto a TLS handshake con requests,
    # ma possiamo inferire qualcosa da header e URL.
    url = response.url
    parsed = urlparse(url)

    if parsed.scheme == "https":
        findings.append("Connessione HTTPS attiva")

    hsts = response.headers.get("Strict-Transport-Security")
    if hsts:
        findings.append(f"HSTS abilitato: {hsts}")

    alpn = response.headers.get("Alt-Svc")
    if alpn and "h3" in alpn.lower():
        findings.append("Possibile supporto HTTP/3 (QUIC)")

    return findings


# ============================
#   MAIN MODULE
# ============================

def run(target):
    results = []

    r = _safe_get(target)
    if not r:
        return [{
            "module": "fingerprinting",
            "severity": "low",
            "title": "Impossibile analizzare il target",
            "description": "Il server non ha risposto o ha bloccato la richiesta.",
            "evidence": None,
            "remediation": None
        }]

    body = r.text
    headers = r.headers
    cookies = r.cookies

    # -----------------------------
    # FAVICON
    # -----------------------------
    fav_hash, fav_tech = _fingerprint_favicon(target)
    if fav_hash:
        desc = f"Hash favicon MD5: {fav_hash}"
        if fav_tech:
            desc += f" → {fav_tech}"
        results.append({
            "module": "fingerprinting",
            "severity": "info",
            "title": "Fingerprint favicon",
            "description": desc,
            "evidence": desc,
            "remediation": None
        })

    # -----------------------------
    # HEADERS
    # -----------------------------
    for kind, value in _detect_headers(headers):
        results.append({
            "module": "fingerprinting",
            "severity": "info",
            "title": f"Header: {kind}",
            "description": value,
            "evidence": value,
            "remediation": None
        })

    # -----------------------------
    # COOKIES
    # -----------------------------
    for ck in _detect_cookies(cookies):
        results.append({
            "module": "fingerprinting",
            "severity": "info",
            "title": "Cookie rilevato",
            "description": ck,
            "evidence": ck,
            "remediation": None
        })

    # -----------------------------
    # CMS
    # -----------------------------
    for c in _detect_cms(body):
        results.append({
            "module": "fingerprinting",
            "severity": "info",
            "title": "CMS rilevato",
            "description": c,
            "evidence": c,
            "remediation": None
        })

    # -----------------------------
    # HTML / JS / FRAMEWORK
    # -----------------------------
    for h in _detect_html(body):
        results.append({
            "module": "fingerprinting",
            "severity": "info",
            "title": "Tecnologia rilevata",
            "description": h,
            "evidence": h,
            "remediation": None
        })

    # -----------------------------
    # STATIC RESOURCES
    # -----------------------------
    for s in _detect_static_resources(target):
        results.append({
            "module": "fingerprinting",
            "severity": "info",
            "title": "Risorsa statica rilevata",
            "description": s,
            "evidence": s,
            "remediation": None
        })

    # -----------------------------
    # TLS / PROTOCOL INFO
    # -----------------------------
    for p in _infer_protocol_info(r):
        results.append({
            "module": "fingerprinting",
            "severity": "info",
            "title": "Informazioni protocollo",
            "description": p,
            "evidence": p,
            "remediation": None
        })

    if not results:
        results.append({
            "module": "fingerprinting",
            "severity": "info",
            "title": "Nessuna tecnologia rilevata",
            "description": "Non sono state trovate firme evidenti.",
            "evidence": None,
            "remediation": None
        })

    return results

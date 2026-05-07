# modules_lookup.py
# Mappa dei moduli disponibili in VulnScout

import modules_headers
import modules_cors
import modules_dirs
import modules_sqli
import modules_sqli_adv
import modules_xss
import modules_phone_osint
import modules_fingerprinting
import modules_test
import modules_ssl
import modules_techfp
import modules_waf
import modules_domain_adv
import modules_osint_email_breach
import modules_osint_adv   # <-- AGGIUNTO QUI

MODULES = {
    "headers": modules_headers,
    "cors": modules_cors,
    "dirs": modules_dirs,
    "sqli": modules_sqli,
    "sqli_adv": modules_sqli_adv,
    "xss": modules_xss,
    "phone_osint": modules_phone_osint,
    "fingerprinting": modules_fingerprinting,
    "test": modules_test,
    "ssl": modules_ssl,
    "techfp": modules_techfp,
    "waf": modules_waf,
    "domain_adv": modules_domain_adv,
    "osint_email_breach": modules_osint_email_breach,
    "osint_adv": modules_osint_adv   # <-- MODULO CORRETTO
}

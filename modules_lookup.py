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
import modules_openredirect
import modules_robots
import modules_osint_adv

import modules_osint_social
import modules_osint_ip_adv
import modules_osint_domain_adv
import modules_osint_email_breach

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
    "openredirect": modules_openredirect,
    "robots": modules_robots,
    "osint_adv": modules_osint_adv,

    "osint_social": modules_osint_social,
    "osint_ip_adv": modules_osint_ip_adv,
    "osint_domain_adv": modules_osint_domain_adv,
    "osint_email_breach": modules_osint_email_breach
}

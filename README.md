<p align="center">
  <img src="assets/logo.png" width="260" alt="Hack-Neo Logo">
</p>


# 🔍 VulnScout  
VulnScout is a lightweight web vulnerability reconnaissance tool designed for educational and authorized security testing. 
VulnScout è uno strumento leggero per la ricognizione delle vulnerabilità web, progettato per scopi didattici e per test di sicurezza autorizzati.

- - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - 

## ⚠️ Disclaimer  
This tool must only be used on systems you own or have explicit permission to test. 
Questo strumento deve essere utilizzato solo su sistemi di proprietà dell'utente o per i quali si dispone di un'autorizzazione esplicita per il test.


- - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - 



✨ Functionality

🛡️ 1. Headers
Analizza gli header HTTP di sicurezza.

Comando

python3 main.py https://sito.com --modules headers

Rileva
Content-Security-Policy mancante/debole

Strict-Transport-Security mancante

X-Frame-Options

X-Content-Type-Options

Referrer-Policy

Permissions-Policy

Server leak

leak
- - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - 


🌐 2. CORS

Analizza la configurazione Cross-Origin Resource Sharing.

Comando

python3 main.py https://sito.com --modules cors

Rileva
Access-Control-Allow-Origin

Access-Control-Allow-Credentials

Metodi pericolosi

Wildcard su header sensibili

Preflight OPTIONS

- - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - 

📁 3. Directory Scanner

Comando

python3 main.py https://sito.com --modules dirs

Rileva
directory comuni

file sensibili (.env, .git, backup.zip, db.sql)

directory indexing

status code anomali

- - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - 

🧬 4. SQLi (base)

Comando

python3 main.py "https://sito.com/page?id=1" --modules sqli

Rileva
SQLi error-based

SQLi boolean-based semplice

- - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - 

🧨 5. XSS (GET + POST + JSON)

Comando
python3 main.py "https://sito.com/page?test=1" --modules xss

python3 main.py "https://sito.com/page?test=1" --modules xss --aggressive

Rileva
XSS riflesso GET

XSS POST

XSS JSON

payload avanzati (modalità aggressiva)

- - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - 

📱 6. Phone OSINT PRO

Comando

python3 main.py +393491234567 --modules phone_osint

Rileva
validità numero

operatore

regione

tipo linea

VoIP

premium rate

numeri temporanei

probabilità WhatsApp

- - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - 

🧬 7. Fingerprinting ULTRA

Comando

python3 main.py https://sito.com --modules fingerprinting

Rileva
Tecnologie lato server
Apache, Nginx, LiteSpeed, IIS

Reverse proxy

CDN (Cloudflare, Akamai, Fastly, CloudFront)

HSTS, ALPN, HTTP/3

Tecnologie lato client
jQuery, React, Vue, Angular, Bootstrap

CMS
WordPress

Joomla

Drupal

Magento

Shopify

Cookie fingerprinting
PHPSESSID

JSESSIONID

ASP.NET_SessionId

laravel_session

csrftoken

express.sid

Favicon Hash (tecnica stile Shodan)
riconoscimento tramite hash MD5 della favicon

Risorse statiche
robots.txt

sitemap.xml

manifest.json

browserconfig.xml

- - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - 


🔍Scansione completa di un sito

Comando

python3 main.py https://target.com --modules all


- - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - 

🧩 Installazione

git clone https://github.com/USERNAME/vulnscout.git

cd vulnscout

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

to start the program python3 main.py http://www.example.it


- - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - 


🧑‍💻 Autore
Progetto sviluppato da Dany (hack-neo)
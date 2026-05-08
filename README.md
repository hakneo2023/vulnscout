<p align="center">
  <img src="assets/logo.png" width="260" alt="Hack-Neo Logo">
</p>

## 📸 Demo Screenshots

Una panoramica del funzionamento di **VulnScout**, con diversi moduli in azione:

<p align="center">
  <img src="screens/VulnScout.gif" width="100%">
</p>

La GIF mostra l’avvio del tool, l’esecuzione dei moduli principali e la generazione dei risultati.

# 🔍 VulnScout  
VulnScout is a lightweight web vulnerability reconnaissance tool designed for educational and authorized security testing

---

VulnScout è uno strumento leggero per la ricognizione delle vulnerabilità web, progettato per scopi didattici e per test di sicurezza autorizzati
- - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - 
## ⚠️ Disclaimer  
This tool must only be used on systems you own or have explicit permission to test 

---

Questo strumento deve essere utilizzato solo su sistemi di proprietà dell'utente o per i quali si dispone di un'autorizzazione esplicita per il test

- - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - 
# 🔧 Moduli di VulnScout 2.0

VulnScout 2.0 include 20 moduli di analisi passiva, OSINT e fingerprinting 
Ogni modulo è progettato per essere non distruttivo e conforme alle best practice OWASP

---

VulnScout 2.0 includes 20 passive analysis, OSINT and fingerprinting modules Each module is designed to be non-destructive and compliant with OWASP best practices

---
✨ Functionality
---
## 🛡️ 1) Headers
Analizza gli header HTTP del server

identifica configurazioni mancanti o deboli

CSP assente

cookie insicuri

server exposure 

---
## 🔄 2) CORS Analyzer
Valuta la configurazione Cross-Origin Resource Sharing

wildcard pericolose

policy permissive.  

---
## 📁 3) Directory Scanner
Scanner passivo per directory e file esposti 
backup

configurazioni

cartelle sensibili

---
## 🧩 4) SQLi (base)
Rilevamento passivo di SQL Injection  

error-based SQLi

parametri vulnerabili

---
## 🧬 5) SQLi Avanzato
Analisi avanzata con payload complessi

time-based

boolean-based SQLi

---
## ⚠️ 6) XSS Detector
Analisi passiva per Cross-Site Scripting

XSS riflesso

output non sanitizzato

---
## 📱 7) Phone OSINT PRO
Raccoglie informazioni OSINT su numeri telefonici

carrier, reputazione, blacklist

---
## 🧠 8) Fingerprinting ULTRA
Fingerprinting avanzato del target

CMS

framework

server 

librerie JS

---
## 🚀 9) Tutti i moduli
Esegue in sequenza tutti i moduli compatibili

---
## 🧪 10) TEST (debug)
Modulo interno di debug

---
## 🔐 11) SSL Analyzer
Analizza certificati SSL/TLS.  

certificati scaduti, protocolli obsoleti.  

---
## 🏗️ 12) Technology Fingerprinting PRO
Fingerprinting tecnologico avanzato

plugin, versioni, stack server

---
## 🛡️ 13) WAF Detector
Rileva la presenza di Web Application Firewall
 
Cloudflare, Sucuri, Imperva, AWS WAF

---
## 🔀 14) Open Redirect Scanner
Analisi passiva per open redirect

redirect non validati, URL riflessi

---
## 🤖 15) Robots.txt Analyzer
Analizza robots.txt per directory sensibili
  
percorsi nascosti o riservati 

---
## 🌐 16) OSINT Avanzato (email/IP/dominio)
Modulo OSINT multi-target

 WHOIS, DNS, reputazione IP, info email
 
---
## 👤 17) OSINT Social (username)
Ricerca username su piattaforme social
  
profili, correlazioni, footprint pubblico

---
## 📡 18) OSINT IP Avanzato
Analisi approfondita di un indirizzo IP

ASN, geolocazione, reputazione

---
## 🏴‍☠️ 19) OSINT Dominio Avanzato (subdomains)
Enumerazione subdomini e informazioni dominio

subdomini esposti, record DNS

---
## ✉️ 20) OSINT Email Breach Check
Verifica se un’email compare in breach pubblici

compromissioni, leak, data breach

---

🧩 Installazione

git clone https://github.com/hakneo2023/vulnscout

cd vulnscout

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt 

se i requirements non dovessero funzionare, provare con il comando: pip install dnspython python-whois requests phonenumbers beautifulsoup4 colorama

If the requirements don't work, try the command: pip install dnspython python-whois requests phonenumbers beautifulsoup4 colorama

to start the program python3 main.py 

---

										         🧑‍💻 Autore
								      Progetto sviluppato da Dany (hack-neo)

                                       per info: hack.neo.git@gmail.com

<p align="center">
  <img src="assets/assets_2/logo.png" width="150" alt="Hack-NEO Logo">
</p>


														

								      Copyright (c) 2026 Dany (hack-neo)


Il permesso è concesso, gratuitamente, a chiunque ottenga una copia di questo software e dei relativi file di documentazione
(di seguito “Software”), di trattare il Software senza restrizioni, inclusi senza limitazioni i diritti di utilizzare, copiare,
modificare, unire, pubblicare, distribuire, sublicenziare e/o vendere copie del Software, e di permettere alle persone a cui
il Software è fornito di farlo, nel rispetto delle seguenti condizioni:

Il presente avviso di copyright e questa dichiarazione di autorizzazione devono essere inclusi in tutte le copie o parti
sostanziali del Software.

IL SOFTWARE È FORNITO "COSÌ COM'È", SENZA ALCUNA GARANZIA ESPRESSA O IMPLICITA, INCLUSE, A TITOLO ESEMPLIFICATIVO,
LE GARANZIE DI COMMERCIABILITÀ, IDONEITÀ PER UNO SCOPO PARTICOLARE E NON VIOLAZIONE DEI DIRITTI ALTRUI.
IN NESSUN CASO GLI AUTORI O I TITOLARI DEL COPYRIGHT POTRANNO ESSERE RITENUTI RESPONSABILI PER QUALSIASI RECLAMO,
DANNO O ALTRO TIPO DI RESPONSABILITÀ, SIA IN UN'AZIONE CONTRATTUALE, ILLECITA O DI ALTRO TIPO, DERIVANTE DA,
O CONNESSA ALL'USO O ALLA DISTRIBUZIONE DEL SOFTWARE.



Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

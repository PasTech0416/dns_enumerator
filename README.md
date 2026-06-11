cat << 'EOF' > README.md
# DNS Enumeration Engine

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Security Tool](https://img.shields.io/badge/category-cybersecurity-red.svg)]()

Framework modulare e professionale scritto in Python per l'attività di Information Gathering e ricognizione DNS (Active Scouting). Il tool è progettato seguendo i sani principi dell'ingegneria del software, separando la logica di scansione in componenti indipendenti e strutturati.

## 🛠️ Architettura del Progetto

Il software adotta un'architettura modulare ad oggetti (OOP) suddivisa nei seguenti compartimenti logici:

- **`src/main.py`**: Punto di ingresso unico dell'applicazione. Gestisce l'interfaccia a riga di comando (CLI) tramite `argparse` e orchestra la pipeline di scansione.
- **`src/core/resolver.py`**: Modulo specializzato nella risoluzione e nella visualizzazione strutturata dei record DNS principali (A, AAAA, MX, NS, TXT).
- **`src/core/axfr.py`**: Componente deputato alla verifica della vulnerabilità di Zone Transfer (attacco AXFR) interrogando direttamente i Name Server autoritativi identificati.
- **`src/core/bruteforcer.py`**: Motore di enumerazione dei sottodomini tramite attacco a dizionario (brute-force basato su wordlist).
- **`src/utils/logger.py`**: Sistema centralizzato di logging strutturato, responsabile dell'output formattato su standard output con timestamp e livelli di severità.

## 🚀 Requisiti e Installazione

Il tool richiede Python 3.10 o superiore e la libreria `dnspython`.

## Installazione delle dipendenze necessarie
pip install -r requirements.txt

## Esecuzione base (utilizza la wordlist di default subs.txt)
python src/main.py iltuotarget.com

## Esecuzione avanzata con specifica di una wordlist personalizzata
python src/main.py iltuotarget.com -w /percorso/alla/tua/wordlist.txt

# ⚠️ Clausola di Esclusione della Responsabilità (Disclaimer)
Questo strumento è stato sviluppato esclusivamente a scopo didattico e per attività autorizzate di Penetration Testing ed Ethical Hacking. Qualsiasi azione eseguita contro sistemi senza un preventivo consenso scritto è da considerarsi illegale. Lo sviluppatore non si assume alcuna responsabilità per l'uso improprio o per eventuali danni causati dall'utilizzo di questo software.
EOF

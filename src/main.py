import argparse
from utils.logger import ConfiguratoreLogger
from core.resolver import RisolutoreDNS
from core.bruteforcer import EnumeratoreSottodomini
from core.axfr import VerificatoreAXFR

def banner():
    print("""
    ==================================================
    |             DNS ENUMERATION ENGINE             |
    |          Framework di Ricognizione Attiva      |
    ==================================================
    """)

def main():
    banner()
    
    # Configurazione dell'interfaccia a riga di comando
    parser = argparse.ArgumentParser(description="Framework modulare per DNS Enumeration.")
    parser.add_argument("dominio", help="Dominio target da sottoporre ad analisi.")
    parser.add_argument("-w", "--wordlist", default="subs.txt", help="Percorso della wordlist per i sottodomini.")
    args = parser.parse_args()

    # Inizializzazione dei servizi ausiliari
    logger = ConfiguratoreLogger.inizializza_logger()

    # Inizializzazione dei motori core
    motore_risoluzione = RisolutoreDNS(logger)
    motore_axfr = VerificatoreAXFR(logger)
    motore_brute = EnumeratoreSottodomini(logger)

    # Esecuzione della pipeline di scansione
    motore_risoluzione.analizza_dominio(args.dominio)
    motore_axfr.controlla_vulnerabilita(args.dominio)
    motore_brute.esegui_attacco(args.dominio, args.wordlist)

    logger.info("Processo di enumerazione terminato.")

if __name__ == "__main__":
    main()
import dns.resolver

class EnumeratoreSottodomini:
    """
    Esegue l'enumerazione dei sottodomini tramite attacco a dizionario.
    """
    def __init__(self, logger):
        self.logger = logger

    def esegui_attacco(self, dominio: str, percorso_wordlist: str) -> list:
        self.logger.info(f"Inizio brute-force dei sottodomini utilizzando: {percorso_wordlist}")
        sottodomini_trovati = []

        try:
            with open(percorso_wordlist, 'r') as file:
                parole = file.read().splitlines()
        except FileNotFoundError:
            self.logger.critical(f"File wordlist non trovato al percorso: {percorso_wordlist}")
            return sottodomini_trovati

        for parola in parole:
            sottodominio_completo = f"{parola}.{dominio}"
            try:
                risposte = dns.resolver.resolve(sottodominio_completo, 'A')
                ips = [str(ip) for ip in risposte]
                self.logger.info(f"Sottodominio individuato: {sottodominio_completo} -> {ips}")
                sottodomini_trovati.append({"sottodominio": sottodominio_completo, "ips": ips})
            except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
                continue
            except Exception as e:
                self.logger.error(f"Errore durante la risoluzione di {sottodominio_completo}: {str(e)}")

        return sottodomini_trovati
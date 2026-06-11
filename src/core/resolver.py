import dns.resolver

class RisolutoreDNS:
    """
    Gestisce la risoluzione dei record DNS standard per un dominio target.
    """
    def __init__(self, logger):
        self.logger = logger
        self.tipi_record = ['A', 'AAAA', 'MX', 'NS', 'TXT']

    def analizza_dominio(self, dominio: str) -> dict:
        self.logger.info(f"Avvio analisi record strutturati per: {dominio}")
        risultati = {}

        for record in self.tipi_record:
            try:
                risposte = dns.resolver.resolve(dominio, record)
                risultati[record] = [str(rdata) for rdata in risposte]
                
                # Ciclo per mostrare a schermo ogni singolo dato trovato
                for dato in risultati[record]:
                    self.logger.info(f"Record {record} individuato -> {dato}")
                    
            except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
                continue
            except Exception as e:
                self.logger.error(f"Errore durante l'interrogazione del record {record}: {str(e)}")
        
        return risultati

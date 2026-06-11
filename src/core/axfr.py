import dns.resolver
import dns.zone
import dns.query

class VerificatoreAXFR:
    """
    Verifica se i Name Server del target sono vulnerabili al Zone Transfer (AXFR).
    """
    def __init__(self, logger):
        self.logger = logger

    def controlla_vulnerabilita(self, dominio: str) -> bool:
        self.logger.info(f"Verifica vulnerabilità AXFR avviata per: {dominio}")
        
        try:
            ns_risposte = dns.resolver.resolve(dominio, 'NS')
            server_dns = [str(ns.target) for ns in ns_risposte]
        except Exception as e:
            self.logger.error(f"Impossibile recuperare i Name Server per il dominio: {str(e)}")
            return False

        vulnerabile = False
        for ns in server_dns:
            self.logger.info(f"Test di trasferimento di zona verso l'host: {ns}")
            try:
                zona = dns.zone.from_xfr(dns.query.xfr(ns, dominio))
                self.logger.warning(f"FALLA RILEVATA: Zone Transfer consentito dall'host {ns}")
                vulnerabile = True
                for nome, nodo in zona.nodes.items():
                    self.logger.info(f" Record estratto: {nome} {nodo.to_text(name=nome)}")
            except Exception:
                self.logger.info(f"Trasferimento di zona rifiutato dall'host {ns}")
        
        return vulnerabile
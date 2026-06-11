import logging
import sys

class ConfiguratoreLogger:
    """
    Configura il sistema di logging centralizzato per l'applicazione.
    """
    @staticmethod
    def inizializza_logger():
        logger = logging.getLogger("DNSEnumerator")
        logger.setLevel(logging.INFO)

        # Formato professionale per i messaggi nel terminale
        formato = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s', datefmt='%H:%M:%S')

        # Configurazione dell'output su Standard Output
        handler_console = logging.StreamHandler(sys.stdout)
        handler_console.setFormatter(formato)
        logger.addHandler(handler_console)
        
        return logger
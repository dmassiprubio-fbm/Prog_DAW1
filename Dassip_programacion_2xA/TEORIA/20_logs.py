import logging
import time


logging.basicConfig(level=logging.DEBUG,
                    format = "%(asctime)s - %(levelname)s - %(message)s - %(lineno)s")

logging.debug('Missatge de debug') #Nivell més baix de diagnòstic.
logging.info('Missatge de informació') # Nivell d'infomació
logging.warning('Missatge de warning') # Nivell de que hi ha o pot haver un error
logging.error("Missatge d'error") # Hi ha un error dins l'aplicació
logging.critical('Missatge critic') # Error molt greu 


def log_time(function):
    def time_function(*args, **kargs):
        start_time = time.time()
        function(*args, **kargs)
        end_timme = time.time()
        logging.info(f"El temps d'execucio de la funció {function.__name__} es de: {end_timme - start_time}")
        return function
    return time_function 


class PropossalManager:

    
    def __init__(self):
        self.propossals = {}
    
    @log_time
    def add_propossal(self, name):
        if name not in self.propossals:
            self.propossals[name] = 'Pendent'
            logging.info(f"{name} - s'ha afegit correctament al diccionari")
        else:
            logging.warning(f'{name} - Ja esta dins el diccionari')

    @log_time
    def delete_propossal(self, name):
        if name in self.propossals:
            del self.propossals[name]
            logging.info(f"{name} - s'ha eliminat correctament al diccionari")
        else:
            logging.error("l'element no esta dins el diccionari")
    
    @log_time
    def mark_propossal_comlete(self, name):
        if name in self.propossals:
            self.propossals[name] = "Complet"
            logging.info(f"{name} - s'ha marcat correctament")
        else:
            logging.error("l'element no esta dins el diccionari")
        
    @log_time
    def list_propossal(self):
        for p, estat in self.propossals.items():
            print(p, estat)

my_propossal = PropossalManager()
my_propossal.list_propossal()
my_propossal.add_propossal("Prop 1")
my_propossal.add_propossal("Prop 2")
my_propossal.add_propossal("Prop 3")
my_propossal.mark_propossal_comlete("Prop 2")
my_propossal.delete_propossal("Prop 3")
my_propossal.list_propossal()



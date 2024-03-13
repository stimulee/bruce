from config import *
from Robot import *
import logging, logging.config, logging.handlers

logging.log_file = log_file
logging.config.fileConfig(logging_conf)
logger = logging.getLogger('robot')
logger.info('Startup')

def main():
    bras = Bras('Hercule')
    
    # bras.base.droite()
    # bras.base.gauche()

    # bras.epaule.rotation('CW',20)
    # bras.epaule.Stop()
    
    # bras.epaule.monter()
    # bras.epaule.descendre()
    
    # bras.coude.rotation('CW',45)
    # bras.coude.rotation('CC',45)
    
    # bras.coude.plier()
    # bras.coude.deplier()
    
    # bras.poignet.plier()
    # bras.poignet.deplier()

    bras.poignet2.plier()
    bras.poignet2.deplier()

    # bras.pince.ouvrir()
    # bras.pince.fermer()
    
main()
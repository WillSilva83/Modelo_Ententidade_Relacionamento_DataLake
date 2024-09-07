import logging
'''
logger.debug("Mensagem de depuração")
logger.info("Mensagem informativa")
logger.warning("Mensagem de aviso")
logger.error("Mensagem de erro")
logger.critical("Mensagem crítica")
'''


def config_logger(app_name, level=logging.DEBUG):
    logger = logging.getLogger(app_name)
    logger.setLevel(level)

    # Console Manipulation 

    ch = logging.StreamHandler()
    ch.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(ch)
    
    return logger


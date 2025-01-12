import logging
# Configuração básica do logging
logging.basicConfig(level=logging.INFO)
def logger(mensagem, nivel=logging.INFO):
    """_summary_

    Args:
        mensagem (_type_): _description_
        nivel:{    
            logging.NOTSET: azul para NOTSET
            logging.INFO: verde para sucesso
            logging.WARNING: amarelo para alerta
            logging.ERROR: vermelho para erro
        }
    """
    # Configurar um logger
    logger = logging.getLogger(__name__) 
    # Mapear níveis de logging para cores
    cores = {
        logging.NOTSET: '\033[94m',    # azul para NOTSET
        logging.INFO: '\033[92m',    # verde para sucesso
        logging.WARNING: '\033[93m',  # amarelo para alerta
        logging.ERROR: '\033[91m'     # vermelho para erro
    }
    mensagem_formatada = f"{cores.get(nivel, '')}{mensagem}\033[0m"
    # Exibir a mensagem colorida usando print
    print(mensagem_formatada)
    # Registrar a mensagem no log
    # logger.log(nivel, mensagem)

# 
# exibir_e_logar("Operação de Serviço!", nivel=logging.NOTSET)
# exibir_e_logar("Operação bem-sucedida!", nivel=logging.INFO)
# exibir_e_logar("Isso é um alerta.", nivel=logging.WARNING)
# exibir_e_logar("Ocorreu um erro!", nivel=logging.ERROR)

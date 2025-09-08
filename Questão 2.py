from pathlib import Path
from datetime import datetime
import logging
import shutil

# Primeiramente definimos os endereços da pasta que queremos ver e depois da pasta que receberá as cópias.
caminho = Path(r"/home/valcann/backupsFrom")
destino_copias = Path(r"/home/valcann/backupsTo")


# Criamos então dois Loggers que vão atuar em diretórios diferentes monitorando a pasta principal e a que receberá as copias,respectivamente.
logger_listagem = logging.getLogger("listagem")
handler1 = logging.FileHandler(filename=r"/home/valcann/backupsFrom.log")
logger_listagem.addHandler(handler1)
formatter = logging.Formatter("%(message)s")
handler1.setFormatter(formatter)
logger_listagem.setLevel(logging.INFO)


logger_copias = logging.getLogger("copias")
handler2 = logging.FileHandler(filename=r"/home/valcann/backupsTo.log")
logger_copias.addHandler(handler2)
handler2.setFormatter(formatter)
logger_copias.setLevel(logging.INFO)


# Essa é uma função para formatar de forma mais legível o tamanho em bytes que a biblioteca Pathlib nos entrega.
def transformar_byte(tamanho):
    grandeza = len(str(tamanho))
    if grandeza < 4:
        return f"{tamanho} bytes"
    elif 7 > grandeza >= 4:
        return f"{tamanho/1000} KBytes"
    elif 10 > grandeza >= 7:
        return f"{tamanho/1000000} MBytes"
    elif 13 > grandeza >= 10:
        return f"{tamanho/1000000000} GBytes"


# Começamos então a caminhar pelo diretório usando iteração e retirando os dados necessários de cada arquivo.
for item in caminho.iterdir():
    # Retira os dados principais e os printa.
    info = item.stat()
    print(
        f"Nome:{item.name} | Tamanho:{transformar_byte(info.st_size)} | Data de criacao:('{datetime.fromtimestamp(info.st_ctime).strftime('%d/%m/%Y %H:%M:%S')}') | Data de modificacao:{datetime.fromtimestamp(info.st_mtime).strftime('%d/%m/%Y %H:%M:%S'),}"
    )
    # Salva o resultado em backupsFrom.Log
    logger_listagem.info(
        f"Nome:{item.name}  Tamanho:{transformar_byte(info.st_size)}  Data de criacao:('{datetime.fromtimestamp(info.st_ctime).strftime('%d/%m/%Y %H:%M:%S')}')  Data de modificacao:{datetime.fromtimestamp(info.st_mtime).strftime('%d/%m/%Y %H:%M:%S'),}"
    )
    # Calcula o tempo da data de criação
    data_criação_arquivo = datetime.fromtimestamp(info.st_ctime)
    data_atual = datetime.now()
    diferenca_dias = (data_atual - data_criação_arquivo).days

    # Exclui se for maior que 3 dias.
    if diferenca_dias > 3:
        Path.unlink(item)
    # Copia se for menor ou igual.
    else:
        shutil.copy2(item, destino_copias)


# Salva o resultado da cópia em backupsTo.log
for item in destino_copias.iterdir():

    logger_copias.info(
        f"Nome:{item.name}  Tamanho:{transformar_byte(info.st_size)}  Data de criacao:('{datetime.fromtimestamp(info.st_ctime).strftime('%d/%m/%Y %H:%M:%S')}')  Data de modificação:{datetime.fromtimestamp(info.st_mtime).strftime('%d/%m/%Y %H:%M:%S'),}"
    )

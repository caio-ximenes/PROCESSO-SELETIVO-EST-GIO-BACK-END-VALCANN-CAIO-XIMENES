from pathlib import Path
from datetime import datetime
import logging
import shutil  

caminho = Path(r"/home/valcann/backupsFrom")
destino_copias = Path(r'/home/valcann/backupsTo')
logging.basicConfig(level=logging.INFO,
                     filename='/home/valcann/backupsFrom.log', 
                     filemode='w')

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





for item in caminho.iterdir():
     info = item.stat()
     data_criação_arquivo = datetime.fromtimestamp(info.st_ctime)
     data_atual = datetime.now()
     diferenca_dias = (data_atual - data_criação_arquivo).days
     print(type(info.st_size))
     print(f"Nome:{item} | Tamanho:{transformar_byte(info.st_size)} | Data de criação:('{datetime.fromtimestamp(info.st_ctime).strftime('%d/%m/%Y %H:%M:%S')}') | Data de modificação:{datetime.fromtimestamp(info.st_mtime).strftime('%d/%m/%Y %H:%M:%S'),}")
     
     
     logging.info(f"Nome:{item}  Tamanho:{transformar_byte(info.st_size)}  Data de criação:('{datetime.fromtimestamp(info.st_ctime).strftime('%d/%m/%Y %H:%M:%S')}')  Data de modificação:{datetime.fromtimestamp(info.st_mtime).strftime('%d/%m/%Y %H:%M:%S'),}")

     if(diferenca_dias > 3):
           Path.unlink(item)
           
     else:
          shutil.copy2(item, destino_copias)



for item in caminho.iterdir():
      
     logging.info(f"Nome:{item}  Tamanho:{transformar_byte(info.st_size)}  Data de criação:('{datetime.fromtimestamp(info.st_ctime).strftime('%d/%m/%Y %H:%M:%S')}')  Data de modificação:{datetime.fromtimestamp(info.st_mtime).strftime('%d/%m/%Y %H:%M:%S'),}")


           





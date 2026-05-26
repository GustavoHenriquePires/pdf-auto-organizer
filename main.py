import os
import time
import shutil
from datetime import datetime

DOWNLOADS = r"C:\Users\Pichau\Downloads"
BASE_DESTINO = r"D:\robo_download\ADS\automacao\pdfs"

print("Robô organizador por data rodando...")

processados = set(os.listdir(DOWNLOADS))

while True:

    arquivos = set(os.listdir(DOWNLOADS))
    novos = arquivos - processados

    for arquivo in novos:

        if not arquivo.lower().endswith(".pdf"):
            continue

        origem = os.path.join(DOWNLOADS, arquivo)

        # data atual
        data = datetime.now().strftime("%Y-%m-%d")

        pasta_data = os.path.join(BASE_DESTINO, data)
        os.makedirs(pasta_data, exist_ok=True)

        destino = os.path.join(pasta_data, arquivo)

        try:
            time.sleep(2)  # espera download terminar
            shutil.move(origem, destino)
            print(f"Movido: {arquivo} -> {data}")

        except Exception as e:
            print("Erro:", e)

    processados = arquivos
    time.sleep(2)
# getPrices_loop_db.py
# Script para coletar preços de Bitcoin e Commodities e armazenar em um banco de dados
import time
import pandas as pd
from sqlalchemy import create_engine
from getBitcoin import get_bitcoin_df
from getComm import get_comm_df

from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do banco de dados
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

# criar conexão com o banco de dados
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"
engine = create_engine(DATABASE_URL)

# testar a conexão
try:
    with engine.connect() as connection:
        print("Conexão bem sucedida!")
except Exception as e:
    print(f"Falha na conexão: {e}")

SLEEP_SECONDS = 60

if __name__ == "__main__":
    while True:
        # Coletar
        df_btc = get_bitcoin_df()
        df_comm = get_comm_df()
        
        # Concatenar
        df = pd.concat([df_btc, df_comm], ignore_index=True)

        # Inserir no banco de dados
        df.to_sql('bronze_cotacoes', engine, if_exists='append', index=False)

        print("Dados inseridos com sucesso!")

        # Esperar próximo ciclo
        time.sleep(SLEEP_SECONDS)

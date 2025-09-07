# getComm.py
# Script para coletar preços atuais de Commodities e retornar como um DataFrame
import yfinance as yf
import pandas as pd
from datetime import datetime

def get_comm_df():
    symbols = ["GC=F", "CL=F", "SI=F"] # Ouro, Petróleo, Prata
    dfs = []
    for sym in symbols:
        # Pegar o preço mais recente
        ultimo_df = yf.Ticker(sym).history(period="1mo", interval="1d")[['Close']].tail(1)
        # Transformar em DataFrame com as colunas corretas
        ultimo_df = ultimo_df.rename(columns={'Close': 'preco'})
        ultimo_df['ativo'] = sym
        ultimo_df['moeda'] = 'USD'
        ultimo_df['horario_coleta'] = datetime.now()
        dfs.append(ultimo_df)
    # Concatenar todos os DataFrames em um só
    return pd.concat(dfs, ignore_index=True)
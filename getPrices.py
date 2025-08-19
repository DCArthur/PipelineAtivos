import pandas as pd
import time

from getBitcoin import get_bitcoin_df
from getComm import get_comm_df

valor_bitcoin = get_bitcoin_df()
valor_commodities = get_comm_df()

while True:
    df = pd.concat([valor_bitcoin, valor_commodities], ignore_index=True)
    print(df)

    time.sleep(60)  # Espera 60 segundos antes de coletar os dados novamente
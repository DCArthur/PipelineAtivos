import requests
from datetime import datetime
import pandas as pd

def get_bitcoin_df():
    # URL p obter o preco da bitcoin
    url = "https://api.coinbase.com/v2/prices/spot"

    # Requisição GET para API
    response = requests.get(url)
    data = response.json()

    # Extrair os dados importantes
    preco = float(data['data']['amount'])
    ativo = data['data']['base']
    moeda = data['data']['currency']
    horario_coleta = datetime.now()

    df = pd.DataFrame([{
        'ativo': ativo,
        'preco': preco,
        'moeda': moeda,
        'horario_coleta': horario_coleta
    }])

    return df

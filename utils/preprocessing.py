import pandas as pd

def carregar_dados(caminho_csv):
    df = pd.read_csv(caminho_csv)

    return df
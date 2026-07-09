import pandas as pd

def load_dataset(origem):
    try:
        df = pd.read_csv(origem).drop(columns = 'Unnamed: 0')
        print('DF carregado com sucesso')
        return df
    except FileNotFoundError:
        print(f'O arquivo não foi encontrado em {origem}')
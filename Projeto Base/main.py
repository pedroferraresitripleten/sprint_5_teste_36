import json
from utils import load_dataset, agrupa, save, plot_agrupamento

def main ():
    print('Abrindo arquivo config')
    with open('src/config.json', 'r') as configuracao:
        config = json.load(configuracao)
        origem = config['origem']

    print('Carregando dataset')
    df = load_dataset(origem)

    print('Agrupando dados')
    resultado = agrupa(df)

    saida = config['saida']

    print('Salvando resultado')
    save(resultado,saida)

    plot_agrupamento(resultado,'island',saida)
    
if __name__ == "__main__":
    main()
    
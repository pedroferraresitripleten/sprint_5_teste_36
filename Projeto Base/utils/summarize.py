import matplotlib.pyplot as plt

def agrupa(df):
    resultado = df.groupby(['island','species', 'sex'])['body_mass_g'].agg(['mean','std']).reset_index()
    return resultado
    
def plot_agrupamento(resultado,coluna,saida):
    plt.figure(figsize=(10,6))
    plt.bar(data=resultado, x=coluna, height='mean')
    plt.savefig(saida.replace('.csv','.png'))

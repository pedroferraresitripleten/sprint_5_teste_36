def save(resultado,output_path):
    try:
        resultado.to_csv(output_path, index=False)
        print('Análise salva com sucesso.')
    except Exception as e:
        print('não foi possível salvar.')   

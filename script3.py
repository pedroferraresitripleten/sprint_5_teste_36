# ============================================================================
# IMPORTAÇÕES DE BIBLIOTECAS
# ============================================================================

# Importa a biblioteca argparse (padrão do Python)
# Função: Gerenciar argumentos de linha de comando
# Nota: Importada mas NÃO utilizada neste código específico
import argparse  

# Importa a biblioteca os (padrão do Python)
# Função: Interagir com o sistema operacional e variáveis de ambiente
# Nota: Importada mas NÃO utilizada neste código específico
import os  

# Importa a biblioteca json (padrão do Python)
# Função: Ler e escrever dados em formato JSON
# Usado neste código: json.load() para ler arquivo JSON
# json.load() converte JSON em dicionário Python
import json  


# ============================================================================
# DEFINIÇÃO DA FUNÇÃO PRINCIPAL
# ============================================================================

def main():
    """
    Função principal do programa.
    
    Esta função:
    1. Abre e lê um arquivo JSON (config.json)
    2. Converte o JSON em um dicionário Python
    3. Extrai valores específicas do dicionário
    4. Exibe os valores no console
    
    Arquivo esperado (config.json):
        {
            "endpoint": "https://api.exemplo.com",
            "formato": "JSON",
            "timeout": 30,
            "debug": false
        }
    """
    
    # Abre o arquivo 'config.json' no modo de leitura ('r')
    # Função: open(caminho_do_arquivo, modo)
    # 
    # Modos de abertura:
    # - 'r' = Read (leitura) - arquivo deve existir
    # - 'w' = Write (escrita) - cria ou sobrescreve arquivo
    # - 'a' = Append (adicionar) - escreve no final do arquivo
    # - 'x' = eXclusive creation - cria novo arquivo (erro se existir)
    # - 'b' = binary (binário) - para imagens, executáveis, etc.
    #
    # with: Gerenciador de contexto
    # - Garante que o arquivo será FECHADO automaticamente
    # - Mesmo se ocorrer um erro durante a leitura
    # - Liberando recursos do SO
    #
    # as file: Alias para a variável que representa o arquivo aberto
    #
    # Sem 'with' (não recomendado):
    #     file = open('config.json', 'r')
    #     config = json.load(file)
    #     file.close()  # Precisa fechar manualmente (risco de esquecer)
    with open('config.json', 'r') as file:
        # Lê o conteúdo completo do arquivo
        # json.load() converte dados JSON em estrutura Python
        #
        # JSON para Python - Conversão de tipos:
        # JSON String    → Python str      ("valor")
        # JSON Number    → Python int/float (42, 3.14)
        # JSON true      → Python True     (booleano)
        # JSON false     → Python False    (booleano)
        # JSON null      → Python None     (nulo)
        # JSON Array     → Python list     ([1, 2, 3])
        # JSON Object    → Python dict     ({"chave": "valor"})
        #
        # Exemplo de transformação:
        # JSON: {"endpoint": "https://api.com", "timeout": 30}
        # Python: {'endpoint': 'https://api.com', 'timeout': 30}
        config = json.load(file)
        
        # Após sair do bloco 'with', o arquivo é fechado automaticamente
        # Não precisa chamar file.close()
        
    print(config)
    print()
    
    # Obtém o valor da chave 'endpoint' do dicionário config
    # Função: dicionario.get(chave, valor_padrao)
    #
    # Diferença entre .get() e acesso direto:
    # 
    # 1. Usando .get():
    #    endpoint = config.get('endpoint')
    #    Se não existir → retorna None (seguro)
    #
    # 2. Usando acesso direto (NÃO RECOMENDADO):
    #    endpoint = config['endpoint']
    #    Se não existir → lança erro KeyError (pode quebrar o programa)
    #
    # SEMPRE USE .get() para segurança!
    #
    # Com valor padrão (melhor prática):
    #    endpoint = config.get('endpoint', 'http://localhost:8000')
    #    Se não existir → retorna valor padrão
    # endpoint = config.get('endpoint')
    endpoint = config.get('origem')
    
    # Obtém o valor da chave 'formato' do dicionário config
    # Se não existir, retorna None
    # Melhor fazer: config.get('formato', 'JSON')
    # config.get(chave, Valor-Padrão)
    formato = config.get('formato', 'JSON')
    
    # Exibe no console os valores extraídos
    # f'...' = f-string (formatted string)
    # {endpoint} = insere o valor de endpoint
    # {formato} = insere o valor de formato
    #
    # Saída esperada:
    # endpoint: https://api.exemplo.com; formato: JSON
    print(f'endpoint: {endpoint}; formato: {formato}')


# ============================================================================
# EXECUÇÃO DO PROGRAMA
# ============================================================================

# Verifica se o script está sendo executado diretamente
# __name__ = variável especial do Python
# __main__ = valor quando script é executado diretamente
if __name__ == "__main__":
    # Chama a função main()
    main()


# ============================================================================
# VERSÃO MELHORADA (COM TRATAMENTO DE ERROS)
# ============================================================================

"""
Código alternativo mais robusto (descomentar para usar):

import json
import os

def main_melhorada():
    '''
    Versão melhorada com tratamento de erros.
    '''
    
    # Define o caminho do arquivo de configuração
    config_file = 'config.json'
    
    # Valida se o arquivo existe antes de tentar abrir
    if not os.path.exists(config_file):
        print(f'ERRO: Arquivo {config_file} não encontrado!')
        return
    
    try:
        # Tenta abrir e ler o arquivo
        with open(config_file, 'r', encoding='utf-8') as file:
            # encoding='utf-8' garante compatibilidade com caracteres especiais
            config = json.load(file)
    
    except json.JSONDecodeError as e:
        # Erro quando JSON está malformado (sintaxe inválida)
        print(f'ERRO: Arquivo JSON inválido! {e}')
        return
    
    except IOError as e:
        # Erro ao ler o arquivo (permissões, disco cheio, etc.)
        print(f'ERRO: Não foi possível ler o arquivo! {e}')
        return
    
    # Extrai valores com padrões (mais seguro)
    endpoint = config.get('endpoint', 'http://localhost:8000')
    formato = config.get('formato', 'JSON')
    timeout = config.get('timeout', 30)
    debug = config.get('debug', False)
    
    # Valida os tipos de dados
    if not isinstance(endpoint, str):
        print('ERRO: endpoint deve ser uma string!')
        return
    
    if not isinstance(timeout, int):
        print('ERRO: timeout deve ser um número inteiro!')
        return
    
    # Se passou em todas as validações, usa os valores
    print(f'Configuração carregada com sucesso!')
    print(f'Endpoint: {endpoint}')
    print(f'Formato: {formato}')
    print(f'Timeout: {timeout}s')
    print(f'Debug: {debug}')
    
    return config  # Retorna o dicionário para uso posterior


if __name__ == "__main__":
    # Descomente para usar a versão melhorada:
    # config = main_melhorada()
    
    # Use a versão simples:
    # main()
"""


# ============================================================================
# EXEMPLOS DE ARQUIVO config.json
# ============================================================================

"""
EXEMPLO 1 - Configuração básica:

{
    "endpoint": "https://api.exemplo.com",
    "formato": "JSON",
    "timeout": 30,
    "debug": false
}


EXEMPLO 2 - Configuração com mais detalhes:

{
    "api": {
        "endpoint": "https://api.exemplo.com",
        "version": "v1",
        "timeout": 30
    },
    "database": {
        "host": "localhost",
        "port": 5432,
        "nome": "meu_banco"
    },
    "logging": {
        "nivel": "INFO",
        "arquivo": "app.log"
    }
}


EXEMPLO 3 - Configuração com listas (arrays):

{
    "endpoints": [
        "https://api1.exemplo.com",
        "https://api2.exemplo.com",
        "https://api3.exemplo.com"
    ],
    "formatos_suportados": ["JSON", "XML", "CSV"],
    "portas": [8000, 8001, 8002]
}
"""


# ============================================================================
# COMO TRABALHAR COM JSON EM PYTHON
# ============================================================================

"""
LEITURA DE JSON:

1. De um arquivo:
    with open('arquivo.json', 'r') as file:
        dados = json.load(file)  # Retorna dict/list

2. De uma string:
    json_string = '{"chave": "valor"}'
    dados = json.loads(json_string)  # Retorna dict/list


ESCRITA DE JSON:

1. Para um arquivo:
    dados = {"chave": "valor", "numero": 42}
    with open('saida.json', 'w') as file:
        json.dump(dados, file, indent=4)  # indent para formatação

2. Para uma string:
    json_string = json.dumps(dados, indent=4)  # Retorna string


DIFERENÇAS:
- json.load()  → Ler de ARQUIVO
- json.loads() → Ler de STRING
- json.dump()  → Escrever em ARQUIVO
- json.dumps() → Escrever em STRING
"""


# ============================================================================
# ACESSANDO DADOS ANINHADOS
# ============================================================================

"""
Se o JSON tem estrutura aninhada:

{
    "api": {
        "endpoint": "https://api.com",
        "timeout": 30
    },
    "database": {
        "host": "localhost"
    }
}

Formas de acessar:

1. Encadeado (risco de erro):
    endpoint = config['api']['endpoint']  # KeyError se 'api' não existir!

2. Usando .get() (RECOMENDADO):
    endpoint = config.get('api', {}).get('endpoint', 'padrão')
    
3. Usando função auxiliar (mais limpo):
    def get_nested(dict_obj, keys, default=None):
        '''Acessa valores aninhados com segurança'''
        for key in keys:
            if isinstance(dict_obj, dict):
                dict_obj = dict_obj.get(key)
            else:
                return default
        return dict_obj if dict_obj is not None else default
    
    endpoint = get_nested(config, ['api', 'endpoint'], 'padrão')
"""


# ============================================================================
# EXEMPLO PRÁTICO COMPLETO
# ============================================================================

"""
Código prático para usar em projeto real:

import json
from pathlib import Path

class ConfigLoader:
    '''Carregador de configurações JSON com validação'''
    
    def __init__(self, config_file='config.json'):
        self.config_file = Path(config_file)
        self.config = None
    
    def carregar(self):
        '''Carrega o arquivo de configuração'''
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
                return True
        except FileNotFoundError:
            print(f'Erro: {self.config_file} não encontrado')
            return False
        except json.JSONDecodeError:
            print(f'Erro: {self.config_file} contém JSON inválido')
            return False
    
    def obter(self, chave, padrao=None):
        '''Obtém um valor da configuração com segurança'''
        if self.config is None:
            return padrao
        return self.config.get(chave, padrao)
    
    def obter_aninhado(self, caminho, padrao=None):
        '''Obtém um valor aninhado ex: 'api.endpoint' '''
        valor = self.config
        for chave in caminho.split('.'):
            if isinstance(valor, dict):
                valor = valor.get(chave)
            else:
                return padrao
        return valor if valor is not None else padrao


# Uso:
loader = ConfigLoader('config.json')
if loader.carregar():
    endpoint = loader.obter('endpoint', 'padrão')
    api_timeout = loader.obter_aninhado('api.timeout', 30)
"""
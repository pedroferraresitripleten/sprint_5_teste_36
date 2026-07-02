# ============================================================================
# IMPORTAÇÕES DE BIBLIOTECAS
# ============================================================================

# Importa a biblioteca argparse (padrão do Python)
# Função: Gerenciar argumentos de linha de comando
# Nota: Importada mas NÃO utilizada neste código específico
import argparse  

# Importa a biblioteca os (padrão do Python)
# Função: Interagir com o sistema operacional
# Usos neste código: Acessar variáveis de ambiente via os.getenv()
# Usos comuns: Criar pastas, ler variáveis de ambiente, executar comandos do SO
import os  

# Importa a biblioteca json (padrão do Python)
# Função: Trabalhar com dados em formato JSON
# Nota: Importada mas NÃO utilizada neste código específico
import json  


from dotenv import load_dotenv


# ============================================================================
# DEFINIÇÃO DA FUNÇÃO PRINCIPAL
# ============================================================================
def main():
    """
    Função principal do programa.
    
    Esta função:
    1. Obtém o valor de uma variável de ambiente chamada "API_TOKEN"
    2. Armazena o valor em uma variável local
    3. Exibe o valor no console
    
    O que são variáveis de ambiente?
    - São variáveis definidas no sistema operacional
    - Podem ser acessadas por qualquer programa
    - Úteis para guardar senhas, tokens, configurações sem expor no código
    
    Como definir uma variável de ambiente?
    
    LINUX/MAC (Terminal):
        export API_TOKEN="sua_chave_aqui"
    
    WINDOWS (PowerShell):
        $env:API_TOKEN="sua_chave_aqui"
    
    WINDOWS (CMD):
        set API_TOKEN=sua_chave_aqui
    
    ARQUIVO .env (melhor prática):
        Criar arquivo .env na raiz do projeto com:
        API_TOKEN=sua_chave_aqui
        Depois usar biblioteca python-dotenv para carregar
    """
    load_dotenv()
    
    # Obtém o valor da variável de ambiente chamada "API_TOKEN"
    # Função: os.getenv(chave, padrão)
    #
    # Parâmetros:
    # - 'API_TOKEN': Nome da variável de ambiente a procurar
    # - Sem segundo parâmetro: retorna None se não encontrar
    #
    # Comportamento:
    # Se API_TOKEN está definida → retorna o valor (string)
    # Se API_TOKEN NÃO está definida → retorna None
    #
    # Exemplos:
    # Variável definida:    API_TOKEN = "abc123xyz" → api_token = "abc123xyz"
    # Variável não definida:                        → api_token = None
    api_token = os.getenv('API_TOKEN_2')
    
    
    # Exibe no console o valor encontrado da variável de ambiente
    # f'...' = f-string (formatted string)
    # {api_token} = insere o valor da variável na string
    #
    # Saída possível:
    # 1. Se API_TOKEN foi definida: Token da API: abc123xyz
    # 2. Se API_TOKEN NÃO foi definida: Token da API: None
    #
    # Problema: Exibir None no console pode não ser ideal
    # Solução melhor (comentada abaixo):
    # if api_token:
    #     print(f'Token da API: {api_token}')
    # else:
    #     print('ERRO: Variável de ambiente API_TOKEN não foi definida!')
    print(f'Token da API: {api_token}')


# ============================================================================
# EXECUÇÃO DO PROGRAMA
# ============================================================================

# Verifica se o script está sendo executado diretamente (não importado)
# __name__ = variável especial do Python
# __main__ = valor quando script é executado diretamente
#
# Exemplos:
# 1. python script.py
#    → __name__ == "__main__" (VERDADEIRO, executa main())
#
# 2. Outro script faz: import script
#    → __name__ == "script" (FALSO, não executa main())
if __name__ == "__main__":
    # Chama a função main() para iniciar o programa
    main()


# ============================================================================
# VERSÃO MELHORADA (COM TRATAMENTO DE ERRO)
# ============================================================================

"""
Código alternativo mais robusto (descomentar para usar):

def main_melhorada():
    # Obtém o valor da variável de ambiente
    api_token = os.getenv('API_TOKEN')
    
    # Valida se a variável foi encontrada
    if api_token is None:
        # Se não encontrar, exibe mensagem de erro
        print('ERRO: Variável de ambiente API_TOKEN não foi definida!')
        print('Defina com: export API_TOKEN="seu_token_aqui"')
        return  # Encerra a função
    
    # Se chegou aqui, tem um token válido
    if api_token == '':
        # Verifica se está vazia (definida mas sem valor)
        print('ERRO: API_TOKEN está definida mas vazia!')
        return
    
    # Valida o comprimento do token (exemplo: mínimo 10 caracteres)
    if len(api_token) < 10:
        print('AVISO: Token parece muito curto, verifique!')
    
    # Se passou todas as validações, usa o token
    print(f'Token da API carregado com sucesso!')
    print(f'Token (primeiros 5 caracteres): {api_token[:5]}...')
    
    # Aqui você poderia usar o token em uma requisição HTTP, por exemplo
    # response = requests.get('https://api.exemplo.com/dados', 
    #                        headers={'Authorization': f'Bearer {api_token}'})


if __name__ == "__main__":
    # Descomente para usar a versão melhorada:
    # main_melhorada()
    
    # Use a versão simples:
    main()
"""


# ============================================================================
# EXEMPLOS DE USO NO TERMINAL
# ============================================================================

"""
EXEMPLO 1 - Executar SEM definir a variável (retorna None):
    $ python script.py
    Token da API: None


EXEMPLO 2 - Definir a variável e depois executar (Linux/Mac):
    $ export API_TOKEN="abc123xyz"
    $ python script.py
    Token da API: abc123xyz


EXEMPLO 3 - Definir e executar na mesma linha (Linux/Mac):
    $ API_TOKEN="seu_token_aqui" python script.py
    Token da API: seu_token_aqui


EXEMPLO 4 - Windows PowerShell:
    PS> $env:API_TOKEN="abc123xyz"
    PS> python script.py
    Token da API: abc123xyz


EXEMPLO 5 - Windows CMD:
    C:\\> set API_TOKEN=abc123xyz
    C:\\> python script.py
    Token da API: abc123xyz


USANDO ARQUIVO .env (RECOMENDADO):
    1. Instalar biblioteca: pip install python-dotenv
    2. Criar arquivo .env na raiz do projeto:
        API_TOKEN=seu_token_aqui
        DATABASE_URL=postgresql://user:pass@localhost/db
    3. Carregar no código:
        from dotenv import load_dotenv
        load_dotenv()
        api_token = os.getenv('API_TOKEN')
"""


# ============================================================================
# COMPARAÇÃO: os.getenv() vs os.environ[]
# ============================================================================

"""
os.getenv('API_TOKEN') vs os.environ['API_TOKEN']

1. os.getenv('API_TOKEN'):
   - Retorna None se a variável não existir
   - Seguro para usar
   - Permite um valor padrão: os.getenv('API_TOKEN', 'valor_padrao')
   
2. os.environ['API_TOKEN']:
   - Lança erro KeyError se não existir
   - Menos seguro (pode causar crash)
   - Usa sintaxe de dicionário

RECOMENDAÇÃO: Use os.getenv() sempre!

Exemplos com padrão:
    api_token = os.getenv('API_TOKEN', 'token_padrao')
    debug_mode = os.getenv('DEBUG', 'False')
    max_connections = os.getenv('MAX_CONN', '100')
"""
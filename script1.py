# ============================================================================
# IMPORTAÇÕES DE BIBLIOTECAS
# ============================================================================

# Importa a biblioteca argparse (padrão do Python)
# Função: Facilita a criação e gerenciamento de argumentos passados via terminal
# Exemplo: python script.py --fonte "http://exemplo.com"
import argparse  

# Importa a biblioteca os (padrão do Python)
# Função: Permite interagir com o sistema operacional
# Usos comuns: criar pastas, deletar arquivos, obter variáveis de ambiente, etc.
# Nota: Importada mas não utilizada neste código específico
import os  

# Importa a biblioteca json (padrão do Python)
# Função: Trabalhar com dados em formato JSON (ler, escrever, converter, etc.)
# Nota: Importada mas não utilizada neste código específico
import json  


# ============================================================================
# DEFINIÇÃO DA FUNÇÃO PRINCIPAL
# ============================================================================

def main():
    """
    Função principal do programa.
    
    Esta função:
    1. Cria um parser de argumentos
    2. Define quais argumentos são aceitos
    3. Interpreta os argumentos fornecidos pelo usuário
    4. Exibe os resultados no console
    
    Para executar com argumento:
        python script.py --fonte "http://api.exemplo.com"
    
    Para executar sem argumento (usa padrão):
        python script.py
    """
    
    # Cria um objeto ArgumentParser
    # Função: Gerenciar e validar argumentos de linha de comando
    # description: Texto que aparece quando o usuário digita: python script.py --help
    parser = argparse.ArgumentParser(
        description='Processa os dados de uma fonte específica'
    )
    
    # Define um argumento opcional chamado --fonte
    # Parâmetros explicados:
    # 
    # - '--fonte': Nome do argumento (começa com -- porque é opcional)
    #   Uso: python script.py --fonte "valor"
    #
    # - type=str: Define o tipo de dado esperado (string de texto)
    #   Se o usuário passar um número, será convertido para string
    #
    # - default='local': Valor padrão se o usuário não fornecer nada
    #   Se rodar python script.py sem --fonte, usa 'local'
    #
    # - help='...': Mensagem de ajuda exibida com --help
    #   Aparece quando o usuário digita: python script.py --help
    parser.add_argument(
        '--fonte',
        type=str,
        default='local',
        help='Endereço de uma fonte de dados (ex: local, http://api.exemplo.com)'
    )
    
    # Interpreta/Analisa os argumentos fornecidos pelo usuário
    # Função: Valida os argumentos e os armazena em um objeto
    # Resultado: Um objeto com atributos para cada argumento definido
    # 
    # Exemplos de uso:
    # 1. python script.py --fonte "http://api.com"
    #    → args.fonte = "http://api.com"
    #
    # 2. python script.py
    #    → args.fonte = "local" (valor padrão)
    args = parser.parse_args()
    
    # Exibe no console o valor da fonte de dados
    # f'...' = f-string (formatted string) - permite inserir variáveis com {chaves}
    # args.fonte = acessa o valor do argumento --fonte
    #
    # Saída esperada:
    # Se passou --fonte "http://api.com":
    #   Fonte de dados: namespace(fonte='http://api.com')
    #
    # Se não passou nada (usa padrão):
    #   Fonte de dados: namespace(fonte='local')
    # print(f'Fonte de dados: {args}')
    
    # Nota: Para acessar apenas o valor da fonte, poderia ser:
    print(f'Fonte de dados: {args.fonte}')


# ============================================================================
# EXECUÇÃO DO PROGRAMA
# ============================================================================

# Verifica se o script está sendo executado diretamente (não importado como módulo)
# __name__ = variável especial do Python
# __main__ = valor quando o script é executado diretamente
#
# Exemplo de como funciona:
# 1. python script.py
#    → __name__ == "__main__" (VERDADEIRO, executa main())
#
# 2. Outro script faz: import script
#    → __name__ == "script" (FALSO, não executa main())
#
# Por que usar isso?
# - Permite reutilizar funções em outros scripts sem executar main()
# - Deixa o código mais profissional e modular
if __name__ == "__main__":
    
    # Chama a função main() para iniciar o programa
    main()
    
    print(f'Arquivo executado até o fim')


# ============================================================================
# EXEMPLOS DE USO NO TERMINAL
# ============================================================================

"""
EXEMPLO 1 - Usar o valor padrão:
    $ python script.py
    Saída: Fonte de dados: namespace(fonte='local')

EXEMPLO 2 - Passar um argumento customizado:
    $ python script.py --fonte "http://api.exemplo.com"
    Saída: Fonte de dados: namespace(fonte='http://api.exemplo.com')

EXEMPLO 3 - Ver a mensagem de ajuda:
    $ python script.py --help
    Saída:
        usage: script.py [-h] [--fonte FONTE]
        
        Processa os dados de uma fonte específica
        
        optional arguments:
          -h, --help            show this help message and exit
          --fonte FONTE         Endereço de uma fonte de dados (ex: local, http://api.exemplo.com)

EXEMPLO 4 - Passar argumento errado (argparse trata automaticamente):
    $ python script.py --origem "valor"
    Saída: error: unrecognized arguments: --origem valor
"""
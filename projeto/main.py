# O que é um script?
# Um script é um arquivo Python que executa um programa ou tarefa.
# Diferente de um módulo, é feito para ser executado, não importado.
#
# Como executar?
# python main.py
#
# O que este script faz?
# 1. Importa funções do módulo calculadora.py
# 2. Usa essas funções para fazer cálculos
# 3. Exibe os resultados no console
# ============================================================================


# ============================================================================
# IMPORTAÇÕES
# ============================================================================

# Importa funções específicas do módulo calculadora
# Sintaxe: from nome_modulo import funcao1, funcao2
#
# O que isso significa?
# - 'from calculadora': Procura o módulo calculadora.py
# - 'import soma, divisao': Traz as funções soma e divisao para este script
# - Depois disso, podemos usar soma() e divisao() diretamente
#
# Alternativas:
# 1. from calculadora import *  (importa tudo)
# 2. import calculadora (importa o módulo inteiro)
#    Uso: calculadora.soma(10, 5)
from calculadora import soma, divisao, multiplicacao


# ============================================================================
# BLOCO PRINCIPAL DO PROGRAMA
# ============================================================================

if __name__ == '__main__':
    # Exibe uma mensagem informativa no console
    # print(): função que exibe texto na tela
    print("Usando funções do módulo calculadora:")

    # Chama a função soma() do módulo calculadora
    # soma(10, 5) realiza: 10 + 5 = 15
    # print() exibe o resultado
    # Saída: Soma: 15
    print("Soma:", soma(10, 5))

    # Chama a função multiplicação() do módulo calculadora
    # multiplicação(10, 2) realiza: 10 * 2 = 20
    # print() exibe o resultado
    # Saída: Multiplicação: 20
    print("Multiplicação:", multiplicacao(10, 2))


# ============================================================================
# COMO FUNCIONA A IMPORTAÇÃO?
# ============================================================================

"""
PASSO A PASSO:

1. Python procura pelo arquivo 'calculadora.py'
   - Procura na mesma pasta do main.py
   - Procura nas pastas definidas em sys.path

2. Se encontrar, carrega o módulo
   - Executa todo o código do módulo (definições de funções)
   - Não executa nada fora de funções

3. Importa as funções especificadas
   - 'soma' fica disponível como soma()
   - 'divisao' fica disponível como divisao()

4. Agora podemos usar essas funções no nosso script
   - soma(10, 5) funciona
   - divisao(10, 2) funciona

ESTRUTURA DO PROJETO:
projeto/
├── calculadora.py    ← Define as funções
└── main.py          ← Importa e usa as funções
"""


# ============================================================================
# EXEMPLOS DE USO COM DIFERENTES IMPORTAÇÕES
# ============================================================================

"""
EXEMPLO 1 - Importação atual (recomendada para poucos imports):
    from calculadora import soma, divisao
    
    resultado1 = soma(10, 5)
    resultado2 = divisao(10, 2)


EXEMPLO 2 - Importar todo o módulo:
    import calculadora
    
    # Agora precisa usar o prefixo calculadora.
    resultado1 = calculadora.soma(10, 5)
    resultado2 = calculadora.divisao(10, 2)
    resultado3 = calculadora.subtracao(10, 5)


EXEMPLO 3 - Importar tudo:
    from calculadora import *
    
    # Pode usar diretamente
    resultado1 = soma(10, 5)
    resultado2 = divisao(10, 2)
    resultado3 = subtracao(10, 5)
    resultado4 = multiplicacao(10, 5)


EXEMPLO 4 - Importar com alias (apelido):
    from calculadora import soma as add, divisao as div
    
    resultado1 = add(10, 5)      # Usa o apelido 'add'
    resultado2 = div(10, 2)      # Usa o apelido 'div'
"""


# ============================================================================
# TRATAMENTO DE ERRO RECOMENDADO
# ============================================================================

"""
Código melhorado com tratamento de erro (descomentar para usar):

from calculadora import soma, divisao

print("Usando funções do módulo calculadora:")

# Soma funciona normalmente (sem riscos)
print("Soma:", soma(10, 5))

# Divisão pode gerar erro se divisor for zero
# Por isso, usamos try-except
try:
    print("Divisão:", divisao(10, 2))
except ValueError as e:
    # Se ocorrer erro, exibe a mensagem
    print(f"ERRO na divisão: {e}")

# Exemplo que gera erro:
try:
    print("Divisão por zero:", divisao(10, 0))
except ValueError as e:
    print(f"ERRO na divisão: {e}")  # Exibe: ERRO na divisão: Não é possível dividir por zero.
"""
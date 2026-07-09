# O que é um módulo?
# Um módulo é um arquivo .py que contém funções, classes ou variáveis
# que podem ser importadas e utilizadas em outros scripts Python.
#
# Benefícios:
# - Reutilização de código
# - Organização e estrutura
# - Facilita manutenção e colaboração
# - Evita repetição de código
#
# Como usar este módulo?
# from calculadora import soma, divisao
# resultado = soma(10, 5)
# ============================================================================


# ============================================================================
# FUNÇÃO 1: SOMA
# ============================================================================

def soma(a, b):
    """
    Realiza a soma de dois números.
    
    Parâmetros:
        a (int/float): Primeiro número
        b (int/float): Segundo número
    
    Retorno:
        int/float: A soma de a + b
    
    Exemplo:
        >>> soma(10, 5)
        15
        >>> soma(3.5, 2.5)
        6.0
    """
    # Retorna a soma dos dois parâmetros
    return a + b


# ============================================================================
# FUNÇÃO 2: SUBTRAÇÃO
# ============================================================================

def subtracao(a, b):
    """
    Realiza a subtração de dois números.
    
    Parâmetros:
        a (int/float): Minuendo (número maior)
        b (int/float): Subtraendo (número menor)
    
    Retorno:
        int/float: O resultado de a - b
    
    Exemplo:
        >>> subtracao(10, 5)
        5
        >>> subtracao(3.5, 1.5)
        2.0
    """
    # Retorna a subtração de b de a
    return a - b


# ============================================================================
# FUNÇÃO 3: MULTIPLICAÇÃO
# ============================================================================

def multiplicacao(a, b):
    """
    Realiza a multiplicação de dois números.
    
    Parâmetros:
        a (int/float): Primeiro fator
        b (int/float): Segundo fator
    
    Retorno:
        int/float: O resultado de a * b
    
    Exemplo:
        >>> multiplicacao(10, 5)
        50
        >>> multiplicacao(3.5, 2)
        7.0
    """
    # Retorna a multiplicação dos dois parâmetros
    return a * b


# ============================================================================
# FUNÇÃO 4: DIVISÃO (COM VALIDAÇÃO)
# ============================================================================

def divisao(a, b):
    """
    Realiza a divisão de dois números com tratamento de erro.
    
    Parâmetros:
        a (int/float): Dividendo (numerador)
        b (int/float): Divisor (denominador)
    
    Retorno:
        float: O resultado de a / b
    
    Lança:
        ValueError: Se b (divisor) for zero
    
    Exemplo:
        >>> divisao(10, 5)
        2.0
        >>> divisao(15, 3)
        5.0
        >>> divisao(10, 0)
        ValueError: Não é possível dividir por zero.
    """
    
    # Valida se o divisor é zero
    # Não é permitido dividir por zero em matemática
    if b == 0:
        # Lança uma exceção customizada com mensagem de erro
        # raise: força o programa a gerar um erro
        # ValueError: tipo de erro usado para valores inválidos
        raise ValueError("Não é possível dividir por zero.")
    
    # Se chegou aqui, o divisor é válido (diferente de zero)
    # Retorna o resultado da divisão
    return a / b

print('Arquivo Calculadora foi aberto')

if __name__ == "__main__":
    print("Arquivo Calculadora executado pelo Python")


# ============================================================================
# COMO UTILIZAR ESTE MÓDULO
# ============================================================================

"""
EXEMPLO 1 - Importar e usar funções específicas:
    from calculadora import soma, divisao
    
    resultado1 = soma(10, 5)           # resultado1 = 15
    resultado2 = divisao(20, 4)        # resultado2 = 5.0

EXEMPLO 2 - Importar todas as funções:
    from calculadora import *
    
    resultado1 = soma(10, 5)
    resultado2 = subtracao(10, 5)
    resultado3 = multiplicacao(10, 5)
    resultado4 = divisao(10, 5)

EXEMPLO 3 - Importar todo o módulo:
    import calculadora
    
    resultado1 = calculadora.soma(10, 5)
    resultado2 = calculadora.divisao(10, 2)

EXEMPLO 4 - Com tratamento de erro:
    from calculadora import divisao
    
    try:
        resultado = divisao(10, 0)  # Vai gerar erro
    except ValueError as e:
        print(f"Erro: {e}")  # Exibe: Erro: Não é possível dividir por zero.
"""
# Definição da função que realiza uma divisão entre dois números
def calcular_divisao(x, y):
    """
    Função que calcula a divisão de x por y com tratamento de erros.
    
    Args:
        x: Número inteiro ou float (dividendo)
        y: Número inteiro ou float (divisor)
    
    Returns:
        float: Resultado da divisão de x por y
    """
    
    # Bloco try: tenta executar o código que pode gerar um erro
    try:
        resultado = x / y  # Realiza a operação de divisão
        
        # # Usar somente se o bloco `else` estiver comentado
        # return resultado
    
    # Bloco except: captura exceções específicas (neste caso, divisão por zero)
    except ZeroDivisionError:
        # Exibe mensagem de erro quando o divisor é zero
        print("Erro: Tentativa de divisão por zero.")
        return 0
        
    except TypeError:
        # Exibe mensagem de erro quando o divisor é zero
        print("Erro: Tentativa de divisão por string.")
    # except:
    #     print("Erro:")
    
    # Bloco else: executa apenas se NÃO houver exceção no try
    else:
        # Mensagem de sucesso quando a divisão é realizada corretamente
        print("A divisão foi realizada com sucesso.")
        # Retorna o resultado da divisão
        return resultado
    
    # Bloco finally: sempre executa, independente de erro ou não
    finally:
        # Mensagem informativa que sempre aparece ao final da execução
        print("Execução do bloco finally: Finalizando cálculo.")
    
    
    # # Bloco Sem Try-except
    # return x / y


# ============================================================================
# CHAMADAS DA FUNÇÃO (TESTES)
# ============================================================================

# Primeira chamada: tenta dividir 10 por 0 (vai gerar erro ZeroDivisionError)
print(calcular_divisao(10, 0))
print()

# Comentário: Explicação de tentativa de divisão incorreta
# Esta chamada gera um erro porque não é possível dividir por zero

# Segunda chamada: divide 10 por 2 corretamente (resultado = 5.0)
print(calcular_divisao(10, 2))
print()

# Comentário: Esta chamada executa com sucesso pois o divisor é diferente de zero


# Terceira chamada: tenta dividir 10 por 'a' (vai gerar erro TypeError)
print(calcular_divisao(10, 'a'))
print()
# ============================================================================
# DEFINIÇÃO DE EXCEÇÃO CUSTOMIZADA
# ============================================================================

# Criação de uma classe de exceção personalizada que herda de Exception
# Esta exceção será lançada quando não houver saldo suficiente
class SaldoInsuficienteException(Exception):
    """
    Exceção customizada para quando há tentativa de retirada maior que o saldo.
    """
    
    def __init__(self, saldo, valor):
        """
        Inicializa a exceção com informações do saldo e valor tentado.
        
        Args:
            saldo: Valor atual da conta
            valor: Valor que se tentou retirar
        """
        # Armazena o saldo disponível
        self.saldo = saldo
        # Armazena o valor que foi tentado retirar
        self.valor = valor
        # Cria uma mensagem descritiva usando f-string
        mensagem = f"Saldo insuficiente! Saldo disponível: R${saldo}, Valor solicitado: R${valor}"
        # Chama o construtor da classe Exception com a mensagem
        super().__init__(mensagem)


# ============================================================================
# DEFINIÇÃO DA FUNÇÃO
# ============================================================================

def retirar_saldo(saldo, valor):
    """
    Função que realiza a retirada de um valor da conta bancária.
    Lança uma exceção se o valor for maior que o saldo disponível.
    
    Args:
        saldo: float - Saldo atual da conta
        valor: float - Valor a ser retirado
    
    Returns:
        float: Novo saldo após a retirada
    
    Raises:
        SaldoInsuficienteException: Se o valor > saldo
    """
    
    # Verifica se o valor solicitado é maior que o saldo disponível
    if valor > saldo:
        # Lança a exceção customizada com informações do erro
        # O "raise" interrompe a execução e passa a exceção para ser tratada
        raise SaldoInsuficienteException(saldo, valor)
    
    # Se chegou aqui, o saldo é suficiente
    # Usa operador -= para decrementar (subtrai e atribui) o valor do saldo
    saldo -= valor  # Equivalente a: saldo = saldo - valor
    
    # Retorna o novo saldo após a retirada
    return saldo


# ============================================================================
# BLOCO DE EXECUÇÃO COM TRATAMENTO DE EXCEÇÕES
# ============================================================================

# Bloco try: tenta executar o código que pode gerar exceção
try:
    # Chamada da função tentando retirar R$150 com saldo de apenas R$100
    # Isto causará o lançamento de SaldoInsuficienteException
    saldo_atual = retirar_saldo(100, 150)

# Bloco except: captura a exceção customizada quando ela é lançada
# "as e" armazena a exceção em uma variável para acessar seus detalhes
except SaldoInsuficienteException as e:
    # Imprime a mensagem de erro armazenada na exceção
    # Isto exibirá: "Saldo insuficiente! Saldo disponível: R$100, Valor solicitado: R$150"
    print(e)


# ============================================================================
# EXEMPLO ADICIONAL DE USO CORRETO
# ============================================================================

# Descomente as linhas abaixo para ver um exemplo que funciona:
# try:
#     saldo_atual = retirar_saldo(100, 50)  # Retirada válida (50 < 100)
#     print(f"Retirada realizada com sucesso! Novo saldo: R${saldo_atual}")
# except SaldoInsuficienteException as e:
#     print(e)
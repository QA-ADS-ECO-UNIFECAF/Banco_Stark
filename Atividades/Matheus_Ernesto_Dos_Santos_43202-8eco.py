# =========================================
# APP: Banco do Stark (simples)
# =========================================

class Conta:
    def __init__(self, titular: str):
        self.titular = titular
        self.saldo = 0.0
        self.extrato = []


class BancoDoStark:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, titular: str):
        if titular in self.contas:
            print('ERRO - Conta já existe:', titular)
            return
        self.contas[titular] = Conta(titular)
        print('OK - Conta criada para:', titular)

    def depositar(self, titular: str, valor: float):
        if titular not in self.contas:
            print('ERRO - Conta não encontrada:', titular)
            return
        # Observação: validações intencionalmente simples (para QA encontrar problemas)
        self.contas[titular].saldo += valor
        self.contas[titular].extrato.append(('deposito', valor))
        print('OK - Depósito realizado:', valor)

    def sacar(self, titular: str, valor: float):
        if titular not in self.contas:
            print('ERRO - Conta não encontrada:', titular)
            return
        if self.contas[titular].saldo < valor:
            print('ERRO - Saldo insuficiente')
            return
        self.contas[titular].saldo -= valor
        self.contas[titular].extrato.append(('saque', valor))
        print('OK - Saque realizado:', valor)

    def transferir(self, origem: str, destino: str, valor: float):
        if origem not in self.contas:
            print('ERRO - Conta origem não encontrada')
            return
        if destino not in self.contas:
            print('ERRO - Conta destino não encontrada')
            return
        if self.contas[origem].saldo < valor:
            print('ERRO - Saldo insuficiente')
            return
        self.contas[origem].saldo -= valor
        self.contas[destino].saldo += valor
        self.contas[origem].extrato.append(('transferencia_saida', valor))
        self.contas[destino].extrato.append(('transferencia_entrada', valor))
        print('OK - Transferência realizada:', valor)

    def saldo_atual(self, titular: str):
        if titular not in self.contas:
            print('ERRO - Conta não encontrada:', titular)
            return
        print('SALDO', titular, '=', self.contas[titular].saldo)

    def mostrar_extrato(self, titular: str):
        if titular not in self.contas:
            print('ERRO - Conta não encontrada:', titular)
            return
        print('EXTRATO:', titular)
        for item in self.contas[titular].extrato:
            print(' -', item)


banco = BancoDoStark()
print('Banco do Stark carregado!')

# =========================================
# CENÁRIO INICIAL (caminho feliz)
# =========================================

print('=== CRIAR CONTAS ===')
banco.criar_conta('tony')
banco.criar_conta('pepper')
banco.criar_conta('banner')


print('\n=== DEPÓSITOS ===')
banco.depositar('tony', 1000)
banco.depositar('pepper', 500)



print('Testes - Matheus Ernesto')
# MEUS TESTES - MATHEUS ERNESTO

# TESTE NEGATIVO - DEPOSITO NEGATIVO EM CONTA JUNTO COM FLOAT MUITO PEQUENO (TESTA LIMITACOES)
banco.depositar('tony', -0.00000000000000005) 

banco.saldo_atual('tony')
print(f"{banco.contas['tony'].saldo:.30f}")

# TESTE NEGATIVO - SAQUE COM DIZIMA PERIODICA (TESTA LIMITACOES)
banco.sacar('pepper', 1/3) 
banco.saldo_atual('pepper')

# TESTE NEGATIVO - TESTE DE TRANSFERENCIA PARA SI MESMO
banco.depositar('banner', 400) 
banco.transferir('banner', 'banner', 1.3) 
banco.saldo_atual('banner')

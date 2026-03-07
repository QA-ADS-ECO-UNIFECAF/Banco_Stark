# -*- coding: utf-8 -*-
"""
Atividade: QA Manual - Banco do Stark
Analista: Robson Paulo da Silva
Arquivo: novos_testes_banco_stark.py
"""

# =============================================================================
# APP: Banco do Stark (Código para Teste)
# =============================================================================

class Conta:
    def __init__(self, titular: str):
        self.titular = titular
        self.saldo = 0.0
        self.extrato = []

class BancoDoStark:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, titular: str):
        # BUG IDENTIFICADO: Aceita nomes vazios ou com espaços
        if titular in self.contas:
            print('ERRO - Conta já existe:', titular)
            return
        self.contas[titular] = Conta(titular)
        print(f'OK - Conta criada para: "{titular}"')

    def depositar(self, titular: str, valor: float):
        if titular not in self.contas:
            print('ERRO - Conta não encontrada:', titular)
            return
        self.contas[titular].saldo += valor
        self.contas[titular].extrato.append(('deposito', valor))
        print(f'OK - Depósito realizado para {titular}: {valor}')

    def sacar(self, titular: str, valor: float):
        if titular not in self.contas:
            print('ERRO - Conta não encontrada')
            return
        # BUG: Não valida se o valor do saque é negativo (sacar -100 vira depósito)
        if self.contas[titular].saldo < valor:
            print('ERRO - Saldo insuficiente')
            return
        self.contas[titular].saldo -= valor
        self.contas[titular].extrato.append(('saque', valor))
        print(f'OK - Saque realizado: {valor}')

    def transferir(self, origem: str, destino: str, valor: float):
        if origem not in self.contas or destino not in self.contas:
            print('ERRO - Conta(s) inválida(s)')
            return
        # BUG: Permite transferência de valor negativo
        self.contas[origem].saldo -= valor
        self.contas[destino].saldo += valor
        self.contas[origem].extrato.append(('transferencia_saida', valor))
        self.contas[destino].extrato.append(('transferencia_entrada', valor))
        print(f'OK - Transferência de {valor} concluída')


# DOCUMENTAÇÃO: NOVOS CASOS DE TESTE (CT)

"""
ID: CT-004
Título: Validar criação de conta com nome composto
Status: PASS
Resultado esperado: Conta criada com sucesso para "Steve Rogers".
Resultado obtido: OK - Conta criada para: "Steve Rogers"

ID: CT-005
Título: Validar integridade do saldo após múltiplas operações
Status: PASS
Resultado esperado: Saldo final deve ser a soma exata das operações.
Resultado obtido: Saldo bate com o cálculo manual.

ID: CT-006
Título: Validar saque de valor exato ao saldo disponível
Status: PASS
Resultado esperado: Saldo deve zerar sem erros.
Resultado obtido: Saldo Tony = 0.0
"""


# DOCUMENTAÇÃO: NOVOS BUG REPORTS (BR)

"""
BUG REPORT 4
Título: Sistema permite criação de conta com titular vazio ou apenas espaços
Severidade: Média | Prioridade: Alta
Descrição: O sistema aceita " " como nome de titular, dificultando a identificação.
Passos: banco.criar_conta("   ")
Resultado Esperado: Erro de "Nome Inválido".
Resultado Obtido: OK - Conta criada para: "   "

BUG REPORT 5
Título: Saque de valor negativo funciona como depósito oculto
Severidade: Alta | Prioridade: Crítica
Descrição: Ao sacar um valor negativo, o sistema subtrai um número negativo, o que soma ao saldo.
Passos: 1. Saldo 100; 2. Sacar -50.
Resultado Esperado: Erro (valor deve ser > 0).
Resultado Obtido: Saldo sobe para 150.

BUG REPORT 6
Título: Transferência negativa inverte os papéis de Origem e Destino
Severidade: Alta | Prioridade: Alta
Descrição: Transferir -100 de Tony para Pepper tira dinheiro de Pepper e dá para Tony.
Passos: banco.transferir('tony', 'pepper', -100)
Resultado Esperado: Bloqueio de valores negativos.
Resultado Obtido: Tony ganha 100 e Pepper perde 100.
"""

# =============================================================================
# EXECUÇÃO DOS NOVOS TESTES


if __name__ == "__main__":
    banco = BancoDoStark()
    
    print("--- TESTANDO NOVOS BUGS ---")
    
    print("\nTeste BR-04: Nome vazio")
    banco.criar_conta("   ") # Bug: Criou conta fantasma
    
    print("\nTeste BR-05: Saque Negativo (Exploit de saldo)")
    banco.criar_conta("tony")
    banco.depositar("tony", 100)
    banco.sacar("tony", -500) # Bug: O saldo vai aumentar!
    print(f"Saldo atual Tony: {banco.contas['tony'].saldo}")
    
    print("\nTeste BR-06: Transferência Reversa (Valor Negativo)")
    banco.criar_conta("pepper")
    banco.depositar("pepper", 1000)
    # Tony quer "roubar" da Pepper usando valor negativo
    banco.transferir("tony", "pepper", -200) 
    print(f"Saldo Tony: {banco.contas['tony'].saldo}")
    print(f"Saldo Pepper: {banco.contas['pepper'].saldo}")
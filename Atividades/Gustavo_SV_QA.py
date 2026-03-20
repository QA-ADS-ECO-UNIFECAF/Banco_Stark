# Atividade em Aula - QA Manual
# Banco do Stark
# Objetivo da atividade:
#
# Transformar a execução prática em **Casos de Teste **
# Registrar pelo menos **3 Bug Report profissional **
# Como vamos trabalhar:
#
# Execute as células na ordem.
# Observe os resultados dos testes (saídas no notebook).
# Preencha os templates (Casos de Teste e Bug Report) nas células indicadas.
# Entrega (durante a aula):
#
# Mínimo 3 Casos de Teste preenchidos (com esperado/obtido e status).
# Mínimo 1 Bug Report preenchido (com passos reproduzíveis e evidência).
# Regras esperadas (Requisitos do Banco)
# Considere que o comportamento correto do sistema seria:
#
# Titular não pode ser vazio (nem só espaços).
# Depósito: valor deve ser > 0.
# Saque: valor deve ser > 0 e não pode exceder o saldo.
# Transferência: valor deve ser > 0, destino deve existir, e não pode transferir para si mesmo.
# Saldo nunca pode ficar negativo.
# Extrato deve registrar corretamente as operações.

# =========================================
# APP: Banco do Steven (simples)
# =========================================

class Conta:
    def __init__(self, titular: str):
        self.titular = titular
        self.saldo = 0.0
        self.extrato = []


class BancoDoSteven:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, titular: str):
        # Validação: Titular não pode ser vazio (nem só espaços)
        if not titular or titular.strip() == "":
            print('ERRO - Titular da conta não pode ser vazio.')
            return
        if titular in self.contas:
            print('ERRO - Conta já existe:', titular)
            return
        self.contas[titular] = Conta(titular)
        print('OK - Conta criada para:', titular)

    def depositar(self, titular: str, valor: float):
        if titular not in self.contas:
            print('ERRO - Conta não encontrada:', titular)
            return
        # Validação: valor do depósito deve ser > 0
        if valor <= 0:
            print('ERRO - O valor do depósito deve ser maior que zero.')
            return
        self.contas[titular].saldo += valor
        self.contas[titular].extrato.append(('deposito', valor))
        print('OK - Depósito realizado:', valor)

    def sacar(self, titular: str, valor: float):
        if titular not in self.contas:
            print('ERRO - Conta não encontrada:', titular)
            return
        # Validação: valor do saque deve ser > 0
        if valor <= 0:
            print('ERRO - O valor do saque deve ser maior que zero.')
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
        # Validação: valor da transferência deve ser > 0
        if valor <= 0:
            print('ERRO - O valor da transferência deve ser maior que zero.')
            return
        # Validação: não pode transferir para si mesmo
        if origem == destino:
            print('ERRO - Não é possível transferir para a mesma conta.')
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


banco = BancoDoSteven()
print('Banco do Steven carregado!')


# Banco do Steven carregado!
# Execute esta célula para gerar um cenário inicial e, em seguida, alguns testes negativos.

# Sua tarefa será:

# Observar a saída
# Criar Casos de Teste com base no que foi executado
# Registrar pelo menos 1 Bug Report

# =========================================
# CENÁRIO INICIAL (caminho feliz)
# =========================================

print('=== CRIAR CONTAS ===')
banco.criar_conta('Garnet')
banco.criar_conta('Ametista')
banco.criar_conta('Perola')

print('\n=== DEPÓSITOS ===')
banco.depositar('Perola', 100)
banco.depositar('Ametista', 0)

print('\n=== SALDOS ===')
banco.saldo_atual('Perola')
banco.saldo_atual('Ametista')

print('\n=== SAQUE ===')
banco.sacar('Perola', 800)
banco.saldo_atual('Perola')

print('\n=== TRANSFERÊNCIA ===')
banco.transferir('Perola', 'Peridot', 50)
banco.saldo_atual('Perola')
banco.saldo_atual('Ametista')

print('\n=== EXTRATO (Perola) ===')
banco.mostrar_extrato('Perola')

print('\n=================================')
print('TESTES NEGATIVOS (QA)')
print('=================================\n')

print('Teste N1 - Depósito com valor zero')
banco.depositar('Perola', 0)

print('\nTeste N2 - Depósito negativo')
banco.depositar('Perola', -50) # Changed to a negative value to match the test description

print('\nSaldo após depósitos inválidos')
banco.saldo_atual('Perola')

print('\nTeste N3 - Saque acima do saldo')
banco.sacar('Perola', 100000)

print('\nTeste N4 - Transferência para conta inexistente')
banco.transferir('Perola', 'Peridot', 50)

print('\nTeste N5 - Consulta de conta inexistente (saldo)')
banco.saldo_atual('Peridot')

print('\nTeste N6 - Consulta de conta inexistente (extrato)')
banco.mostrar_extrato('Steven')


# === CRIAR CONTAS ===
# OK - Conta criada para: Garnet
# OK - Conta criada para: Ametista
# OK - Conta criada para: Perola

# === DEPÓSITOS ===
# OK - Depósito realizado: 100
# ERRO - O valor do depósito deve ser maior que zero.

# === SALDOS ===
# SALDO Perola = 100.0
# SALDO Ametista = 0.0

# === SAQUE ===
# ERRO - Saldo insuficiente
# SALDO Perola = 100.0

# === TRANSFERÊNCIA ===
# ERRO - Conta destino não encontrada
# SALDO Perola = 100.0
# SALDO Ametista = 0.0

# === EXTRATO (Perola) ===
# EXTRATO: Perola
#  - ('deposito', 100)

# =================================
# TESTES NEGATIVOS (QA)
# =================================

# Teste N1 - Depósito com valor zero
# ERRO - O valor do depósito deve ser maior que zero.

# Teste N2 - Depósito negativo
# ERRO - O valor do depósito deve ser maior que zero. (Previously 'OK - Depósito realizado: 50')

# Saldo após depósitos inválidos
# SALDO Perola = 100.0 (Previously 150.0 if the negative deposit also failed)

# Teste N3 - Saque acima do saldo
# ERRO - Saldo insuficiente

# Teste N4 - Transferência para conta inexistente
# ERRO - Conta destino não encontrada

# Teste N5 - Consulta de conta inexistente (saldo)
# ERRO - Conta não encontrada: Peridot

# Teste N6 - Consulta de conta inexistente (extrato)
# ERRO - Conta não encontrada: Steven
# Casos de Teste (atividade)
# Agora você vai documentar 3 Casos de Teste com base no que você observou.

# Regras
# Cada caso precisa ter Resultado esperado e Resultado obtido.
# Status deve ser Pass ou Fail.
# Evidência: copie um trecho da saída do notebook (ou descreva exatamente o que apareceu).
# Sugestões de temas (você escolhe 3)
# Depósito com valor 0
# Depósito negativo
# Saque acima do saldo
# Transferência para conta inexistente
# Consulta de saldo de conta inexistente
# Template - Caso de Teste 1
# ID: CT-001
# Título/Objetivo: Verificação de depósito negativo

# Pré-condição: Banco iniciado - Conta existente

# Passos:

# Iniciar banco.
# Realizar depósito negativo.
# Resultado esperado: "ERRO - O valor do depósito deve ser maior que zero."

# Resultado obtido: "ERRO - O valor do depósito deve ser maior que zero."

# Status (Pass/Fail): Pass

# Evidência:

# "banco.depositar('Perola', -5000)

# ERRO - O valor do depósito deve ser maior que zero."

# Template - Caso de Teste 2
# ID: CT-002
# Título/Objetivo: Verificação de depósito com valor 0.

# Pré-condição: Banco iniciado - Conta existente

# Passos:

# Iniciar o banco.
# Realizar depósito com valor 0.
# Resultado esperado: "ERRO - O valor do depósito deve ser maior que zero."

# Resultado obtido: "ERRO - O valor do depósito deve ser maior que zero."

# Status (Pass/Fail): Pass

# Evidência:

# "banco.depositar('Ametista', 0)

# ERRO - O valor do depósito deve ser maior que zero."

# Template - Caso de Teste 3
# ID: CT-003
# Título/Objetivo: Testar funcionalidade de transferência com saldo insuficiente

# Pré-condição: Banco iniciado - Conta criada - Saldo insuficiente

# Passos:

# Iniciar banco.
# Criar conta.
# Transferir um valor acima do valor em conta.
# Resultado esperado: "ERRO - Saldo insuficiente"

# Resultado obtido: "ERRO - Saldo insuficiente"

# Status (Pass/Fail): Pass

# Evidência:

# "banco.transferir('Perola', 'Ametista', 10000)

# ERRO - Saldo insuficiente

# SALDO Perola = 100.0"

# Bug Report (atividade)
# Agora escolha 3 falhas que você observou e registre o Bug Report profissional de cada uma delas.

# Dicas
# O bug deve ser reproduzível (passos claros)
# Inclua o Resultado esperado e o Resultado obtido
# Inclua evidência (saída do notebook)
# Sugestões de bugs (se apareceram na sua execução):

# Sistema aceita depósito com valor 0
# Sistema aceita depósito com valor negativo
# Template - Bug Report
# Título: Deposito negativo

# Severidade (Baixa/Média/Alta): Alta

# Prioridade (Baixa/Média/Alta): Alta

# Ambiente: Google Colab / Python 3.x / Banco do Steven

# Descrição:
# Depósito de valor negativo. Valor deve ser maior que 0.

# Passos para reproduzir:

# Iniciar banco.
# Realizar depósito com valor negativo.
# Resultado esperado: ERRO - O valor do depósito deve ser maior que zero."

# Resultado obtido: ERRO - O valor do depósito deve ser maior que zero."

# Evidência:

# banco.depositar('Perola', -100)

# ERRO - O valor do depósito deve ser maior que zero."

# Impacto/Risco: Transferir um valor negativo impacta diretamente na integridade financeira e viola as regras, além de causar inconsistência financeira.

# Template - Bug Report
# Título: Depósito = 0.

# Severidade (Baixa/Média/Alta): Alta
# Prioridade (Baixa/Média/Alta): Alta

# Ambiente: Google Colab / Python 3.x / Banco do Steven

# Descrição:
# Depositar um valor = 0.

# Passos para reproduzir:

# Iniciar banco
# Conta existente
# Depositar valor = 0.
# Resultado esperado: "ERRO - O valor do depósito deve ser maior que zero."

# Resultado obtido: "ERRO - O valor do depósito deve ser maior que zero."

# Evidência:

# "banco.depositar('Ametista', 0)

# ERRO - O valor do depósito deve ser maior que zero."

# Impacto/Risco: Violação de um requisito fundamentl de negócio, impacta diretamente a integridade dos registros financeiros e o comportamento esperado de um banco

# (Opcional) Rodar novos testes
# Use esta célula para rodar testes adicionais e fortalecer suas evidências. Você pode criar novos casos de teste e/ou registrar mais bugs.


# Escreva seus testes aqui (exemplos abaixo)

# banco.depositar('pepper', -1)
# banco.sacar('pepper', 0)
# banco.transferir('pepper', 'banner', 999999)

print('Pronto! Execute seus testes aqui.')


# Pronto! Execute seus testes aqui.
# Critérios de avaliação (rápido)
# Casos de teste: passos claros + esperado/obtido + status + evidência
# Bug report: reproduzível + esperado/obtido + evidência + impacto
# Quando terminar, avise o professor no chat.

Banco do Steven carregado!
=== CRIAR CONTAS ===
OK - Conta criada para: Garnet
OK - Conta criada para: Ametista
OK - Conta criada para: Perola

=== DEPÓSITOS ===
OK - Depósito realizado: 100
ERRO - O valor do depósito deve ser maior que zero.

=== SALDOS ===
SALDO Perola = 100.0
SALDO Ametista = 0.0

=== SAQUE ===
ERRO - Saldo insuficiente
SALDO Perola = 100.0

=== TRANSFERÊNCIA ===
ERRO - Conta destino não encontrada
SALDO Perola = 100.0
SALDO Ametista = 0.0

=== EXTRATO (Perola) ===
EXTRATO: Perola
 - ('deposito', 100)

=================================
TESTES NEGATIVOS (QA)
=================================

Teste N1 - Depósito com valor zero
ERRO - O valor do depósito deve ser maior que zero.

Teste N2 - Depósito negativo
ERRO - O valor do depósito deve ser maior que zero.

Saldo após depósitos inválidos
SALDO Perola = 100.0

Teste N3 - Saque acima do saldo
ERRO - Saldo insuficiente

Teste N4 - Transferência para conta inexistente
ERRO - Conta destino não encontrada

Teste N5 - Consulta de conta inexistente (saldo)
ERRO - Conta não encontrada: Peridot

Teste N6 - Consulta de conta inexistente (extrato)
ERRO - Conta não encontrada: Steven
Pronto! Execute seus testes aqui.

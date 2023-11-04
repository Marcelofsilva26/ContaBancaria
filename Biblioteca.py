import datetime

class ContaBancaria:
    def __init__(self, numero, saldo, nome, tipo, status, limite):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.status = status
        self.limite = limite
        self.ultima_operacao = None

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if self.status == "ativa":
            if valor > 0 and valor <= self.saldo + self.limite:
                self.saldo -= valor
                self.ultima_operacao = datetime.datetime.now()
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Valor de saque inválido ou saldo insuficiente.")
        else:
            print("Conta desativada. Não é possível realizar saques.")

    def ativar_conta(self):
        if self.saldo == 0:
            self.status = "ativa"
            print("Conta ativada com sucesso.")
        else:
            print("Não é possível ativar a conta com saldo diferente de zero.")

    def verificar_saldo(self):
        print(f"Saldo da conta: R${self.saldo:.2f}")




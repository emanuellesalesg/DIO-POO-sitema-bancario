from transacao import Transacao
from conta import Conta

class Saque(Transacao):
    def __init__(self, num_saques) -> None:
        self.saque_max = 500.
        self._num_saques = num_saques

    def get_numero_saques(self):
        return self._num_saques

    def registrar(self, conta: Conta, valor: float) -> None:

        if valor > 0 and valor <= self.saque_max and self.get_numero_saques() < 3:
            if conta.get_saldo() >= valor:
                novo_saldo = conta.get_saldo() - valor
                conta.set_saldo(novo_saldo)
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
                conta._historico.adicionar_historico(f"Saque de R$ {valor:.2f} realizado com sucesso.")
                self._num_saques += 1
            else:
                print("@ERRO Saldo insuficiente para realizar o saque.")
        else:
            print(f"@ERRO Limite de saque excedido (máx. R$ {self.saque_max:.2f}) ou número máximo de saques atingido (3 saques por dia).")

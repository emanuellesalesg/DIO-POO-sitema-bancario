from transacao import Transacao
from conta import Conta

class Deposito(Transacao):

    def registrar(self, conta: Conta, valor: float) -> None:
        if valor > 0:
            conta.set_saldo(conta.get_saldo() + valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            conta._historico.adicionar_historico(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("@ERRO Valor informado inválido.")

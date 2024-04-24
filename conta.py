import random
from historico import Historico

class Conta:
    def __init__(self) -> None:
        self._saldo = 0.
        self._numero = self.gerar_numero_unico()
        self._agencia = "0001"
        self._historico = Historico()
    
    def get_agencia(self) -> str:
        return self._agencia
    
    def get_numero(self) -> int:
        return self._numero
    
    def get_saldo(self) -> float:
        return self._saldo
    
    def get_historico(self) -> str:
        return self._historico.get_historico()
    
    def set_saldo(self, saldo: float) -> None:
        self._saldo = saldo
    
    def __str__(self) -> str:
        return f"Agência: {self._agencia}\nConta: {self._numero}\nSaldo: {self._saldo}\nHistórico: {self._historico.get_historico()}"

    def gerar_numero_unico(self) -> str:
        numero_aleatorio = random.randint(100, 999)
        return str(numero_aleatorio)

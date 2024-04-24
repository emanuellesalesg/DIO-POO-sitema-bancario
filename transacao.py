from abc import ABC, abstractmethod
from conta import Conta

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta: Conta, valor: float) -> None:
        pass

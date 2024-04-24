class Historico:
    def __init__(self) -> None:
        self._historico = ''
    
    def adicionar_historico(self, nova_operacao: str) -> None:
        self._historico += f'\n{nova_operacao}'
    
    def get_historico(self) -> str:
        return self._historico

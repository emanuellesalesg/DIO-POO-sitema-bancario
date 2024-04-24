class Cliente:
    def __init__(self, endereco: str) -> None:
        self._endereco = endereco
        self.contas = []
    
    def get_endereco(self) -> str:
        return str(self._endereco)
    
    def criar_conta(self, conta) -> None:
        self.contas.append(conta)
        print("## Conta Criada com Sucesso")

    def mostrar_contas(self) -> None:
        for conta in self.contas:
            print(f"Agência: {conta.get_agencia()}, Número: {conta.get_numero()}, Saldo: {conta.get_saldo()}")
    
    def buscar_conta(self, numero_conta):
        for conta in self.contas:
            if conta.get_numero() == numero_conta:
                return conta
        return None
    
    def realizar_transacao(self, transacao, conta, valor: float) -> None:
        transacao.registrar(conta, valor)

from cliente import Cliente

class PessoaFisica(Cliente):
    def __init__(self, cpf: int, nome: str, data_nascimento: str, endereco: str) -> None:
        super().__init__(endereco)
        self._cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
    
    def get_cpf(self) -> int:
        return self._cpf
    
    def cliente_info(self) -> None:
        print(f"Pessoa Física\nNome: {self.nome}\nCPF: {self._cpf}\nEndereço: {self.get_endereco()}\n")
    
    def __str__(self) -> str:
        return f"## Pessoa Física\nNome: {self.nome}\nCPF: {self._cpf}\nEndereço: {super().get_endereco()}"

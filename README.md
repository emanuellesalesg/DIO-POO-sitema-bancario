# Documentação do Código

Este documento descreve a estrutura e o funcionamento do sistema bancário implementado em Python, como participação do `bootcamp Python AI Backend Developer da DIO`. O sistema inclui classes para representar clientes, contas bancárias e transações.

## Resumo e Considerações

Este sistema bancário backend permite a criação de usuários identificados por CPF, com a capacidade de associar várias contas a cada usuário. Cada conta possui seu próprio sistema de transações, permitindo depósitos, saques e visualizar histórico de transação. O sistema também implementa regras de limitação, como até 3 saques por dia, com um limite máximo de saque de R$500 por transação.


## Funcionalidades Principais

- **Cadastro de Clientes**:
  - Permite criar clientes do tipo pessoa física e associar contas bancárias a eles.

- **Operações Bancárias**:
  - Depósito: Adiciona fundos a uma conta específica.
  - Saque: Retira fundos de uma conta respeitando limitações de valor máximo e número de saques diários.

- **Consulta e Visualização**:
  - Mostra saldo e histórico de transações de uma conta.

## Futuras Implementações

- **Futuras Implementações**:
  - Adição de diferentes tipos de conta, como conta corrente e poupança.
  - Integração do sistema com um banco de dados para armazenamento persistente dos dados fornecidos.

## Exemplo de Utilização: `banco_teste.py`

O código inclui um sistema de menu interativo para realizar operações bancárias. Aqui está um resumo do fluxo principal:

1. **Cadastro de Cliente e Conta**:
   - Solicita informações básicas do cliente (nome, CPF, etc.).
   - Cria uma nova conta associada ao cliente.

2. **Login em Conta**:
   - Permite acesso às operações da conta (depósito, saque, consulta de saldo e histórico).

3. **Operações na Conta**:
   - Realiza depósitos e saques na conta associada ao cliente.
   - Consulta saldo e histórico de transações.

4. **Saída do Programa**:
   - Permite encerrar o programa quando o usuário desejar.

## Estrutura do Código

O código está organizado em várias classes, cada uma responsável por uma funcionalidade específica. Abaixo está a descrição de cada classe e seu propósito.

### Classe `Cliente`

- **Métodos Principais**:
  - `__init__(self, endereco: str) -> None`: Inicializa um cliente com um endereço.
  - `get_endereco(self) -> str`: Retorna o endereço do cliente.
  - `criar_conta(self, conta) -> None`: Cria uma nova conta para o cliente.
  - `mostrar_contas(self) -> None`: Mostra todas as contas associadas ao cliente.
  - `buscar_conta(self, numero_conta)`: Busca uma conta específica do cliente pelo número.
  - `realizar_transacao(self, transacao, conta, valor: float) -> None`: Realiza uma transação em uma conta específica.

### Classe `Conta`

- **Métodos Principais**:
  - `__init__(self) -> None`: Inicializa uma conta com saldo zero e um número único.
  - `get_agencia(self) -> str`: Retorna a agência da conta.
  - `get_numero(self) -> int`: Retorna o número da conta.
  - `get_saldo(self) -> float`: Retorna o saldo atual da conta.
  - `get_historico(self) -> str`: Retorna o histórico de transações da conta.
  - `set_saldo(self, saldo: float) -> None`: Define o saldo da conta.
  - `gerar_numero_unico(self) -> str`: Gera um número único para a conta.

### Classe `Deposito`

- **Métodos Principais**:
  - `registrar(self, conta: Conta, valor: float) -> None`: Registra um depósito em uma conta específica.

### Classe `Saque`

- **Métodos Principais**:
  - `registrar(self, conta: Conta, valor: float) -> None`: Registra um saque em uma conta específica, respeitando limites.

### Classe `Historico`

- **Métodos Principais**:
  - `__init__(self) -> None`: Inicializa um objeto de histórico vazio.
  - `adicionar_historico(self, nova_operacao: str) -> None`: Adiciona uma nova operação ao histórico.
  - `get_historico(self) -> str`: Retorna o histórico completo como uma string.

### Classe `Transacao` (classe abstrata)

- **Métodos Principais**:
  - `registrar(self, conta: Conta, valor: float) -> None`: Método abstrato para registrar uma transação.

### Classe `PessoaFisica`

- **Métodos Principais**:
  - `__init__(self, cpf: int, nome: str, data_nascimento: str, endereco: str) -> None`: Inicializa uma pessoa física com dados pessoais.
  - `get_cpf(self) -> int`: Retorna o CPF da pessoa física.
  - `cliente_info(self) -> None`: Mostra informações sobre o cliente.

## Observações

- Este código foi desenvolvido com fins educacionais e pode ser expandido com mais funcionalidades, como cadastro de outros tipos de clientes e operações bancárias adicionais.
- Certifique-se de fornecer entradas válidas de acordo com as solicitações dos menus para evitar erros durante a execução.

Este sistema bancário básico demonstra conceitos fundamentais de orientação a objetos e interação com o usuário em Python.

- Agradeço a DIO pela oportunidade e o desafio.</br></br> 
Emanuelle Gonçalo

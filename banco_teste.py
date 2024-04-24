from pessoa_fisica import PessoaFisica
from conta import Conta
from deposito import Deposito
from saque import Saque

#Banco Teste é para teste de aplicação:

menu = """
============= Bem Vindo(a) =============

[1] Realizar cadastro
[2] Usuário
[s] Sair

========================================
--> """
menu2 = """
================ Contas ================

[1] Criar nova conta
[2] Login em conta
[s] Sair

========================================
--> """
menu3 = """
============== Operações ===============

[1] Depositar
[2] Sacar
[3] Saldo
[4] Histórico
[s] Sair

========================================
--> """

lista_clientes = []
numero_saque = 0

# Para teste foram criados um total de 3 menu. 
# Menu 1 - Realiza cadastro e faz login em usuário.
# Menu 2 - Cria novas contas para o mesmo usuário e faz login em conta existente.
# Menu 3 - Faz operações na conta desejada.

while True:
    # Menu 1
    opcao = input(menu)

    if opcao == '1':
        
        nome = input("Nome: ")
        cpf = int(input("CPF: "))
        data_nascimento = input("Data de Nascimento: ")
        endereco = input("Endereco: ")
        
        cliente = PessoaFisica(cpf, nome, data_nascimento, endereco)
    
        lista_clientes.append(cliente)
        print("\nCriando conta...\n")
        conta = Conta()
        lista_clientes[-1].criar_conta(conta)
        print("\n\n##Cadastro realizado com sucesso!")
        print(f"Bem vindo(a) {cliente.nome}!\n")
        print(conta)


    elif opcao == '2':

        print("\nÀrea do Cliente!\n")
        cpf = int(input("CPF: "))

        for clientes in lista_clientes:
            if cliente.get_cpf() == cpf:
                sair = False
                
                # Menu 2
                while True:
                    
                    if not sair:
                        print("Bem-vindo(a)\n")
                        numero_conta = input("Número da conta:\n")
                    
                        conta_transacao = cliente.buscar_conta(numero_conta)
                    else:
                        break

                    if conta_transacao:
                        
                        # Menu 3
                        while True:
                            opcao3 = input(menu3)
                            if opcao3 == '1':
                                valor = float(input("Valor: R$"))
                                deposito = Deposito()
                                cliente.realizar_transacao(deposito, conta_transacao, valor)
                            
                            if opcao3 == '2':
                                valor = float(input("Valor: R$ "))
                                sacar = Saque(numero_saque)
                                cliente.realizar_transacao(sacar, conta_transacao, valor)
                                numero_saque = sacar.get_numero_saques()
                                

                            
                            if opcao3 == '3':
                                print(f"R$ {conta.get_saldo():.2f}")
                            
                            if opcao3 == '4':
                                print(conta.get_historico())
    
                            elif opcao3 == 's':
                                sair = True
                                break
                    else:
                        print("@ERRO@ Conta não encontrada.")

            else:
                print("@ERROR@ Usuário não encontrado.")

    elif opcao == 's':
        break

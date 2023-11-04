from Bibiliotecabanco import *


def main():
    contas = {}  # Dicionário para armazenar as contas bancárias

    while True:
        print("\nMenu:")
        print("1. Criar nova conta")
        print("2. Acessar conta existente")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero = input("Digite o número da conta: ")
            nome = input("Digite o nome do cliente: ")
            tipo = input("Digite o tipo da conta: ")
            saldo = float(input("Digite o saldo inicial: "))
            limite = float(input("Digite o limite: "))
            nova_conta = ContaBancaria(numero, saldo, nome, tipo, "ativa", limite)
            contas[numero] = nova_conta
            print("Conta criada com sucesso!")

        elif opcao == "2":
            numero = input("Digite o número da conta: ")
            if numero in contas:
                conta = contas[numero]
                print(f"Acesso à conta de {conta.nome}")
                while True:
                    print("\nOperações:")
                    print("1. Depositar")
                    print("2. Sacar")
                    print("3. Ativar conta")
                    print("4. Verificar saldo")
                    print("5. Sair da conta")
                    operacao = input("Escolha uma operação: ")

                    if operacao == "1":
                        valor = float(input("Digite o valor a depositar: "))
                        conta.depositar(valor)
                    elif operacao == "2":
                        valor = float(input("Digite o valor a sacar: "))
                        conta.sacar(valor)
                    elif operacao == "3":
                        conta.ativar_conta()
                    elif operacao == "4":
                        conta.verificar_saldo()
                    elif operacao == "5":
                        print("Saindo da conta.")
                        break
                    else:
                        print("Opção inválida. Tente novamente.")

            else:
                print("Conta não encontrada. Verifique o número da conta.")

        elif opcao == "3":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

usuarios = []

def cadastrar():
    nome = input("Digite o nome: ")
    usuarios.append(nome)
    print("Usuário cadastrado com sucesso!\n")

def listar():
    print("\n--- Lista de Usuários ---")
    for i, user in enumerate(usuarios, start=1):
        print(f"{i}. {user}")
    print()

def menu():
    while True:
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")

menu()

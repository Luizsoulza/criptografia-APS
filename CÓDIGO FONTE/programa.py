from caracteres import BASE_CARACTERES
from criptografia import criptografar
from descriptografia import descriptografar

def menu():
    while True:
        print("\n====== Menu Principal ======")
        print("1. Criptografar")
        print("2. Descriptografar")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            texto = input("Digite o texto a ser criptografado: ")[:256]
            chave = input("Digite a chave: ")
            criptografado = criptografar(texto, chave, BASE_CARACTERES)
            print("\nTexto criptografado:")
            print(criptografado)

        elif opcao == '2':
            texto = input("Digite o texto criptografado: ")
            chave = input("Digite a chave: ")
            descriptografado = descriptografar(texto, chave, BASE_CARACTERES)
            print("\nTexto descriptografado:")
            print(descriptografado)

        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

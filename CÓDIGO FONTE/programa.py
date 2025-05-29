from caracteres import BASE_CARACTERES
from criptografia import cifra_vigenere
from descriptografia import decifra_vigenere

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
            criptografado = cifra_vigenere(texto, chave, BASE_CARACTERES)
            print("Texto criptografado:", criptografado)

        elif opcao == '2':
            texto = input("Digite o texto criptografado: ")
            chave = input("Digite a chave: ")
            descriptografado = decifra_vigenere(texto, chave, BASE_CARACTERES)
            print("Texto descriptografado:", descriptografado)

        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o programa
if __name__ == "__main__":
    menu()
# programa.py
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
            texto = input("Digite o texto (máx. 256 caracteres): ")
            chave = input("Digite a chave: ")
            if len(texto) > 1000:
                print("Erro: texto muito longo.")
                continue
            if not chave:
                print("Erro: chave vazia.")
                continue
            try:
                criptografado = criptografar(texto, chave)
                print("\nTexto criptografado (hexadecimal):\n" + criptografado)
            except Exception as e:
                print("Erro na criptografia:", e)

        elif opcao == '2':
            texto = input("Digite o texto criptografado (hexadecimal): ")
            chave = input("Digite a chave: ")
            if not chave:
                print("Erro: chave vazia.")
                continue
            try:
                original = descriptografar(texto, chave)
                print("\nTexto descriptografado:\n" + original)
            except Exception as e:
                print("Erro na descriptografia:", e)

        elif opcao == '3':
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()

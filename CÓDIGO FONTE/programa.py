#PROGRAMA


from criptografia import criptografar
from descriptografia import descriptografar

def menu():
    while True:
        print("\n__ALGORITMO DE CRIPTOGRAFIA E DESCRIPTOGRAFIA__")
        print("1. Criptografar")
        print("2. Descriptografar")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            frase = input("Digite a frase para criptografar: ")
            senha = input("Digite a chave: ")
            resultado = criptografar(frase, senha)
            print("Texto criptografado:", resultado)

        elif opcao == '2':
            texto = input("Digite o texto criptografado: ")
            senha = input("Digite a chave: ")
            try:
                resultado = descriptografar(texto, senha)
                print("Frase original:", resultado)
            except Exception as e:
                print("Erro na descriptografia:", e)

        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

menu()

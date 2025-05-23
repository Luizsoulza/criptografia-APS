#criptografia

from criptografia import criptografar
from descriptografia import descriptografar

def menu():
    # Loop pra mostrar o menu até o usuário escolher sair
    while True:
        print("\n=== Criptografia e Descriptografia ===")
        print("1 - Criptografar")
        print("2 - Descriptografar")
        print("3 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            senha = input("Chave: ")
            mensagem = input("Mensagem para criptografar: ")
            resultado = criptografar(mensagem, senha)
            print("Texto criptografado:", resultado)

        elif opcao == '2':
            senha = input("Chave: ")
            mensagem = input("Mensagem criptografada: ")
            try:
                # Tenta descriptografar, mas pode dar erro se a senha estiver errada ou mensagem estiver faltando informação.
                #Ou formatada errada
                resultado = descriptografar(mensagem, senha)
                print("Mensagem original:", resultado)
            except Exception as e:
                # Se der erro, vai aparecer um alert e vai aparecer a opção para descriptografar novamente.
                print("Aconteceu um erro na descriptografia, confira a chave e a mensagem.")

        elif opcao == '3':
            print("Programa encerrado...")
            break

        else:
            print("Opção inválida, tente novamente!")

menu()

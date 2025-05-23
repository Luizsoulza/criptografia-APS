#Criptografia

import os
import base64
import hashlib

# Essa função é responsável por gerar um valor aleatório, um salto de 16 bytes.
def gerar_salt(tamanho=16):
    return os.urandom(tamanho)  # retorna 'tamanho' bytes aleatórios, usando a derivação de chave.
#O salt é usado aqui como uma forma de garantir que a chave gerada a partir da senha seja única,
#mesmo se a senha for a mesma quando outro usuário utilizar o programa.

# Aqui é usado uma derivação de chave criptográfica segura a partir de uma senha e um salt
def gerar_chave(senha, salt, iteracoes=100000):
    # utiliza a função pbkdf2-hmac com sha-256 para derivar uma chave segura
    return hashlib.pbkdf2_hmac('sha256', senha.encode(), salt, iteracoes, dklen=32)

# Monta um vetor de inicialização (iv), também com bytes aleatórios
def gerar_vetor_inicializacao(tamanho=16):
    return os.urandom(tamanho)  # agora será utilizado na permutação

# Realiza a operação de permutação xor entre os dados e a "tabela" que é a chave + iv
def permutar_dados(dados, tabela):
    # para cada byte dos dados, aplica xor com o byte correspondente da tabela.
    return bytes([b ^ tabela[i % len(tabela)] for i, b in enumerate(dados)])

# Função principal que realiza a criptografia de uma frase com base em uma senha
def criptografar(mensagem, senha):
    # gera um salt aleatório para derivar a chave
    salt = gerar_salt()
    
    # deriva a chave a partir da senha e do salt
    chave = gerar_chave(senha, salt)
    
    # gera um iv aleatório
    iv = gerar_vetor_inicializacao()
    
    # converte a frase de texto para bytes
    dados = mensagem.encode()
    
    # Mistura a chave derivada com o iv para criar uma tabela mais robusta para a permutação
    tabela_permutacao = chave + iv
    
    # É aqui que criptografia acontece, a função aplica xor entre cada byte da mensagem e a tabela que criamos com a (chave + iv),
    # embaralhando tudo pra virar um monte de bytes que ninguém entende sem a chave certa
    dados_permutados = permutar_dados(dados, tabela_permutacao)

    # empacota os dados: primeiro o salt, depois o iv, e por fim os dados criptografados
    pacote = salt + iv + dados_permutados
    
    # codifica todo o pacote em base64 para facilitar o transporte como string
    criptografado = base64.b64encode(pacote)
    
    # retorna o resultado como string (decode de base64)
    return criptografado.decode()

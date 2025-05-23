#CRIPTOGRAFIA

import os
import base64
import hashlib

#ESSA FUNÇÃO É RESPONSÁVEL POR GERAR UM VALOR ALEATÓRIO, UM SALTO DE DETERMINADO TAMANHO DE BYTES
def gerar_salt(tamanho=16):
    return os.urandom(tamanho)  # RETORNA 'tamanho' BYTES ALEATÓRIOS, USANDO A DERIVAÇÃO DE CHAVE
"""O SALT É USADO AQUI COMO UMA FORMA DE GARANTIR QUE A CHAVE GERADA A PARTIR DA SENHA SEJA ÚNICA,
MESMO SE A SENHA FOR A MESMA QUANDO OUTRO USUÁRIO UTILIZAR O PROGRAMA"""

#AQUI É USADO UMA DERIVAÇÃO DE CHAVE CRIPTOGRÁFICA SEGURA A PARTIR DE UMA SENHA E UM SALT
def gerar_chave(senha, salt, iteracoes=100000):
    #UTILIZA A FUNÇÃO PBKDF2-HMAC COM SHA-256 PARA DERIVAR UMA CHAVE SEGURA
    return hashlib.pbkdf2_hmac('sha256', senha.encode(), salt, iteracoes, dklen=32)

# Gera um vetor de inicialização (IV), também com bytes aleatórios
def gerar_vetor_inicializacao(tamanho=16):
    return os.urandom(tamanho)  # Embora não usado diretamente, simula um IV tradicional

# Realiza a operação de permutação XOR entre os dados e a "tabela" (chave)
def permutar_dados(dados, tabela):
    # Para cada byte dos dados, aplica XOR com o byte correspondente da tabela (modular)
    return bytes([b ^ tabela[i % len(tabela)] for i, b in enumerate(dados)])

# Função principal que realiza a criptografia de uma frase com base em uma senha
def criptografar(frase, senha):
    # Gera um salt aleatório para derivar a chave
    salt = gerar_salt()
    
    # Deriva a chave a partir da senha e do salt
    chave = gerar_chave(senha, salt)
    
    # Gera um IV aleatório (não é utilizado na permutação, mas armazenado para estrutura)
    iv = gerar_vetor_inicializacao()
    
    # Converte a frase de texto para bytes
    dados = frase.encode()
    
    # Aplica a permutação XOR entre os dados e a chave derivada
    dados_permutados = permutar_dados(dados, chave)
    
    # Empacota os dados: primeiro o salt, depois o IV, e por fim os dados criptografados
    pacote = salt + iv + dados_permutados
    
    # Codifica todo o pacote em Base64 para facilitar o transporte como string
    criptografado = base64.b64encode(pacote)
    
    # Retorna o resultado como string (decode de base64)
    return criptografado.decode()

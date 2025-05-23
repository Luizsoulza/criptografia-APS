# Descriptografia

import base64
import hashlib

# Aqui é usado uma derivação de chave criptográfica segura a partir de uma senha e um salt
def gerar_chave(senha, salt, iteracoes=100000):
    # utiliza a função pbkdf2-hmac com sha-256 para derivar uma chave segura
    return hashlib.pbkdf2_hmac('sha256', senha.encode(), salt, iteracoes, dklen=32)

# Realiza a operação de permutação xor entre os dados e a "tabela" (chave + iv)
def permutar_dados(dados, tabela):
    # Para cada byte dos dados, aplica xor com o byte correspondente da tabela (modular)
    return bytes([b ^ tabela[i % len(tabela)] for i, b in enumerate(dados)])

# Função que realiza a descriptografia de uma frase cifrada com base em uma senha
def descriptografar(texto_criptografado, senha):
    # Decodifica o texto base64 para bytes
    pacote = base64.b64decode(texto_criptografado)
    
    # Extrai o salt (16 bytes) e o iv (16 bytes)
    salt = pacote[:16]
    iv = pacote[16:32]
    
    # o restante são os dados permutados
    dados_permutados = pacote[32:]
    
    # Assim como na criptografia deriva a mesma chave a partir da senha e do salt
    chave = gerar_chave(senha, salt)
    
    # Junta a chave derivada com o iv para criar a tabela de permutação
    tabela_permutacao = chave + iv  # IMPORTANTEEEEE, só com esses dados pra conseguir desfazer a permutação corretamente
    
    # Reverte a permutação xor para obter os dados originais
    dados = permutar_dados(dados_permutados, tabela_permutacao)
    
    # Converte de bytes pra string
    return dados.decode()

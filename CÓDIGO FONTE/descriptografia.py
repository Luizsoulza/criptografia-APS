#DESCRIPTOGRAFIA


import base64
from criptografia import gerar_chave, permutar_dados

def descriptografar(texto_criptografado, senha):
    pacote = base64.b64decode(texto_criptografado)
    salt = pacote[:16]
    iv = pacote[16:32]
    dados_permutados = pacote[32:]

    chave = gerar_chave(senha, salt)
    dados = permutar_dados(dados_permutados, chave)

    return dados.decode()

from caracteres import BASE_CARACTERES

def cifra_vigenere(texto, chave, base):
    chave_expandida = (chave * ((len(texto) // len(chave)) + 1))[:len(texto)]
    resultado = ''
    for char_texto, char_chave in zip(texto, chave_expandida):
        if char_texto in base and char_chave in base:
            indice_texto = base.index(char_texto)
            indice_chave = base.index(char_chave)
            novo_indice = (indice_texto + indice_chave) % len(base)
            resultado += base[novo_indice]
        else:
            resultado += char_texto
    return resultado

def criptografar(texto, chave):
    # Aplica Vigenère 3 vezes
    etapa1 = cifra_vigenere(texto, chave, BASE_CARACTERES)
    etapa2 = cifra_vigenere(etapa1, chave, BASE_CARACTERES)
    etapa3 = cifra_vigenere(etapa2, chave, BASE_CARACTERES)

    # Converte para bytes e depois para hexadecimal
    texto_bytes = etapa3.encode('utf-8')
    texto_hex = texto_bytes.hex()

    return texto_hex

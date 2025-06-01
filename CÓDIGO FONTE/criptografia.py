from caracteres import BASE_CARACTERES

def vigenere(texto, chave, base):
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

def transposicao_bloco(texto, tamanho_bloco=4):
    resultado = ''
    for i in range(0, len(texto), tamanho_bloco):
        bloco = texto[i:i+tamanho_bloco]
        
        resultado += bloco[::-1]
    return resultado

def permutacao_bijetora(bytes_seq):
  
    return bytes(( (b * 3 + 7) % 256 for b in bytes_seq ))

def modificar_chave(chave, modificador):
  
    return chave + modificador
    
def criptografar(texto, chave):

    etapa1 = vigenere(texto, chave, BASE_CARACTERES)


    etapa2 = transposicao_bloco(etapa1)


    chave2 = modificar_chave(chave, '_2')
    etapa3 = vigenere(etapa2, chave2, BASE_CARACTERES)


    chave3 = modificar_chave(chave, '_3')
    etapa4 = vigenere(etapa3, chave3, BASE_CARACTERES)


    etapa4_bytes = etapa4.encode('utf-8')
    etapa5_bytes = permutacao_bijetora(etapa4_bytes)

    texto_encriptado = etapa5_bytes.hex()
    return texto_encriptado

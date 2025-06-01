from caracteres import BASE_CARACTERES

def vigenere_decifrar(texto, chave, base):
    chave_expandida = (chave * ((len(texto) // len(chave)) + 1))[:len(texto)]
    resultado = ''
    for char_texto, char_chave in zip(texto, chave_expandida):
        if char_texto in base and char_chave in base:
            indice_texto = base.index(char_texto)
            indice_chave = base.index(char_chave)
            novo_indice = (indice_texto - indice_chave) % len(base)
            resultado += base[novo_indice]
        else:
            resultado += char_texto
    return resultado

def permutacao_bijetora_inversa(bytes_seq):
    return bytes(((171 * (b - 7)) % 256 for b in bytes_seq))

def transposicao_bloco_inversa(texto, tamanho_bloco=4):
    resultado = ''
    for i in range(0, len(texto), tamanho_bloco):
        bloco = texto[i:i+tamanho_bloco]
        resultado += bloco[::-1]
    return resultado

def modificar_chave(chave, modificador):
    return chave + modificador

def descriptografar(texto_hex, chave):
    
    etapa1_bytes = bytes.fromhex(texto_hex)

    etapa2_bytes = permutacao_bijetora_inversa(etapa1_bytes)

    etapa2_str = etapa2_bytes.decode('utf-8')

    chave3 = modificar_chave(chave, '_3')
    etapa3 = vigenere_decifrar(etapa2_str, chave3, BASE_CARACTERES)

    chave2 = modificar_chave(chave, '_2')
    etapa4 = vigenere_decifrar(etapa3, chave2, BASE_CARACTERES)

    etapa5 = transposicao_bloco_inversa(etapa4)
 
    etapa6 = vigenere_decifrar(etapa5, chave, BASE_CARACTERES)

    return etapa6


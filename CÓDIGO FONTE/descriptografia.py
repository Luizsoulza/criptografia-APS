from caracteres import BASE_CARACTERES

def decifra_vigenere(texto, chave, base):
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
    # inverso multiplicativo de 3 mod 256 é 171
    return bytes(((171 * (b - 7)) % 256 for b in bytes_seq))

def cifra_vigenere_decifrar(texto, chave, base):
    chave_expandida = (chave * ((len(texto) // len(chave)) + 1))[:len(texto)]
    resultado = ''
    for char_texto, char_chave in zip(texto, chave_expandida):
        if char_texto in base and char_chave in base:
            indice_texto = base.index(char_texto)
            indice_chave = base.index(char_chave)
            novo_indice = (indice_texto - indice_chave) % len(base)  # note a subtração aqui!
            resultado += base[novo_indice]
        else:
            resultado += char_texto
    return resultado

def transposicao_bloco_inversa(texto, tamanho_bloco=4):
    resultado = ''
    for i in range(0, len(texto), tamanho_bloco):
        bloco = texto[i:i+tamanho_bloco]
        # Regra inversa: inverte o bloco (igual a original, pois inverter 2x volta ao normal)
        resultado += bloco[::-1]
    return resultado

def modificar_chave(chave, modificador):
    # mesma função que antes
    return chave + modificador

def descriptografar(texto_hex, chave):
    # 1 - hex para bytes
    etapa1_bytes = bytes.fromhex(texto_hex)

    # 2 - função matemática inversa (permutação bijetora inversa)
    etapa2_bytes = permutacao_bijetora_inversa(etapa1_bytes)

    # 3 - bytes para string UTF-8
    etapa2_str = etapa2_bytes.decode('utf-8')

    # 4 - Vigenère com chave 3 modificada (decifrar)
    chave3 = modificar_chave(chave, '_3')
    etapa3 = cifra_vigenere_decifrar(etapa2_str, chave3, BASE_CARACTERES)

    # 5 - Vigenère com chave 2 modificada (decifrar)
    chave2 = modificar_chave(chave, '_2')
    etapa4 = cifra_vigenere_decifrar(etapa3, chave2, BASE_CARACTERES)

    # 6 - transposição inversa (inverter blocos)
    etapa5 = transposicao_bloco_inversa(etapa4)

    # 7 - Vigenère com chave 1 (decifrar)
    etapa6 = cifra_vigenere_decifrar(etapa5, chave, BASE_CARACTERES)

    return etapa6



"""def descriptografar(texto_hex, chave):
    # Converte hexadecimal para texto
    try:
        texto_bytes = bytes.fromhex(texto_hex)
        texto = texto_bytes.decode('utf-8')
    except Exception as e:
        raise ValueError("Erro ao converter hexadecimal para texto.") from e

    # Aplica Vigenère 3 vezes (inverso)
    etapa1 = decifra_vigenere(texto, chave, BASE_CARACTERES)
    etapa2 = decifra_vigenere(etapa1, chave, BASE_CARACTERES)
    etapa3 = decifra_vigenere(etapa2, chave, BASE_CARACTERES)

    return etapa3 """

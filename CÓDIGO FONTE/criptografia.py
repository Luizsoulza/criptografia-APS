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


def transposicao_bloco(texto, tamanho_bloco=4):
    resultado = ''
    for i in range(0, len(texto), tamanho_bloco):
        bloco = texto[i:i+tamanho_bloco]
        # regra fixa: inverte o bloco
        resultado += bloco[::-1]
    return resultado



def permutacao_bijetora(bytes_seq):
    # Exemplo simples: para cada byte b, calcula (b * 3 + 7) mod 256
    return bytes(( (b * 3 + 7) % 256 for b in bytes_seq ))

def modificar_chave(chave, modificador):
    # Exemplo simples: concatena um texto fixo
    return chave + modificador



"""def criptografar(texto, chave):
    # Aplica Vigenère 3 vezes
    etapa1 = cifra_vigenere(texto, chave, BASE_CARACTERES)
    etapa2 = cifra_vigenere(etapa1, chave, BASE_CARACTERES)
    etapa3 = cifra_vigenere(etapa2, chave, BASE_CARACTERES)

    # Converte para bytes e depois para hexadecimal
    texto_bytes = etapa3.encode('utf-8')
    texto_hex = texto_bytes.hex()

    return texto_hex"""
    
def criptografar(texto, chave):
    # 1 - Vigenère (chave 1)
    etapa1 = cifra_vigenere(texto, chave, BASE_CARACTERES)

    # 2 - Transposição (blocos)
    etapa2 = transposicao_bloco(etapa1)

    # 3 - Vigenère (chave 2 modificada)
    chave2 = modificar_chave(chave, '_2')
    etapa3 = cifra_vigenere(etapa2, chave2, BASE_CARACTERES)

    # 4 - Vigenère (chave 3 modificada)
    chave3 = modificar_chave(chave, '_3')
    etapa4 = cifra_vigenere(etapa3, chave3, BASE_CARACTERES)

    # 5 - Função matemática bijetora nos bytes (sem chave)
    etapa4_bytes = etapa4.encode('utf-8')
    etapa5_bytes = permutacao_bijetora(etapa4_bytes)

    # 6 - Saída em hexadecimal
    texto_final_hex = etapa5_bytes.hex()
    return texto_final_hex

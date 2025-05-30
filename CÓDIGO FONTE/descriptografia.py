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

def descriptografar(texto_hex, chave):
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

    return etapa3

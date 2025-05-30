from caracteres import BASE_CARACTERES as base

def cifra_vigenere(texto, chave_expandida, base):
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

def xor_indices(texto, chave_expandida, base):
    resultado = ''
    for c, k in zip(texto, chave_expandida):
        if c in base and k in base:
            i_c = base.index(c)
            i_k = base.index(k)
            i_xor = i_c ^ i_k
            # Garantir que o índice XOR está dentro da base
            i_xor = i_xor % len(base)
            resultado += base[i_xor]
        else:
            resultado += c
    return resultado

def criptografar(texto, chave, base):
    chave_expandida = (chave * ((len(texto) // len(chave)) + 1))[:len(texto)]
    texto_cifrado = cifra_vigenere(texto, chave_expandida, base)
    texto_cifrado = xor_indices(texto_cifrado, chave_expandida, base)
    return texto_cifrado

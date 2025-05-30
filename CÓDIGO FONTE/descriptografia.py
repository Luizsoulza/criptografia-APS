from caracteres import BASE_CARACTERES as base

def decifra_vigenere(texto, chave_expandida, base):
    resultado = ''
    for t, k in zip(texto, chave_expandida):
        if t in base and k in base:
            t_index = base.index(t)
            k_index = base.index(k)
            novo_index = (t_index - k_index) % len(base)
            resultado += base[novo_index]
        else:
            resultado += t
    return resultado

def xor_indices_inversa(texto, chave_expandida, base):
    # XOR inverso é o mesmo do direto
    resultado = ''
    for c, k in zip(texto, chave_expandida):
        if c in base and k in base:
            i_c = base.index(c)
            i_k = base.index(k)
            i_xor = i_c ^ i_k
            i_xor = i_xor % len(base)
            resultado += base[i_xor]
        else:
            resultado += c
    return resultado

def descriptografar(texto_cifrado, chave, base):
    chave_expandida = (chave * ((len(texto_cifrado) // len(chave)) + 1))[:len(texto_cifrado)]
    texto_xor_desfeito = xor_indices_inversa(texto_cifrado, chave_expandida, base)
    texto_original = decifra_vigenere(texto_xor_desfeito, chave_expandida, base)
    return texto_original

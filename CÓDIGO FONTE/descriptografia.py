def decifra_vigenere(texto, chave, base):
    resultado = ''
    chave_expandida = (chave * ((len(texto) // len(chave)) + 1))[:len(texto)]
    for t, k in zip(texto, chave_expandida):
        if t in base and k in base:
            t_index = base.index(t)
            k_index = base.index(k)
            novo_index = (t_index - k_index) % len(base)
            resultado += base[novo_index]
        else:
            resultado += t  # mantém caractere que não está na base
    return resultado
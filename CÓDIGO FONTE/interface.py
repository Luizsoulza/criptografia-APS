import customtkinter as ctk
from criptografia import criptografar
from descriptografia import descriptografar

ctk.set_appearance_mode('dark')

app = ctk.CTk()
app.title('Criptografia APS')
app.geometry('500x600')

# Funções de ação
def executar_acao():
    opcao = campo_opcao.get()
    texto = campo_texto.get()
    chave = campo_chave.get()

    resultado.delete("1.0", "end")

    if opcao == '1':
        if len(texto) > 1000:
            resultado.insert("end", "Erro: texto muito longo.")
            return
        if not chave:
            resultado.insert("end", "Erro: chave vazia.")
            return

        try:
            criptografado = criptografar(texto, chave)
            resultado.insert("end", criptografado)
        except Exception as e:
            resultado.insert("end", f"Erro na criptografia: {e}")

    elif opcao == '2':
        if not chave:
            resultado.insert("end", "Erro: chave vazia.")
            return

        try:
            descriptografado = descriptografar(texto, chave)
            resultado.insert("end", descriptografado)
        except Exception as e:
            resultado.insert("end", f"Erro na descriptografia: {e}")

    elif opcao == '3':
        app.destroy()
    else:
        resultado.insert("end", "Opção inválida. Escolha 1, 2 ou 3.")

def limpar_campos():
    campo_opcao.delete(0, "end")
    campo_texto.delete(0, "end")
    campo_chave.delete(0, "end")
    resultado.delete("1.0", "end")

def copiar_resultado():
    conteudo = resultado.get("1.0", "end").strip()
    app.clipboard_clear()
    app.clipboard_append(conteudo)

# Interface
label_menu = ctk.CTkLabel(app, text='MENU PRINCIPAL', font=('Arial', 18))
label_menu.pack(pady=10)

label_opcoes = ctk.CTkLabel(app, text='1. Criptografar\n2. Descriptografar\n3. Sair')
label_opcoes.pack(pady=3)

campo_opcao = ctk.CTkEntry(app, placeholder_text='Escolha uma opção:')
campo_opcao.pack(pady=5)

campo_texto = ctk.CTkEntry(app, placeholder_text='Digite o texto para Criptografar ou Descriptografar:', width=400)
campo_texto.pack(pady=5)

campo_chave = ctk.CTkEntry(app, placeholder_text='Digite a chave:', width=400)
campo_chave.pack(pady=5)

botao_executar = ctk.CTkButton(app, text='Executar', command=executar_acao)
botao_executar.pack(pady=10)

botao_limpar = ctk.CTkButton(app, text='Limpar Tudo', command=limpar_campos)
botao_limpar.pack(pady=5)

resultado = ctk.CTkTextbox(app, width=400, height=200)
resultado.pack(pady=10)

botao_copiar = ctk.CTkButton(app, text='Copiar Resultado', command=copiar_resultado)
botao_copiar.pack(pady=5)

app.mainloop()

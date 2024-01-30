import tkinter as tk

def codifica(text, senha):
    texto_codificado = ""
    text = text.upper()
    senha = senha.upper()

    for i, char in enumerate(text):
        if char.isalpha():
            key = senha[i % len(senha)]
            desloc = ord(key) - ord('A')
            if char.isupper():
                char_codificado = chr(((ord(char) - ord('A') + desloc) % 26) + ord('A'))
            else:
                char_codificado = chr(((ord(char) - ord('a') + desloc) % 26) + ord('a'))
            texto_codificado += char_codificado
        else:
            texto_codificado += char

    return texto_codificado



def decodifica(texto_codificado, senha):
    texto_decodificado = ""
    senha = senha.upper()

    for i, char in enumerate(texto_codificado):
        if char.isalpha():
            key = senha[i % len(senha)]
            desloc = ord(key) - ord('A')
            if char.isupper():
                char_decodificado = chr(((ord(char) - ord('A') - desloc) % 26) + ord('A'))
            else:
                char_decodificado = chr(((ord(char) - ord('a') - desloc) % 26) + ord('a'))
            texto_decodificado += char_decodificado
        else:
            texto_decodificado += char

    return texto_decodificado

def botao_codificar_clicked():
    text_to_encode = input_text.get("1.0", "end-1c")
    senha = senha_entry.get()
    texto_codificado = codifica(text_to_encode, senha)
    texto_saida.delete("1.0", "end")
    texto_saida.insert("1.0", texto_codificado)

def botao_decodificar_clicked():
    text_to_decode = input_text.get("1.0", "end-1c")
    senha = senha_entry.get()
    texto_decodificado = decodifica(text_to_decode, senha)
    texto_saida.delete("1.0", "end")
    texto_saida.insert("1.0", texto_decodificado)

# Janela principal
root = tk.Tk()
root.title("Cifra de Della Porta")

# Campos de entrada
input_label = tk.Label(root, text="Texto:")
input_text = tk.Text(root, width=40, height=10)
senha_label = tk.Label(root, text="Palavra-chave:")
senha_entry = tk.Entry(root, width=20)
output_label = tk.Label(root, text="Resultado:")
texto_saida = tk.Text(root, width=40, height=10)

# Botões e gatilhos de função
botao_codificar = tk.Button(root, text="Codificar", command=botao_codificar_clicked)
botao_decodificar = tk.Button(root, text="Decodificar", command=botao_decodificar_clicked)

# Posicionamento dos elementos na janela
input_label.grid(row=0, column=0, padx=10, pady=5)
input_text.grid(row=1, column=0, padx=10, pady=5)
senha_label.grid(row=2, column=0, padx=10, pady=5)
senha_entry.grid(row=3, column=0, padx=10, pady=5)
botao_codificar.grid(row=4, column=0, padx=10, pady=5)
botao_decodificar.grid(row=5, column=0, padx=10, pady=5)
output_label.grid(row=6, column=0, padx=10, pady=5)
texto_saida.grid(row=7, column=0, padx=10, pady=5)

root.mainloop()




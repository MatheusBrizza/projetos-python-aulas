'''
2. Faça o botão fechar a janela quando clicado.  
Utilize o método destroy() para fechar a janela principal.
'''
import tkinter as tk

janela = tk.Tk()
janela.title("2. Faça o botão fechar a janela quando clicado.")
botao_destroir = tk.Button(text="Botão para fechar janela", command=janela.destroy)
botao_destroir.pack()

janela.mainloop()
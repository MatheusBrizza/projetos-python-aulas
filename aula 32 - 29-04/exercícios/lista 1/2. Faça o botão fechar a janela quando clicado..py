'''
2. Faça o botão fechar a janela quando clicado.  
Utilize o método destroy() para fechar a janela principal.
'''
import tkinter as tk

janela = tk.Tk()

botao_destroir = tk.Button(text="fechar", command=janela.destroy)
botao_destroir.pack()

janela.mainloop()
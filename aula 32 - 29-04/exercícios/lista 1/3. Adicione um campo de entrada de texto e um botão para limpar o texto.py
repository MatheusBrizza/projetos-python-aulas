'''
3. Adicione um campo de entrada de texto e um botão para limpar o texto.  
O campo de entrada deve permitir que o usuário digite um texto. 
O botão "Limpar" deve apagar o conteúdo do campo de entrada quando 
clicado.
'''
import tkinter as tk

janela = tk.Tk()
janela.title("3. Adicione um campo de entrada de texto e um botão para limpar o texto.")
caixa_texto = tk.Text(janela)
caixa_texto.pack()



janela.mainloop()
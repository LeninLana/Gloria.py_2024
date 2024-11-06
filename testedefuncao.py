from tkinter import *
import customtkinter as ct

tela = ct.CTk()

tela.title('Cadastro de cpf')
tela.geometry('400x250')
'''
def funcao():
    tela_entrada2= []
    for caractere in tela_entrada2():
        
'''

tela_mens1 = Label(tela, text= 'digite seu nome')
tela_mens1.grid(column=0, row=0, padx=10, pady=10)
tela_mens2 = Label(tela, text= 'digite seu cpf')
tela_mens2.grid(column=0, row=1, padx=10, pady=10)
tela_mens3 = Label(tela, text= 'digite seu email')
tela_mens3.grid(column=0, row=2, padx=10, pady=10)
tela_entrada1 = ct.CTkEntry(tela, placeholder_text='ex: Antonio')
tela_entrada1.grid(column=1, row=0, padx=10, pady=10)
tela_entrada2 = ct.CTkEntry(tela, placeholder_text='ex: 12345678910')
tela_entrada2.grid(column=1, row=1, padx=10, pady=10)
tela_entrada3 = ct.CTkEntry(tela, placeholder_text='ex: antonio123@gmail.com')
tela_entrada3.grid(column=1, row=2, padx=10, pady=10)
botao = Button(tela, text='fazer cadastro', command= funcao)
botao.grid(column=0, row=5, padx=10, pady=10)
tela.mainloop()

from tkinter import *
import customtkinter

tela = customtkinter.CTk()

tela.title('Cadastro de cpf')
tela.geometry('400x250')
customtkinter.set_default_color_theme('blue')
customtkinter.set_appearance_mode('dark')

def funcao():
    if tela_entrada == 'sedução':
        print('bananada')
    else:
        print('sem bananada')

tela_mens = Label(tela, text= 'mensagem')
tela_mens.grid(column=0, row=0, padx=10, pady=10)
tela_saida = Label(tela, text = "")
tela_saida.grid(column=0, row=1, padx=10, pady=10)
tela_entrada = Entry(tela, text='texto')
tela_entrada.grid(column=0, row=3, padx=10, pady=10)
botao = Button(tela, text='butão', command= funcao)
botao.grid(column=0, row=5, padx=10, pady=10)
tela_saida['text'] = 'retorno da função'
tela.mainloop()

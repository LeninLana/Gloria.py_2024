#AI QUE NÃO SEI OQ NÃO SEI OQ LÁ
from tkinter import *

def celsius_para_fahrenheit():
        c = float (temperatura.get())
        f = (c * 1.8) + 32
        resultado.config(text=f"{c}°C é igual a {f:.2f}°F")

def fahrenheit_para_celsius():
        f = float(temperatura.get())
        c = (f - 32) * 5/9
        resultado.config(text=f"{f}°F é igual a {c:.2f}°C")

def celsius_para_kelvin():
        c = float(temperatura.get())
        k = c + 273.15
        resultado.config(text=f"{c}°C é igual a {k:.2f}K")

def kelvin_para_celsius():
        k = float(temperatura.get())
        c = k - 273.15
        resultado.config(text=f"{k}K é igual a {c:.2f}°C")

def fahrenheit_para_kelvin():
        f = float(temperatura.get())
        k = (f - 32) * 5/9 + 273.15
        resultado.config(text=f"{f}°F é igual a {k:.2f}K")

def kelvin_para_fahrenheit():
        k = float(temperatura.get())
        f = (k - 273.15) * 9/5 + 32
        resultado.config(text=f"{k}K é igual a {f:.2f}°F")


tela = Tk()
tela.geometry("400x500")

colocar_temperatura = Label(tela, text="Digite a temperatura: ")
colocar_temperatura.grid(column=0, row=0, padx=10, pady=10)

temperatura = Entry(tela)
temperatura.grid(column=1, row=0, padx=10, pady=10)

apertar= Label(tela, text="Aperte a opção")
apertar.grid(column=0, row=1, padx=10, pady=10)


Button(tela, text="1. De Celsius para Fahrenheit", command=celsius_para_fahrenheit).grid(column=0, row=2, sticky=W, padx=10, pady=10)
Button(tela, text="2. De Fahrenheit para Celsius", command=fahrenheit_para_celsius).grid(column=0, row=3, sticky=W, padx=10, pady=10)
Button(tela, text="3. De Celsius para Kelvin"    , command=celsius_para_kelvin    ).grid(column=0, row=4, sticky=W + E, padx=10, pady=10)
Button(tela, text="4. De Kelvin para celsius"    , command=kelvin_para_celsius    ).grid(column=0, row=5, sticky=W + E, padx=10, pady=10)
Button(tela, text="5. De Fahrenheit para Kelvin" , command=fahrenheit_para_kelvin ).grid(column=0, row=6, sticky=W + E, padx=10, pady=10)
Button(tela, text="6. De Kelvin para Fahrenheit" , command=kelvin_para_fahrenheit ).grid(column=0, row=7, sticky=W + E, padx=10, pady=10)

resultado = Label(tela, text="")
resultado.grid(column=0, row=8, padx=10, pady=10)


tela.mainloop()
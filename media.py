
###BIBLIOTECAS###
import tkinter as tk
from tkinter import ttk

###VARIÁVEIS###
notas = []

###JANELA###
janela = tk.Tk()

janela.title("Calculadora de Média")

frame = ttk.Frame(janela, padding="20")
frame.grid()

# Elementos
label = ttk.Label(frame, text="Digite e adicione as notas e clique em 'Calcular Média'")
label.grid(row=0, column=0, pady=(0, 12))

label_notas = ttk.Label

entrada = ttk.Entry(frame, width=20)
entrada.grid(row=2, column=0, pady=(4, 12))

botao = ttk.Button(frame, text="Calcular Média", command=lambda: calculing(notas))
botao.grid(row=3, column=1, pady=(4, 12))

botao_add = ttk.Button(frame, text="Add", command=lambda: add())
botao_add.grid(row=3, column=0, pady=(4, 12))

label = ttk.Label(frame, text="Digite as notas e clique em 'Calcular Média'")
label.grid(row=4, column=0, pady=(0, 12))

###FUNÇÕES###

# Calcular a média
def calculing(notas):
    if len(notas) > 0:
        resultado = sum(notas) / len(notas)
        print(f"soma: {sum(notas)}, quantidade: {len(notas)}, média: {resultado}")
        notas.clear()

        if resultado >= 7:
            print("Aprovado")
        else:
            print("Reprovado")

# Receber as notas
def add():
    try:
        input_nota = float(entrada.get())

        if input_nota < 0 or input_nota > 10:
            print("Nota inválida. Por favor, digite um número entre 0 e 10.")
            
        else:
            notas.append(input_nota)
            label_notas= ttk.Label(frame, text=str(notas))
            label_notas.grid(row=1, column=0, pady=(0, 12))
            
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'calc'.")

janela.mainloop()
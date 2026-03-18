
# Bibliotecas
import tkinter as tk
from tkinter import ttk

# Variáveis
notas = []

###JANELA###
janela = tk.Tk()

janela.title("Calculadora de Média")

frame = ttk.Frame(janela, padding="20")
frame.grid()

# Elementos
label = ttk.Label(frame, text="Digite as notas e clique em 'Calcular Média'")
label.grid(row=0, column=0, pady=(0, 12))

entrada = ttk.Entry(frame, width=20)
entrada.grid(row=1, column=0, pady=(4, 12))

botao = ttk.Button(frame, text="Calcular Média", command=lambda: calculing(notas))
botao.grid(row=2, column=0, pady=(4, 12))

# Função para calcular a média
def calculing(notas):
    resultado = sum(notas) / len(notas)
    print(f"soma: {sum(notas)}, quantidade: {len(notas)}, média: {resultado}")
    notas.clear()
    if resultado >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

# Loop para receber as notas
while True:
    try:
        input_nota = input("Digite uma nota (ou 'calc' para calcular): ")
        if input_nota == 'calc' and len(notas) > 0:
            calculing(notas)

        elif float(input_nota) < 0 or float(input_nota) > 10:
            print("Nota inválida. Por favor, digite um número entre 0 e 10.")
            continue
        else:
            notas.append(float(input_nota))

    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'calc'.")



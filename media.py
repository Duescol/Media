import tkinter as tk
from tkinter import ttk

notas = []

###JANELAS###
janela = tk.Tk() # Cria a janela
janela.title("Calculadora de Média")

frame = ttk.Frame(janela, padding="20")
frame.grid() # Configura a janela

resultado_var = tk.StringVar() #V Variável que mostra os resultados <notas>
notas_var = tk.StringVar(value="Notas: []")

ttk.Label(frame, text="Digite e adicione as notas, depois clique em 'Calcular Média'").grid(
    row=0, column=0, columnspan=2, pady=(0, 12) # Textinho pra ler
)

label_notas = ttk.Label(frame, textvariable=notas_var)
label_notas.grid(row=1, column=0, columnspan=2, pady=(0, 12))

entrada = ttk.Entry(frame, width=20)
entrada.grid(row=2, column=0, columnspan=2, pady=(4, 12))

ttk.Button(frame, text="Add", command=lambda: add()).grid(row=3, column=0, pady=(4, 12))
ttk.Button(frame, text="Calcular Média", command=lambda: calculing(notas)).grid(row=3, column=1, pady=(4, 12))

label_resultado = ttk.Label(frame, textvariable=resultado_var)
label_resultado.grid(row=4, column=0, columnspan=2, pady=(0, 12))

###FUNÇÕES###

def calculing(notas):
    if len(notas) > 0:
        media = sum(notas) / len(notas)
        status = "Aprovado ✓" if media >= 7 else "Reprovado ✗"
        resultado_var.set(f"Média: {media:.2f} — {status}")
        notas.clear()
        notas_var.set("Notas: []")
    else:
        resultado_var.set("Nenhuma nota adicionada.")

def add():
    try:
        input_nota = float(entrada.get())
        if input_nota < 0 or input_nota > 10:
            resultado_var.set("Nota inválida. Digite um número entre 0 e 10.")
        else:
            notas.append(input_nota)
            notas_var.set(f"Notas: {notas}")
            resultado_var.set("")
            entrada.delete(0, tk.END)  # Limpa o campo após adicionar
    except ValueError:
        resultado_var.set("Entrada inválida. Digite um número.")

janela.mainloop()
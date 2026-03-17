
notas = []

def calculing(notas):
    resultado = sum(notas) / len(notas)
    print(f"soma: {sum(notas)}, quantidade: {len(notas)}, média: {resultado}")
    if resultado >= 7:
        print("Aprovado")
    else:
        print("Reprovado")


while True:
    try:
        input_nota = input("Digite uma nota (ou 'sair' para encerrar): ")
        if input_nota == 'sair':
            calculing(notas)

        elif float(input_nota) < 0 or float(input_nota) > 10:
            print("Nota inválida. Por favor, digite um número entre 0 e 10.")
            continue
        else:
            notas.append(float(input_nota))

    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'sair'.")



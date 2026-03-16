
notas = []

def calculing(notas):
    resultado = sum(notas) / len(notas)
    print(f"soma: {sum(notas)}, quantidade: {len(notas)}, média: {resultado}")

while True:
    try:
        input_nota = input("Digite uma nota (ou 'sair' para encerrar): ")
        if input_nota == 'sair':
            calculing(notas)
        else:
            notas.append(float(input_nota))

    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'sair'.")



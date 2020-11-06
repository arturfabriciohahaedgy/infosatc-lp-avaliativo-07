numeroLista = []
for x in range(10):
    numeroInput = int(input("Insira o numero: "))
    numeroLista.append(numeroInput)

numeroLista2 = numeroLista.copy()

filtro = list(filter(lambda x: x % 2 == 0, numeroLista))
filtro2 = list(filter(lambda x: x % 2 != 0, numeroLista2))


print("Numeros Pares: ")
for x in filtro:
    print(x)

print("Numeros Impares: ")
for x in filtro2:
    print(x)



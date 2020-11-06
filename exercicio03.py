numeroLista = []
for x in range(5):
    numeroInput = int(input("Insira o numero: "))
    numeroLista.append(numeroInput)
filtro = list(filter(lambda x: x>10, numeroLista))
print("Numeros filtrados: ")
for x in filtro:
    print(x)
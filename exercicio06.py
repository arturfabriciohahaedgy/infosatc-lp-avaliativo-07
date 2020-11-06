numero = int(input("Insira um numero para ver o quadrado e o triplo: "))
calculo = lambda x: x ** 2
calculo1 = lambda x: x * 3
print("Quadrado do Número:", calculo(numero))
print("Triplo do Número:", calculo1(numero))
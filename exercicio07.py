

notaPrimeira = 6
notaSegunda = 8.5

media = lambda nota1, nota2: (nota1 * 4 + nota2 * 6)/10

def conceito1(nota1, nota2):
    if (media(nota1, nota2)) >= 0 and (media(nota1, nota2)) <= 4.9:
        return "D"
    if (media(nota1, nota2)) >= 5.0 and (media(nota1, nota2)) <= 6.9:
        return "C"
    if (media(nota1, nota2)) >= 7.0 and (media(nota1, nota2)) <= 8.9:
        return "B"
    if (media(nota1, nota2)) >= 9.0 and (media(nota1, nota2)) <= 10.0:
        return "A"  
    
print("Média do aluno:", media(notaPrimeira, notaSegunda))
print("Conceito do aluno:", conceito1(notaPrimeira, notaSegunda))

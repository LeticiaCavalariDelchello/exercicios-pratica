#Exercicio 2 - Realizar a média de 3 notas
def calcula_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

while True:
    try:
        nota1, nota2, nota3 = map(float, input('Digite as 3 notas separadas por espaço: ').split())
        break
    except ValueError:
        print('Digite apenas valores válidos!')


media = calcula_media(nota1, nota2, nota3)
print(f'A média do aluno é: {media:.2f}')


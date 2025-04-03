#Soma de dois números - solicitando os números fora da função
def soma_dois_numeros(num1, num2):
    return num1 + num2

while True:
    try:
        numero1, numero2 = map(float, input('Digite dois números separados por espaço: ').split())
        break
    except ValueError:
        print('Erro: Digite apenas números válidos separados por um espaço.')


soma = soma_dois_numeros(numero1, numero2)
print(f'A soma de {numero1} + {numero2} é: {soma}')


'''
#Soma de dois números - refatorado
def soma_dois_numeros():
    while True:
        try:
            numero1, numero2 = map(float, input('Digite dois números separados por um espaço: ').split())
            return numero1, numero2 #Retornado apenas quando a entrada for válida.
        except ValueError:
            print('Erro: Digite apenas dois números válidos separados por um espaço.')
        

#Chamando a função soma_dois_numeros
numero1, numero2 = soma_dois_numeros()
soma = numero1 + numero2

print(f'A soma de {numero1} + {numero2} é: {soma}')

'''

''' Solução feita pelo chat GPT

def soma_dois_numeros():
    try:
        numero1, numero2 = map(int, input("Digite dois números separados por espaço: ").split())
        soma = numero1 + numero2
        print(f"A soma de {numero1} + {numero2} é: {soma}")
    except ValueError:
        print("Erro: Certifique-se de digitar apenas números inteiros separados por espaço.")

# Chamando a função
soma_dois_numeros()

'''
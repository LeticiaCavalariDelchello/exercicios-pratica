# Exercício dia 4 - Cálculo de área
def calculaArea(base: float, altura: float):
    return base * altura

while True:
    try:
        base = float(input('Digite a base do retângulo: '))
        altura = float(input('Digite a altura do retângulo: '))
        break
    except ValueError:
        print('Erro: Os valores digitados não são válidos, tente novamente.')
        continue


areaRetangulo = calculaArea(base, altura)
print(f'A área do retângulo de base: {base} e altura: {altura} é igual a: {areaRetangulo}')
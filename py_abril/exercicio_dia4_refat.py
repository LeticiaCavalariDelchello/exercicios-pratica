# Exercício dia 4 - Cálculo de área de um retângulo

def calcula_area(base: float, altura: float) -> float:
    """
    Calcula a área de um retângulo.
    Fórmula: área = base * altura
    """
    return base * altura

def obter_valores() -> tuple[float, float]:
    """
    Solicita os valores de base e altura ao usuário, com validação de entrada.
    Retorna uma tupla (base, altura)
    """
    while True:
        try:
            base = float(input('Digite a base do retângulo: '))
            altura = float(input('Digite a altura do retângulo: '))
            return base, altura
        except ValueError:
            print('Erro: Digite apenas valores numéricos válidos.')

def main():
    base, altura = obter_valores()
    area = calcula_area(base, altura)
    print(f'A área do retângulo de base {base} e altura {altura} é: {area:.2f}')

if __name__ == "__main__":
    main()

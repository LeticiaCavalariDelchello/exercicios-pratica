# Exercício dia 3 - Conversão de temperatura (refatorado)

def converte_fahrenheit(celsius: float) -> float:
    """
    Converte uma temperatura de Celsius para Fahrenheit.
    
    Fórmula: F = (9/5) * C + 32
    """
    return (9 / 5) * celsius + 32

def main():
    while True:
        try:
            temp_celsius = float(input('Digite uma temperatura em Celsius: '))
            break
        except ValueError:
            print('Erro: Digite um valor numérico válido.')

    fahrenheit = converte_fahrenheit(temp_celsius)
    print(f'A temperatura correspondente em Fahrenheit é: {fahrenheit:.2f}ºF')

# Executa o programa
if __name__ == "__main__":
    main()

# Exercício dia 3 - Conversão de temperatura
def convertaFarenheit(celsius):
    return (9/5) * celsius + 32


tempCelsius = float(input('Digite uma temperatura em Celsius: '))
farenheit = convertaFarenheit(tempCelsius)

print(f'A temperatura em Fahrenheit é: {farenheit}ºF')

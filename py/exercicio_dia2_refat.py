# Exercício 2 - Calcular a média de 3 notas
def calcula_media(nota1, nota2, nota3):
    """Calcula a média de três notas."""
    return (nota1 + nota2 + nota3) / 3

# Entrada e validação das notas
while True:
    try:
        nota1, nota2, nota3 = map(float, input('Digite as 3 notas separadas por espaço: ').split())
        
        # Verifica se as notas estão no intervalo de 0 a 10
        if any(nota < 0 or nota > 10 for nota in [nota1, nota2, nota3]):
            print("Erro: Todas as notas devem estar entre 0 e 10.")
            continue  # Pede novamente os valores se estiverem errados
        
        break  # Sai do loop se as notas forem válidas
    except ValueError:
        print('Erro: Digite apenas valores numéricos válidos!')

# Calcula e exibe a média
media = calcula_media(nota1, nota2, nota3)
print(f'A média do aluno é: {media:.2f}')

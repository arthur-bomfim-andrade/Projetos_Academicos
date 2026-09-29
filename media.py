#calculadora de média
def calcular_média(nota1, nota2):
    return (nota1 + nota2)/2
print("=== Sistema de Notado Aluno ===")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = calcular_média(n1,n2)
print(f"A média final é: {media:.2f}")
if media >= 7.0:
    print("Aprovado!")
else:
    print("Reprovado!")

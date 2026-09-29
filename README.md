# 🧮 Calculadora de Média

Um programa simples em **Python** que calcula a média de duas notas de um aluno e informa se ele foi aprovado ou reprovado.

## 📌 Funcionalidades

- Recebe duas notas do usuário.
- Calcula a média das notas.
- Exibe a média final com duas casas decimais.
- Informa se o aluno foi aprovado ou reprovado.

## 🛠️ Tecnologias

- Python 3

## 🚀 Como executar

1. Instale o Python 3.
2. Clone ou baixe este projeto.
3. Abra a pasta do projeto no VS Code.
4. Execute o arquivo:

## 🗣️ Exemplo de uso

```#calculadora de média
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
```

```=== Sistema de Notado Aluno ===
Digite a primeira nota: 10
Digite a segunda nota: 5 
A média final é: 7.50
Aprovado!
```


```bash
python calculadora_media.py

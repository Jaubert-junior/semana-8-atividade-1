#entrada de dados
num1 = int(input().strip())
num2 = int(input().strip())
num3 = int(input().strip())
num4 = int(input().strip())
num5 = int(input().strip())
numeros =[ num1 , num2 , num3 , num4 ,num5]

#processamento
soma = sum(numeros)
media = soma / len(numeros)

#saída de dados
print(f"{media:.2f}")
if num1 > media :
    print(f"{num1:.2f}")

if num2 > media :
    print(f"{num2:.2f}")

if num3 > media :
    print(f"{num3:.2f}")

if num4 > media :
    print(f"{num4:.2f}")

if num5 > media :
    print(f"{num5:.2f}")
 

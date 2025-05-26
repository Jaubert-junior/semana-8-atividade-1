#entrada de dados
peso = float(input().strip())
altura = float( input().strip())

#processamento e saída de dados
imc = peso / (altura * altura)
print(f"{imc:.2f}")
if imc < 18.5 :
    print("Abaixo do peso")
elif imc < 25 :
    print("Peso normal")
elif imc < 30 :
    print ("Sobrepeso")
elif imc <35 :
    print ("obeso leve")
elif imc < 40 :
    print ("Obeso moderado")
elif imc >= 40 :
    print ("Obeso mórbido")


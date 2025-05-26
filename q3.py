#entrada de dados
num1 = int(input().strip())
num2 = int(input().strip())
num3 = int(input().strip())
num4 = int(input().strip())
num5 = int(input().strip())

#processamento e saída de dados
if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5 :
    print(num1)
else :
    if num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5 :
        print(num2) 
    else :
        if num3 >= num1 and num3 >= num2 and num3 >= num4 and num2 >= num5 :
            print(num3) 
        else :
            if num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5 :
                print(num4) 
            elif num5 >= num1 and num5 >= num2 and num5 >= num3 and num5 >= num4 :
                print(num5) 

if num1 <= num2 and num1 <= num3 and num1 <= num4 and num1 <= num5 :
    print(num1)
else :
    if num2 <= num1 and num2 <= num3 and num2 <= num4 and num2 <= num5 :
        print(num2) 
    else :
        if num3 <= num1 and num3 <= num2 and num3 <= num4 and num3 <= num5 :
            print(num3) 
        else :
            if num4 <= num1 and num4 <= num2 and num4 <= num3 and num4 <= num5 :
                print(num4) 
            elif num5 <= num1 and num5 <= num2 and num5 <= num3 and num5 <= num4 :
                print(num5) 




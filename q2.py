#entrada de dados
dia1 = int(input().strip())
mes1 = int(input().strip())
ano1 = int(input().strip())
data1 = (f"{dia1}/{mes1}/{ano1}")

dia2 = int(input().strip())
mes2 = int(input().strip())
ano2 = int(input().strip())
data2 = (f"{dia2}/{mes2}/{ano2}")
#processamento e saída de dados
if ano1 > ano2:
        print(data1)
elif ano2 > ano1:
        print(data2)
else:  
        if mes1 > mes2:
            print(data1)
        elif mes2 > mes1:
            print(data2)
        else:  
            if dia1 > dia2:
                print(data1)
            elif dia2 > dia1:
                print(data2)
            else:
                print(data1)






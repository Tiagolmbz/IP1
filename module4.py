terminos = 5
serie=0
cont=0
for i in range(1,terminos+1):
    if cont < 1:
        serie +=1/1
        print("+")
    else:
        serie -=1/1
        print("-")
    cont=cont+1
    if cont==4:
        cont=0
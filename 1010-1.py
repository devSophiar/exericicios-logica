def temperatura(lista, origem, destino):
    if origem=='C' and destino=='F':
        return [(temp*9/5)+32 for temp in lista]
    elif origem=="F" and destino=="C":
        return[(temp - 32) * 5/9 for temp in lista]
    else: 
        print('invalido')

celsius=[10,15,35,80]
fahrenheit= temperatura(celsius, "C", "F")
print("fahrenheit", fahrenheit)

fahrenheit=[10,15,35,80]
celsius= temperatura(celsius, "F", "C")
print("celsius", celsius)

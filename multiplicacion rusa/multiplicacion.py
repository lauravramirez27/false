multiplicador=int(input("Ingrese multiplicador: "))
multiplicando=int(input("Ingrese multiplicando: "))

ador=[multiplicador]
ando=[multiplicando]

cantidad=len(ador)
valor=multiplicador
ador.append(valor)
ador.split(",")
while valor!=1:
    print(valor,"2")
    valor=valor/2
    print(valor)
    ador.append(valor)
    valor=ador[cantidad-1]
    print(valor)



print(ador)



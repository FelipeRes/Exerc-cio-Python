lata = 360
garrafa = 600
garrafa2 = 2000
qntL = 0
qntG = 0
qntG2 = 0

def valorArrecadado(p,m,g):
    return p * lata + m * garrafa + g * garrafa2


while 1==1:
    try:
        qntL = int(input('Informe o numero de latas(360ml):\n'))
        break
    except ValueError:
        print ("entrada invalida!")
while 1==1:
    try:
        qntG = int(input('Informe o numero de garrafa(600ml):\n'))
        break
    except ValueError:
        print ("entrada invalida!")
while 1==1:
    try:
        qntG2 = int(input('Informe o numero de garrafa(2 litros):s\n'))
        break
    except ValueError:
        print ("entrada invalida!")
        
print ("Total de camisas: ",valorArrecadado(qntL,qntG,qntG2)/1000, " Litros")

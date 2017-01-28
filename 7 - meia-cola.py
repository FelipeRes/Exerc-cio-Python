pequena = 10
media = 12
grande = 15
qntP = 0
qntM = 0
qntG = 0

def valorArrecadado(p,m,g):
    return p*pequena+m*media+g*grande


while 1==1:
    try:
        qntP = int(input('Informe o numero de camisas pequenas\n'))
        break
    except ValueError:
        print ("entrada invalida!")
while 1==1:
    try:
        qntM = int(input('Informe o numero de camisas medias\n'))
        break
    except ValueError:
        print ("entrada invalida!")
while 1==1:
    try:
        qntG = int(input('Informe o numero de camisas grandes\n'))
        break
    except ValueError:
        print ("entrada invalida!")
        
print ("Total de camisas: ",valorArrecadado(qntP,qntM,qntG))

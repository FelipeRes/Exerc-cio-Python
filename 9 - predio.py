

def calcularAltura(sombra,minhaSombra, minhaAltura):
    return sombra/minhaSombra*minhaAltura

s =0;
ms = 0;
ma = 0;
while 1==1:
    try:
        s = float(input('Digite o comprimento da sombra do prédio:\n'))
        break
    except ValueError:
        print ("entrada invalida!")
while 1==1:
    try:
        ms = float(input('Digite o comprimento da sua sombra:\n'))
        break
    except ValueError:
        print ("entrada invalida!")
while 1==1:
    try:
        ma = float(input('Digite a sua altura:\n'))
        break
    except ValueError:
        print ("entrada invalida!")
print("Altura do predio: ", calcularAltura(s,ms,ma));
    

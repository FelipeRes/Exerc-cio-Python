anelChip = 4
anelAlimento = 3.5

qntFrangos = 0
while 1==1:
    try:
        qntFrangos = int(input("Insira a quantidade de frangos:\n"))
        break
    except ValueError:
        print("Entrada invalida")

total = qntFrangos*(anelChip+anelAlimento*2)
print("Custo Total: ", total) 

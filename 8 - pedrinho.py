Moeda1 = 1
Moeda2 = 5
Moeda3 = 10
Moeda4 = 25
Moeda5 = 50
Moeda6 = 100

q1=0
q2=0
q3=0
q4=0
q5=0
q6=0

while 1==1:
    try:
        q1 = int(input('Quantidade de moedas de 1 centavo:\n'))
        break
    except ValueError:
        print ("entrada invalida!")
while 1==1:
    try:
        q2 = int(input('Quantidade de moedas de 5 centavos:\n'))
        break
    except ValueError:
        print ("entrada invalida!")

while 1==1:
    try:
        q3 = int(input('Quantidade de moedas de 10 centavos:\n'))
        break
    except ValueError:
        print ("entrada invalida!")

while 1==1:
    try:
        q4 = int(input('Quantidade de moedas de 25 centavos:\n'))
        break
    except ValueError:
        print ("entrada invalida!")

while 1==1:
    try:
        q5 = int(input('Quantidade de moedas de 50 centavos:\n'))
        break
    except ValueError:
        print ("entrada invalida!")

while 1==1:
    try:
        q6 = int(input('Quantidade de moedas de 1 real:\n'))
        break
    except ValueError:
        print ("entrada invalida!")

valorTotal = q1*Moeda1 + q2*Moeda2 + q3*Moeda3 + q4*Moeda4 + q5*Moeda5 + q6*Moeda6
print ("Total em reais: ", valorTotal/100, "R$")

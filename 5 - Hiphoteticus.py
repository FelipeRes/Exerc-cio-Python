horaNormal = 10
horaExtra = 15

qntHoras = 0
qntExtras = 0
while 1==1:
    try:
        qntHoras = int(input("Insira a quantidade de horas trabalhadas:\n"))
        break
    except ValueError:
        print("Entrada invalida")

while 1==1:
    try:
        qntExtras = int(input("Insira a quantidade de horas extras:\n"))
        break
    except ValueError:
        print("Entrada invalida")

salarioBruto = qntHoras*horaNormal+qntExtras*horaExtra
salarioLiquido = salarioBruto-(salarioBruto/100*10)
print ("Salario bruto: ", salarioBruto)
print ("Salario liquido: ", salarioLiquido)
                             

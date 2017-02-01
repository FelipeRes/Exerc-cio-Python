#2
def Dois(valor):
    return valor/100*70
#3
def Tres(minutos):
    horas = minutos//60
    m = minutos-horas*60
    return ({"horas":horas, "minutos":m})
#4
def Quatro(minutos):
    horas = minutos//60
    m = minutos-horas*60
    return ({"horas":horas, "minutos":m})
#5
def Cinco(velocidade):
    return velocidade*3.6

#6
def Seis(velocidade):
    return velocidade/3.6

#7
def Sete(num1, num2):
    return (num1+num2)/(num1-num2)

#8
def Oito(A,B):
    return (A//B, A%B)

#9
def Nove(valor):
    return ({"Antecessor:":valor-1, "Sucessor":valor+1})

#10
def Dez(x):
    return x*3

#11
def Onze(nome,endereco,telefone):
    return ({"Nome: ":nome," Endereco: ": endereco," Telefone: ":telefone})

#12
def Doze(A,B,C,D):
    return (A+B*2+C*3+D*4)/10

#13
def Treze(valor):
    return 2013-valor

#14
def Quatorze(valor):
    num = str(valor)
    return num[len(num)-2]

#15
def Quinze(valor):
    C = valor//100
    valor -= C*100
    D = valor//10
    valor -= D*10
    U = valor
    return(U*100+D*10+C)

#16
def Dezeseis(valor):
    area = valor*valor
    perimetro = valor*4
    return ({"area":area,"perimetro":perimetro})
#17
def Dezesete(valor, desconto):
    return valor/100*desconto

#18
def Dezoito(A,B):
    B = A+B
    A = B-A
    B = B-A
    return (A, B)

#19
def Dezenove(valor):
    qntHoras = valor//100
    minutos = valor-(qntHoras*100)
    return qntHoras*60+minutos

#20
def Vinte(valor):
    notas50 = valor//50
    valor = valor%50
    
    notas10 = valor//10
    valor = valor%10
    
    notas5 = valor//5
    valor = valor%5
    
    notas1 = valor//1
    valor = valor%1
    
    return ("%d notas de 50R$\n%d notas de 10R$\n%d notas de 5R$\n%d notas de 1R$") % (notas50, notas10,notas5, notas1)

print (Tres(420))

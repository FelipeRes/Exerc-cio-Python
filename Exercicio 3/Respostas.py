import datetime

def Mensagem():
    x = 10
    y = 1
    x -= 1
    y += 2
    x = x - 1
    y = y + 2
    x = x - 1
    y = y + 2
    if x > y:
        return "x ficou maior que y"
    elif x < y:
        return "x ficou menor que y"
    else:
        return "x e y ficaram iguais"

def TesteIf(L1, L2, L3):
    letras = '';
    if L1 == 'V':
        letras = letras + 'A'
    else:
        if L2 == 'V':
             if L3 == 'V':
                 letras = letras + 'B'
             else:
                 letras = letras + 'C'
                 letras = letras + 'D'
    letras = letras + 'E'
    return letras
#Deve ser digitado apenas V ou F para leitura dos valores
La = input("Digite uma letra: ")
Lb = input("Digite uma letra: ")
Lc = input("Digite uma letra: ")
print(TesteIf(La, Lb, Lc))

#a)AE
#b)CDE
#c)BE
#d)FFF


def tres(x,y):
    if(x > y):
        return x
    elif(x<y):
        return y
    else:
        return 0
    
def quatro(x,y,z):
    l = {x,y,z}
    l = sorted(l)
    return l

def cinco(x):
    if(x%2 > 0):
        return False
    else:
        return True

def seis(valor):
    if(valor >20):
        print("Vá ao cinema")
    else:
        print("Fique assistindo TV")

def sete(nome, sexo):
    s = 'ilm'
    if(sexo == 'masculino'):
        s += 'o Sr. '
    if(sexo == 'feminino'):
        s += 'a Sra.'
    s += nome
    s += ' Bem vindo a programação python.'
    return s

def oito(x):
    if(x>0):
        return 'positivo'
    elif(x<0):
        return 'negativo'
    elif(x==0):
        return 0

def nove(x):
    if(x%5 == 0):
        return 'verdadeiro'
    else:
        return 'falso'

def dez(distancia, tempo):
    v = distancia/tempo
    return str(v)+" km/h"

def onze(temp):
    if(temp > 36.6):
        return 'Esta com febre'
    else:
        return 'Sem febre'

def doze(num):
    if(num%7 > 0):
        return 'O numero é multiplo de 7'
    else:
        return 'O número não e multiplo de 8'

def treze(x):
    if(x%2 == 0 and x%3 ==0):
        return 'Verdadeiro'
    else:
        return 'Falso'

def quatorze(ano):
    idade = datetime.datetime.now().year - ano
    if(idade >= 16):
        return 'Pode votar'
    else:
        return 'Não pode'

def quinze(letra):
    vogais = {'a','e','i','o','u'}
    if(letra in vogais):
        return True
    else:
        return False

def dezesseis(num):
    if(num > 12 or num <= 0):
        return 'Valor não corresponde a nenhum mes'
    else:
        a = ('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Oututbro','Novembro','Dezembro')
        return a[num-1]

def dezesete(x,y):
    if(x%2==0 and y%2==0):
        return 'Os dois são pares'
    elif(x%2!=0 and y%2!=0):
        return 'Os dois são impares'
    elif(x%2==0 and y%2!=0):
        return 'O primeiro é par e o segundo é impar'
    elif(x%2!=0 and y%2==0):
        return 'O primeiro é impar e o segundo é par'

def dezoito(x,y,z):
    return quatro(x,y,z)[2]

def dezenove(sinal):
    if(sinal =='V'):
        return 'Siga'
    elif(sinal == 'E'):
        return 'Pare'
    elif(sinal == 'A'):
        return 'Atenção'

def vinte(massa, altura):
    imc = massa/(altura*altura)
    if(imc <18.5):
        return str(imc) + '>' + 'Abaixo do peso'
    if(imc < 25):
        return str(imc) + '>' + 'Peso normal'
    if(imc <30):
        return str(imc) + '>' + 'Sobre peso'
    if(imc < 35):
        return str(imc) + '>' + 'Obeso levo'
    if(imc < 40):
        return str(imc) + '>' + 'Obeso moderado'
    if(imc >= 40):
        return str(imc) + '>' +'Obeso morbido'


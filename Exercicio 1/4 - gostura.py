queijo = 50
presunto = 50
hamburguer = 100

qntHamburger = 0
while 1==1:
    try:
        qntHamburger = int(input("Insira o numero de hamburguers:\n"))
        break
    except ValueError:
        print("Valor invalido!")
        
qntQueijo = qntHamburger*queijo*2
qntPresunto = qntHamburger*presunto
qntHamburguer = qntHamburger*hamburguer
print ("Total em kilos a comprar de queijo: ", qntQueijo/1000, " KG")
print ("Total em kilos a comprar de presunto: ", qntPresunto/1000, " KG")
print ("Total em kilos a comprar de Hamburguer: ", qntHamburguer/1000, " KG")




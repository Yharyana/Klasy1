import random
from shop.store import *
#class product:
#    pass
#ziemniak=product()
#ogurek=product()
#chlep=product()
#print(type(ziemniak))
#lista_produktow={
 #   ziemniak:type(ziemniak)
#}
#print(lista_produktow)


apple1=Apple("sweet",",medium",4.20)
potato1=Potato("sweet",",medium",4.20)
produkt1=Product("japka","warzywa",12)
order1=Order("jakub","dec",[produkt1,produkt1,produkt1])



losowa_order=Order("marcin","smith",)
def creat_random():
    rand=random.randint(1,10)
    for i in range(rand):
        losowa_order.list.append(i)

if __name__=='__main__':
    wypisanie_produktu(produkt1)
    wypisanie_order(order1)


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
class Product:
    def __init__(self,name,name_of_category,price):
        self.name=name
        self.name_of_category=name_of_category
        self.price=price
class Order:
    def __init__(self,name,surrname,list=False):

        self.surrname = surrname
        self.name = name
        if list==False:
            list=[]
        self.list = list
        whole_price=sum(list)
        self.whole_price = whole_price
class Apple:
    def __init__(self,gatunek,rozmiar,price_per_kg):
        self.rozmiar=rozmiar
        self.price_per_kg = price_per_kg
        self.gatunek = gatunek

class Potato:
    def __init__(self,gatunek,rozmiar,price_per_kg):
        self.rozmiar=rozmiar
        self.price_per_kg = price_per_kg
        self.gatunek = gatunek

apple1=Apple("sweet",",medium",4.20)
potato1=Potato("sweet",",medium",4.20)
produkt1=Product("japka","warzywa",12)
order1=Order("jakub","dec",[12,3,4])

def wypisanie(Order):


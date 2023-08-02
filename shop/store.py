class Product:
    def __init__(self,name,name_of_category,price):
        self.name=name
        self.name_of_category=name_of_category
        self.price=price
class Order:
    def __init__(self,name,surrname,list=None):

        self.surrname = surrname
        self.name = name
        if list==None:
            list=[]
        self.list = list
        whole_price=0
        for products in list:
            whole_price+=products.price
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
def wypisanie_produktu(Product):
    print("nazwa produktu",Product.name,"\n","nazwa kateogri",Product.name_of_category,"\n","cena",Product.price)
def wypisanie_order(Order):
    napis=""
    for products in Order.list:
        napis+=","+products.name
    print(napis,Order.name,Order.whole_price,Order.surrname)

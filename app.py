from enum import Enum


class Actions(Enum):
    SHOW_PRODUCTS = 1
    ADD_2_CART = 2
    SHOW_CART=3
    EXIT=5


class Product:
    def __init__(self,name,price = 0,cont=0) -> None:
        self.name = name
        self.price = price
        self.cont = cont

    def __str__(self) -> str:
        return f'{self.name} , price: {self.price} , cont: {self.cont}'

    def buy (self):
        self.cont = self.cont - 1

   

products = []
cart = []


def add_first():
    products.append(Product('apple', 5,10))
    products.append(Product('ball', 10,10))
    products.append(Product('orange', 7,10))
    products.append(Product('balone', 2,100))

def menu():
    while True:
        for act in Actions:
            print(f'{act.name} - {act.value}')
        user_selection = Actions(int(input("enter your selection:")))
        if user_selection == Actions.SHOW_PRODUCTS:
            for prd in products: print(prd)
        if user_selection == Actions.ADD_2_CART: add2cart()
        if user_selection == Actions.SHOW_CART: show_cart()
        if user_selection == Actions.EXIT: return

def search():
    prd2search = input('enter product:')
    for prd in products:
        if prd.name == prd2search: return prd

def add2cart():
    prd2buy = search()
    if prd2buy:
        quantity = int(input(f"Enter the quantity of {prd2buy.name} you want to buy: "))
        if 1 <= quantity <= prd2buy.cont:
            prd2buy.cont -= quantity
            cart.append(Product(prd2buy.name, prd2buy.price, quantity))
            print(f"Added {quantity} {prd2buy.name} to the cart.")
        else:
            print(f"Invalid quantity. Available quantity: {prd2buy.cont}")
    else:
        print("Product not found.")


def show_cart():
    total_price = 0
    for prd in cart:
        print(prd)
        total_price += prd.price * prd.cont
    print("Total Price of Cart:", total_price)


        


if __name__ == '__main__':
    add_first()
    menu()
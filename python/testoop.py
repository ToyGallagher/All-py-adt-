'''
class Menu:
    def __init__(self):
        self.menu_choice = "B"
        self.meal_choice = "R"
        self.burger = {
            "R" : ("regular burger",60),
            "C" : ("chesse burger",75),
            "D" : ("double burger",90)
        }
        self.chicken = {
            'F': ("Fried Chicken", 120),
            'G': ("Grilled Chicken", 150),
            'C': ("Chef's Chicken", 180)
        }
        self.pasta = {
            'S': ("Spaghetti de Italiano", 90),
            'L': ("Lasagna Supreme", 120),
            'M': ("Macaroni Special", 100)
        }
    def display_main_menu(self):
        print("---<< Main Menu >>---")
        print("    <B>urger Meal    ")
        print("    <C>hicken Meal   ")
        print("    <P>asta Meal     ")
    def display_burger_menu(self) -> None:
        print("---<< Burger Sub Menu >>---")
        print("    <R>egular Burger       ")
        print("    <C>heese Burger        ")
        print("    <D>ouble Cheese Burger ")

    def display_chicken_menu(self) -> None:
        print("---<< Chicken Sub Menu >>---")
        print("    <F>ried Chicken         ")
        print("    <G>rilled Chicken       ")
        print("    <C>hef's Chicken        ")

    def display_pasta_menu(self) -> None:
        print("---<< Pasta Sub Menu >>---")
        print("    <S>paghetti de Italiano")
        print("    <L>asagna Supreme      ")
        print("    <M>acaroni Special     ")
    def get_menu_choice(self):
        self.menu_choice = input("Enter your choice: ")
    def get_meal_choice(self):
        self.meal_choice = input("Enter your choice: ")
    def set_menu_choice(self):
        return self.menu_choice
    def set_meal_choice(self):
        return self.meal_choice
    def get_result(self):
        if self.menu_choice == "B":
            return self.burger[self.meal_choice]
        elif self.menu_choice == "C":
            return self.chicken[self.meal_choice]
        elif self.menu_choice == "P":
            return self.pasta[self.meal_choice]
def process():
    food_menu = Menu()
    food_menu.display_main_menu()
    food_menu.get_menu_choice()
    menu_choice = food_menu.set_menu_choice()

    if menu_choice == 'B':
        food_menu.display_burger_menu()
    if menu_choice == 'C':
        food_menu.display_chicken_menu()
    if menu_choice == 'P':
        food_menu.display_pasta_menu()
    food_menu.get_meal_choice()
    name,price = food_menu.get_result()
    print(f"Your {name} is {price} Baht.")
process()
'''
'''
class cal:
    def __init__(self):
        self.tv = 6000
        self.dvd = 1500
        self.audio = 3000
    def set_stock(self):
        self.stock_tv = int(input("How many TVs? ")) 
        self.stock_dvd = int(input("How many DVD players? "))
        self.stock_audio = int(input("How many Audio Systems? "))
    def get_pricetv(self):
        return self.stock_tv*self.tv
    def get_pricedvd(self):
        return self.stock_dvd*self.dvd
    def get_priceaudio(self):
        return self.stock_audio*self.audio
    def sumprice(self):
        self.result = (self.stock_tv*self.tv)+(self.stock_dvd*self.dvd)+(self.stock_audio*self.audio)
        print(f"Total price is {self.result}") 
    #def show(self):
        #print(f"Total price is {self.result}") 
    def process(self):
        if self.result > 24000:
            print(f"You've got a discount of {self.result*(20/100)} baht.")
            print(f"Your payment is {self.result-(self.result*(20/100))} baht. Thank you!")
        else:
            print(f"Your payment is {self.result} baht. Thank you!")
x = cal()
x.set_stock()
x.sumprice()
x.process()
'''
'''
class Item:
    def __init__(self,id,type,price):
        self.id = id
        self.type = type
        self.price = price
    def __str__(self):
        return f' id : {self.id}, type : {self.type}, price : {self.price}'
    def get_id(self):
        return self.id
    def getType(self):
        return self.type
    def getPrice(self):
        return self.price
def idExist(id,res):
    if id == res.get_id():
        return True
def whatisId(id,res):
    return res.getType()
def whatisPrice(id,res):
    return res.getPrice()

def getInput():
    #item_dict = {}
    total_item = int(input("How many products are there? : "))
    for i in range(total_item):
        temp_id,temp_type,temp_price = input().split()
        item_temp = Item(temp_id,temp_type,temp_price)
        #item_dict[temp_id] = item_temp #item_dict[123] = class Item
    return item_temp #item_dict  

def mainLoop(res):
    CONT = True
    while CONT:
        id = input("Id : ")
        if id == res.get_id():
            print("This id doesn't exist.")
        else:
            while True:
                q = int(input("Q : "))
                if q == 1:
                    print(whatisId(id, res))
                elif q == 2:
                    print(whatisPrice(id, res))
                elif q == 3:
                    break
                elif q == 0:
                    CONT =False
                    break
res = getInput()
mainLoop(res)
'''


  
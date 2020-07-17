class Animal:
    def __init__(self,weight, price):
        self.weight = weight
        self.price = price

class No_fly(Animal):
    fly_status = False
    
class Yes_fly(Animal):
    fly_status = True
    



class Cow(No_fly):
    name = "Cow"

class Goat(No_fly):
    name = "Goat"


class Guse(Yes_fly):
    name = "Guse"

class Chick(Yes_fly):
    name = "Chick"

animal_test = Cow(10, 25)
second_animal_test = Guse(0,0)


print(animal_test.name, animal_test.fly_status)


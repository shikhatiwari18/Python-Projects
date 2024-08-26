class house:
    house_type = 'Rented_House'
    def __init__(self,floors,rooms,price):
        self.floors = floors
        self.rooms = rooms
        self.price = price
home = house(1,3,3300000)   
print(type(home))   
print(home.floors)   
print(home.rooms)
print(home.price)   
home.price = 2200
print(home.price)
home.bathrooms =4
print(home.bathrooms)
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("Название ресторана: " + self.restaurant_name + ", кухня: " + self.cuisine_type)
    def open_restaurant(self):
        print("Ресторан открыт")
def p1():
    newRestaurant = Restaurant("Rest1", "русская")
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def p2():
    name = input("Введите название ресторана: ")
    kuh = input("Введите кухню: ")
    newRestaurant1 = Restaurant(name, kuh)
    newRestaurant1.describe_restaurant()

    name = input("Введите название ресторана: ")
    kuh = input("Введите кухню: ")
    newRestaurant2 = Restaurant(name, kuh)
    newRestaurant2.describe_restaurant()

    name = input("Введите название ресторана: ")
    kuh = input("Введите кухню: ")
    newRestaurant3 = Restaurant(name, kuh)
    newRestaurant3.describe_restaurant()
    
def p3():
    class NRestaurant(Restaurant):
        def change_reyt(self):
            r = input("Введите новый рейтинг: ")
            self.reyt = r

    newRestaurant = NRestaurant("Rest1", "русская")
    newRestaurant.reyt = "1"
    print("Старый рейтинг: " + newRestaurant.reyt)
    newRestaurant.change_reyt()
    print("Новый рейтинг: " + newRestaurant.reyt)


p1()
p2()
p3()

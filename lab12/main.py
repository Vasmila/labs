class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Название ресторана: " + self.restaurant_name + ", кухня: " + self.cuisine_type)

def p1():

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors

        def ice_flavors(self):
            print('Вкусы мороженого:')
            print(*self.flavors, sep=',  ')

    newRestaurant = IceCreamStand("Кафе-Мороженое", 'сладости', ['ваниль', 'клубника', 'шоколад'])
    newRestaurant.ice_flavors()
    newRestaurant.describe_restaurant()

def p2():

    class IceCreamStand(Restaurant):
        def __init__(self,restaurant_name, cuisine_type, flavors, place, time):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors
            self.place = place
            self.time = time

        def ice_flavors(self):
            print('Виды мороженного: ')
            print(*self.flavors, sep=',  ')

        def new_flavor(self):
            self.flavors.append(input('Введите новый сорт: '))

        def del_flavor(self):
            self.flavors.remove(input('Введите сорт, который хотите удалить: '))

        def poisk(self):
            if input('Какой вкус хотите найти? ') in self.flavors:
                print('В наличии')
            else:
                print('Нет в наличии')

    class Na_palochke(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, flavors, loc, time, forma):
            super().__init__(restaurant_name, cuisine_type, flavors, loc, time)
            self.forma = forma

        def ice_forma(self):
            print('Форма мороженого:', self.forma)

    newRestaurant1 = IceCreamStand("Кафе-Мороженое", 'сладости', ['ваниль', 'клубника', 'шоколад'], 'ул. Мира', '6:00-18:00')
    newRestaurant1.describe_restaurant()
    newRestaurant1.new_flavor()
    newRestaurant1.ice_flavors()
    newRestaurant1.del_flavor()
    newRestaurant1.ice_flavors()
    newRestaurant1.poisk()

    newRestaurant2 = Na_palochke("Кафе-Мороженое", 'сладости', ['ваниль', 'клубника'], 'Вознесенский пр.', '8:00-22:00', 'овальная')
    newRestaurant2.describe_restaurant()
    newRestaurant2.ice_forma()

import tkinter as tk
def p3():
    class IceCreamStand:
        def __init__(self):
            self.flavors = ['ваниль', 'клубника', 'шоколад', 'манго-маракуя', 'крем-брюле', 'смородина']
            self.types = ['шарик', 'эскимо', 'стаканчик', 'пломбир', 'брикет', 'рожок']

        def get_flavors(self):
            return self.flavors

        def get_types(self):
            return self.types

    class IceCreamStandGUI:
        def __init__(self, master):
            self.master = master
            master.title("Ice Cream Stand")
            root.geometry("490x250")

            self.ice_cream_stand = IceCreamStand()
            self.flavors_label = tk.Label(master, text='Вкусы', font='Arial 18 bold')
            self.flavors_listbox = tk.Listbox(master, font='Arial 16', height=len(self.ice_cream_stand.get_flavors()))

            for flavors in self.ice_cream_stand.get_flavors():
                self.flavors_listbox.insert(tk.END, flavors)

            self.types_label = tk.Label(master, text='Вид', font='Arial 18 bold')
            self.types_listbox = tk.Listbox(master, font='Arial 16', height=len(self.ice_cream_stand.get_types()))

            for type in self.ice_cream_stand.get_types():
                self.types_listbox.insert(tk.END, type)

            self.flavors_label.grid(row=0, column=0)
            self.flavors_listbox.grid(row=1, column=0)
            self.types_label.grid(row=0, column=1)
            self.types_listbox.grid(row=1, column=1)

    root = tk.Tk()
    x = IceCreamStandGUI(root)
    root.mainloop()

p1()
p2()
p3()

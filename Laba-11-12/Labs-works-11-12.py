import tkinter as tk

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating
    
    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Кухня ресторана: {self.cuisine_type}")
        print(f"Рейтинг ресторана: {self.rating}")
    
    def open_restaurant(self):
        print("Ресторан открыт")
    
    def change_rating(self, new_rating):
        self.rating = new_rating
        print(f"Новый рейтинг ресторана: {self.rating}")

new_restaurant = Restaurant("Обжоркин", "Русская кухня")
print(new_restaurant.restaurant_name)
print(new_restaurant.cuisine_type)
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()

#---------------------------------------------------------------------

baffo_restaurant = Restaurant("Баффо", "Итальянская кухня")
sakura_restaurant = Restaurant("Сакура", "Японская кухня")
lost_polos_restaurant = Restaurant("Лос Полос", "латиноамериканская кухня")

baffo_restaurant.describe_restaurant()
sakura_restaurant.describe_restaurant()
lost_polos_restaurant.describe_restaurant()

baffo_restaurant.change_rating(15)
baffo_restaurant.describe_restaurant()


# 12 Лабораторная работа
#---------------------------------------------------------------------
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, location, working_hours, ice_cream_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        self.location = location
        self.working_hours = working_hours
        self.ice_cream_type = ice_cream_type

    
    def show_flavors(self):
        print("Виды мороженного: ")
        for i in self.flavors:
            print(i)
    
    def show_location(self):
        print("Локация: ", self.location)
    
    def show_working_hours(self):
        print("Часы работы: ", self.working_hours)
    
    def add_flavor(self, new_flavor):
        self.flavors.append(new_flavor)
    

    def del_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
        else:
            print("Такого вида мороженного в списке нет!!!")
    
    def is_flover_on_list(self, flavor):
        if flavor in self.flavors:
            print(flavor, "мороженное есть в списке")
        else:
            print("Такого вида мороженного в списке нет!!!")
    

    def add_ice_cream_type(self, ice_type):
        self.ice_cream_type.append(ice_type)
    
    def del_ice_cream_type(self, ice_type):
        if ice_type in self.ice_cream_type:
            self.ice_cream_type.remove(ice_type)
        else:
            print("Такого типа мороженного в списке нет!!!")

    def show_ice_cream_type(self):
        print("Виды типов мороженного: ")
        for i in self.ice_cream_type:
            print(i)

#IceCreamPlace = IceCreamStand("Заморожка", "Десертная кухня", ["Ванильное", "Шоколадное", "Крем брюле", "Фруктовый лёд"], "Г.Тосно", "8:00 - 21:00", [])
#IceCreamPlace.add_ice_cream_type("На палочке")
#IceCreamPlace.add_flavor("Карамельное")
#IceCreamPlace.del_flavor("Ванильное")
#IceCreamPlace.describe_restaurant()
#IceCreamPlace.show_flavors()
#IceCreamPlace.show_location()
#IceCreamPlace.show_working_hours()
#IceCreamPlace.is_flover_on_list("Шоколадное")
#IceCreamPlace.show_ice_cream_type()




#12.3
#---------------------------------------------------------------------
class IceCreamStand:
    def __init__(self, restaurant_name, cuisine_type, flavors, raiting = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = flavors
        self.raiting = raiting
  
    def add_flavor(self, new_flavor):
        self.flavors.append(new_flavor)
    
    def del_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
        else:
            print("Такого вида мороженного в списке нет!!!")
    
ice_cream_stand = IceCreamStand("Марыга Боба", "Мороженное", ["Ванильное", "Шоколадное", "Крем брюле", "Фруктовый лёд"], 1.3)

def add_flavor_to_list():
    input_text = add_flavor_widget.get()
    if input_text:
        ice_cream_stand.add_flavor(input_text)
        list_box.insert(tk.END, str(input_text))
        add_flavor_widget.delete(0, tk.END)

def del_flavor_from_list():
    list_box_items = list_box.get(0, tk.END)
    input_text = del_flavor_widget.get()
    if input_text:
        if input_text in list_box_items:
            ice_cream_stand.del_flavor(input_text)
            list_box.delete(list_box_items.index(input_text))
            del_flavor_widget.delete(0, tk.END)



main_window = tk.Tk()
main_window.title("Интерфейс магазина мороженного")
main_window.geometry("800x600")

label = tk.Label(main_window, text=ice_cream_stand.restaurant_name, font = ("Arial", 24, "bold"))
label.place(x=100, y=50, width=300, height=100)

label = tk.Label(main_window, text=f"Рейтинг: {ice_cream_stand.raiting}", font = ("Arial", 16))
label.place(x=500, y=50, width=300, height=100)

list_box = tk.Listbox(main_window, font = ("Arial", 12, "bold"))
for i in ice_cream_stand.flavors:
    list_box.insert(tk.END, str(i))
list_box.place(x=145, y=130, width=300, height=300)

add_flavor_widget = tk.Entry(main_window, font = ("Arial", 20))
add_flavor_widget.place(x=550, y=130, width=200, height=50)

add_butoon = tk.Button(main_window, text="Добавить", font = ("Arial", 16), command=add_flavor_to_list)
add_butoon.place(x=550, y=200, width=200, height=50)

del_flavor_widget = tk.Entry(main_window, font = ("Arial", 20))
del_flavor_widget.place(x=550, y=280, width=200, height=50)

del_button = tk.Button(main_window, text="Удалить", font = ("Arial", 16), command=del_flavor_from_list)
del_button.place(x=550, y=350, width=200, height=50)

main_window.mainloop()
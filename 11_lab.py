def p1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name}, кухня: {self.cuisine_type} итальянская")

        def open_restaurant(self):
            print("Ресторан открыт")

    newRestaurant = Restaurant("Кентуки","")
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)

    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def p2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant1(self):
            print(f"Название ресторана {self.restaurant_name}, кухня: {self.cuisine_type}")

        def open_restaurant(self):
            print("Ресторан открыт")

    newRestaurant1 = Restaurant(input("Введите название ресторана"), input("Введите тип ресторана"))
    newRestaurant2 = Restaurant(input("Введите название ресторана"), input("Введите тип ресторана"))
    newRestaurant3 = Restaurant(input("Введите название ресторана"), input("Введите тип ресторана"))

    newRestaurant1.describe_restaurant1()
    newRestaurant2.describe_restaurant1()
    newRestaurant3.describe_restaurant1()

def p3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, restaurant_points):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.restaurant_points = restaurant_points


        def new_points(self, new_points):
            self.restaurant_points = new_points



        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name}, кухня: {self.cuisine_type} , рейтинг:{self.restaurant_points}")

        def open_restaurant(self):
            print("Ресторан открыт")

    newRestaurant = Restaurant(input("Введите название ресторана"), input("введите кухню"), input("введите рейтинг ресторана"))

    newRestaurant.describe_restaurant()
    newRestaurant.new_points(input("введите новый рейтнг"))
    newRestaurant.describe_restaurant()
p2()




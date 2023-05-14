def p1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name}, кухня: {self.cuisine_type} итальянская")

        def open_restaurant(self):
            print("Ресторан открыт")
    class IceCreamStand:
        def
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("Имя ресторана " + self.restaurant_name.title() + ", кухня " + self.cuisine_type)
    def open_restaurant(self):
        print("Ресторан " + self.restaurant_name.title() + " открыт!")

restaurant = Restaurant("Буззы рум", "Бурятская")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
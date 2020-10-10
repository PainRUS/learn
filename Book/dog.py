class Dog():
    """Простая модель собаки."""

    def __init__(self, name, age):
        """Инициализирует атрибуты name и age"""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садиться по команде."""
        print(self.name.title() + " сейчас сидит.")

    def roll_over(self):
        """Собака перекатывается по команде."""
        print(self.name.title() + " перекатился!")


my_dog = Dog("Бобик", 6)
your_dog = Dog("Шарик", 3)
print("Мою собаку зовут " + my_dog.name.title() + ".")
print("Моей собаке " + str(my_dog.age) + " лет.")
my_dog.sit()

print("\nТвою собаку зовут " + your_dog.name.title() + ".")
print("Твоей собаке " + str(your_dog.age) + " лет.")
your_dog.sit()


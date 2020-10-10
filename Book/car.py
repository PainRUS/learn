class Car():
    """Простая модель автомобиля"""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print("У этой машины " + str(self.odometer_reading) + " миль пробега.")

    def update_odometer(self, mileage):
        """
        Устанавливет заданное значение на одометре
        При попытке обратной прокрутки изменение отклоняется.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Вы не можете прокрутить назад одометр!")

    def increment_odometer(self, miles):
        """Увеличение показания одометра с заданным прирпщением."""
        self.odometer_reading += miles

class Battery():
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size=70):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print("Эта машина имеет " + str(self.battery_size) + "-kwh батарею.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "Эта машина может проехать примерно " + str(range)
        message += " миль на полном заряде аккумулятора."
        print(message)

class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""
    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса-родителя
        Затем инициализирует атрибуты специфические для электромобиля.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


"""
my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23500)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
"""

my_tesla = ElectricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
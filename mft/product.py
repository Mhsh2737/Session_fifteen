class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.__dict__}"

class NonElectrical(Product):
    def __init__(self, name, price, weight):
        super().__init__( name, price)
        self.weight = weight
    def __repr__(self):
        return f"{self.__dict__}"

class Furniture(NonElectrical):
    def __init__(self, name, price, weight, number_of_people):
        super().__init__(name, price, weight)
        self.number_of_people = number_of_people

    def __repr__(self):
        return f"{self.__dict__}"

class Electrical(Product):
    def __init__(self, name, price ,voltage):
        super().__init__(name, price)
        self.voltage = voltage
    def __repr__(self):
        return f"{self.__dict__}"

class Mobile(Electrical):
    def __init__(self, name, price, voltage, page_size, brand):
        super().__init__(name, price, voltage)
        self.page_size = page_size
        self.brand = brand
    def __repr__(self):
        return f"{self.__dict__}"

class Laptop(Electrical):
    def __init__(self, name, price, voltage, cpu, ram):
        super().__init__(name, price, voltage)
        self.cpu = cpu
        self.ram = ram
    def __repr__(self):
        return f"{self.__dict__}"

class Asus(Laptop):
    def __init__(self, name, price, voltage, cpu, ram,serial_number1):
        super().__init__(name, price, voltage, cpu, ram)
        self.serial_number1 = serial_number1
    def __repr__(self):
        return f"{self.__dict__}"

class Lenovo(Laptop):
    def __init__(self, name, price, voltage, cpu, ram,serial_number2):
        super().__init__(name, price, voltage, cpu, ram)
        self.serial_number2 = serial_number2
    def __repr__(self):
        return f"{self.__dict__}"

class Iphone(Mobile):
    def __init__(self, name, price, voltage, page_size, brand, serial_number):
        super().__init__( name, price, voltage, page_size, brand)
        self.serial_number = serial_number
    def __repr__(self):
        return f"{self.__dict__}"

class Samsung(Mobile):
    def __init__(self, name, price, voltage, page_size, brand, series):
        super().__init__( name, price, voltage, page_size, brand)
        self.series = series
    def __repr__(self):
        return f"{self.__dict__}"

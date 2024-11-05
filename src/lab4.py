class Lamp:
    def __init__(self, type_="Нема типу", power=0, quantity=0, name="None", price=0, character="Нема характер"):
        self.__type = type_
        self.__power = power
        self.__quantity = quantity
        self.__name = name
        self.price = price
        self.character = character

    def get_type(self):
        return self.__type

    def get_power(self):
        return self.__power

    def get_quantity(self):
        return self.__quantity

    def get_name(self):
        return self.__name

    def __str__(self): 
        return (f"Type: {self.__type} \nPower: {self.__power} W\n"
                f"Quantity: {self.__quantity} \nName: {self.__name}\nPrice: {self.price}\nCharacter: {self.character}")

    def __repr__(self):
        return f"Lamp({self.__type}, {self.__power} Вт, {self.__quantity} шт, {self.__name}, {self.price}, {self.character})\n"

    def __del__(self):
        print("The object is deleted")

def main():
    lamp_1 = Lamp("Розжарювальна", 6, 3, "Побутова", 200, "Яскрава")
    lamp_2 = Lamp("Світлодіодна", 9, 10, "Декоративна", 500, "Фіолетова")
    lamp_3 = Lamp("Люмінесцентна", 3, 20, "Настільна", 100, "Цікава")

    print(lamp_1)
    print(f"repr: {repr(lamp_1)}")
    print(lamp_2)
    print(f"repr: {repr(lamp_2)}")
    print(lamp_3)
    print(f"repr: {repr(lamp_3)}")
main()

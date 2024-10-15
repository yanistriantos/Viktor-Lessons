# OOP -> Object Oriented Programming

# class => wrapper data + methods to work with that data
# class -> data + ways to work with that data

# data -> variable
# ways to work with data -> function

# A class acts as a 'blueprint' for custom types in python.  The blueprint will define the structure, design, and features
# that all houses of that type should have. In Python, a class is like that blueprint—it defines a new type of object
# with its own attributes (characteristics) and methods (actions or behaviors).

# self -> reference to the object created by the type (class)

class Car:
    # variable -> attribute
    model = ""
    color = ""
    manufacturer = ""
    is_running = False

    # constructor -> the first METHOD (function) called when an object is instantiated (created)
    def __init__(self, model, color, manufacturer):
        self.model = model
        self.color = color
        self.manufacturer = manufacturer

    def start_car(self):
        if self.is_running == False:
            self.is_running = True

    def stop_car(self):
        if self.is_running:
            self.is_running = False

    def accelarate(self):
        if (self.is_running):
            print("Car is accelarating...")
        else:
            print("Car is stopped, cannot accelerate")        

    def __str__(self):
        return f"""
                Model of the car is: {self.model}
                Color of the car is: {self.color}
                Car was made by: {self.manufacturer}
                Car is: {self.is_running}
                """

# class -> 128 byte
# 10 ** 5 objects of type Class -> 128 * 1000000 bytes in memory


car1 = Car("e90", "black", "BMW")
car2 = Car("e92", "white", "B<W")

print(car1, car2)

car1.start_car()

print(car1, car2)

car1.accelarate()
car2.accelarate()

# # car1 is an object of the type Car
# cars_list = []
# for _ in range(10 ** 2):
#     car = Car("e90", "black", "BMW")
#     cars_list.append()

# print(cars_list)

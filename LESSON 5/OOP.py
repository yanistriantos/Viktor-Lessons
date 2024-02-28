# class: a blueprint of how it's objects will look and behave
# object: instance of a class. Everything in python is an object

# what is the self keyword: reference to the current object

class Factory:
    # class attributes (literally variables)
    materials = {}
    location = ""

    # the constructor (__init__ means initializator, initialization)
    def __init__(self, materials, location):
        self.materials = materials
        self.location = location

    def print_materials(self):
        for (material, price) in self.materials.items():
            print(f"Material: {material}, price: {price}")


my_factory = Factory({"wood": 20, "bricks": 15}, "Varna")
my_factory.print_materials()

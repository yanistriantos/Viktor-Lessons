# Define a base class named Item to represent a generic item with a name and a description.
class Item:
    # The constructor method initializes each new instance of the class.
    def __init__(self, name, description):
        # Instance variables for name and description are created and set to the values passed in.
        self.name = name
        self.description = description

  
# Define a subclass of Item named Weapon for weapons with additional attribute 'damage'.
class Weapon(Item):
    # The constructor for Weapon, adding 'damage' on top of name and description.
    def __init__(self, name, description, damage):
        # Call the constructor of the parent (Item) class to set name and description.
        super().__init__(name, description)
        # Initialize the damage attribute specific to the Weapon class.
        self.damage = damage

# Define a subclass of Item named Potion for potions with an 'effect'.
class Potion(Item):
    # The constructor for Potion, adding 'effect' on top of name and description.
    def __init__(self, name, description, effect):
        # Call the constructor of the parent (Item) class.
        super().__init__(name, description)
        # Initialize the effect attribute specific to the Potion class.
        self.effect = effect

# Define a subclass of Item named Armor for armors with a 'defense' attribute.
class Armor(Item):
    # The constructor for Armor, adding 'defense' on top of name and description.
    def __init__(self, name, description, defense):
        # Call the constructor of the parent (Item) class.
        super().__init__(name, description)
        # Initialize the defense attribute specific to the Armor class.
        self.defense = defense

# Define a class named Inventory to manage a collection of items.
class Inventory:
    # The constructor for Inventory, initializing an empty list to store items.
    def __init__(self):
        self.items = []

    # Method to add an item to the inventory.
    def add_item(self, item):
        self.items.append(item)

    # Method to remove an item from the inventory by its name.
    def remove_item(self, item_name):
        # Use list comprehension to filter out the item with the given name.
        self.items = [item for item in self.items if item.name != item_name]

    # Method to display the inventory's items along with their descriptions.
    def display_inventory(self):
        for item in self.items:
            print(f"item name: {item.name}, item description: {item.description}")

    def save_inventory(self):
        with open("inventory.txt", "w") as file:
            for item in self.items:
                file.write(f"Item: {item.name} Description: {item.description}\n")

# Example usage of the classes defined above.
if __name__ == "__main__":
  inventory = Inventory() # Create an Inventory instance.
  inventory.add_item(Weapon("Sword", "A sharp blade", 50)) # Add a Weapon to the inventory.
  inventory.add_item(Potion("Healing Potion", "Restores 20 HP", "20HP")) # Add a Potion to the inventory.
  inventory.display_inventory() # Display the inventory's contents.
  inventory.save_inventory()
  print("TOZI KOD")

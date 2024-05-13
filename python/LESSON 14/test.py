from game_inventory import *

if __name__ == "__main__":
  inventory = Inventory()
  inventory.add_item(Weapon("Sword", "A sharp blade", 50)) # Add a Weapon to the inventory.
  inventory.add_item(Potion("Healing Potion", "Restores 20 HP", "20HP")) # Add a Potion to the inventory.
  inventory.display_inventory() # Display the inventory's contents.
  inventory.save_inventory()

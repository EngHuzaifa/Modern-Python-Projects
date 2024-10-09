import os
from typing import List

class InventoryItem:
    def __init__(self, name: str, quantity: int, price: float):
        self.name: str = name
        self.quantity: int = quantity
        self.price: float = price

    def __str__(self) -> str:
        return f"Item: {self.name}, Quantity: {self.quantity}, Price: ${self.price:.2f}"


def get_user_input() -> InventoryItem:
    name: str = input("Enter item name: ")
    quantity: int = int(input("Enter item quantity: "))
    price: float = float(input("Enter item price: "))
    return InventoryItem(name, quantity, price)


def add_inventory_item(inventory: List[InventoryItem], item: InventoryItem) -> None:
    inventory.append(item)
    print(f"Item '{item.name}' added successfully!")


def update_inventory_item(inventory: List[InventoryItem], name: str, quantity: int) -> bool:
    for item in inventory:
        if item.name == name:
            item.quantity += quantity
            return True
    return False


def display_inventory(inventory: List[InventoryItem]) -> None:
    if not inventory:
        print("Inventory is empty.")
    else:
        for item in inventory:
            print(item)


def main() -> None:
    inventory: List[InventoryItem] = []
    while True:
        print("\n=== Inventory Management System ===")
        print("1. Add Item")
        print("2. Update Item Quantity")
        print("3. Display Inventory")
        print("4. Exit")
        
        try:
            choice: int = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        
        if choice == 1:
            try:
                item: InventoryItem = get_user_input()
                add_inventory_item(inventory, item)
            except ValueError:
                print("Invalid input. Please try again.")
        elif choice == 2:
            name: str = input("Enter the name of the item to update: ")
            try:
                quantity: int = int(input("Enter the quantity to add/subtract: "))
                if update_inventory_item(inventory, name, quantity):
                    print(f"Item '{name}' updated successfully!")
                else:
                    print(f"Item '{name}' not found in inventory.")
            except ValueError:
                print("Invalid quantity. Please enter an integer.")
        elif choice == 3:
            display_inventory(inventory)
        elif choice == 4:
            print("Exiting Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
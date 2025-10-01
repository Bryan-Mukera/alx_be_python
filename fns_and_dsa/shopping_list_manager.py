# Initialize an empty shopping list
shopping_list = []

# Function to add an item to the shopping list
def add_item(item):
    shopping_list.append(item)
    print(f"{item} has been added to the shopping list.")

# Function to remove an item from the shopping list
def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")

# Function to display the current shopping list
def display_list():
    if shopping_list:
        print("Current shopping list:")
        for index, item in enumerate(shopping_list, 1):
            print(f"{index}. {item}")
    else:
        print("The shopping list is empty.")

# Main menu loop
while True:
    print("\nShopping List Menu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        item = input("Enter item to add: ")
        if item.strip():  # Check for non-empty input
            add_item(item)
        else:
            print("Item name cannot be empty.")
    elif choice == "2":
        item = input("Enter item to remove: ")
        if item.strip():  # Check for non-empty input
            remove_item(item)
        else:
            print("Item name cannot be empty.")
    elif choice == "3":
        display_list()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
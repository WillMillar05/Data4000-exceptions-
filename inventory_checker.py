# Inventory Checker Program
# This will check inventory elvels copared to a threshold

# Ask user for valid interger (non-negative)
def get_valid_integer(prompt):
    while True:
        user_input = input(prompt).strip()
        try:
            value = int(user_input)
            if value < 0:
                print("Error: Value must be a non-negative integer.\n")
            else:
                return value
        except ValueError:
            print("Error: Please enter a valid integer.\n")
#check inventory level against the threshold and calculate a percentage 
def main():
    print("\nInventory Management System")
    print("-" * 30)

    inventory_level = get_valid_integer("Enter current inventory level: ")
    reorder_threshold = get_valid_integer("Enter minimum reorder threshold: ")

    if reorder_threshold == 0:
        print("Error: Reorder threshold cannot be zero. Cannot calculate percentage.\n")
        return

    if inventory_level < reorder_threshold:
        print("Reorder Alert: Inventory is below the threshold!")
        percentage = (inventory_level / reorder_threshold) * 100
        print(f"Current inventory is at {percentage:.2f}% of the reorder threshold.")
    else:
        print("Inventory level is sufficient. No need to reorder.")

if __name__ == "__main__":
    main()

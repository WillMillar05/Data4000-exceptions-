# Enter retail sales data andn calculare total revenue

# ask user for valid number (non-negative)
def get_valid_number(prompt, data_type):
    while True:
        user_input = input(prompt).strip()

        try:
            value = data_type(user_input)

            if value < 0:
                print("Error: Value must be non-negative.\n")
            else:
                return value

        except ValueError:
            print("Error: Please enter a valid numeric value.\n")


def main():
    print("\nRetail Sales Data Entry System")
    print("-" * 35)

    units_sold = get_valid_number("Enter number of units sold: ", int)
    price_per_unit = get_valid_number("Enter price per unit ($): ", float)

    total_revenue = units_sold * price_per_unit

    print("\nSales Summary")
    print("-" * 35)
    print(f"Units Sold: {units_sold}")
    print(f"Price per Unit: ${price_per_unit:.2f}")
    print(f"Total Revenue: ${total_revenue:.2f}")


if __name__ == "__main__":
    main()
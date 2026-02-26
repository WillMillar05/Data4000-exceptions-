
# Financial Ratio Calculator

# This calculates the profit margin ratio for a business

def get_valid_float(prompt):
    while True:
        user_input = input(prompt).strip()
        try:
            value = float(user_input)
            return value
        except ValueError:
            print("Error: Please enter a valid numeric value.\n") # re-prompt user for valid input
            pass  

def main():
    print("\nFinancial Ratio Calculator - Profit Margin Ratio")
    print("-" * 50)

    while True:
        profit = get_valid_float("Enter profit amount ($): ")
        revenue = get_valid_float("Enter revenue amount ($): ")

        try:
            if revenue == 0:
                raise ZeroDivisionError("Revenue cannot be zero for ratio calculation.")
            profit_margin_ratio = (profit / revenue) * 100
        except ZeroDivisionError as e:
            print(f"Error: {e}\n")
            pass # re-prompt user for valid input

        else:
            print(f"\nProfit Margin Ratio: {profit_margin_ratio:.2f}%")
            break 
        
         # Exit loop after successful calculation

if __name__ == "__main__":
    main()


# Salary Adjustment Program

# This program calculates the new salary after applying an adjustment percentage

def get_valid_float(prompt):
    while True:
        user_input = input(prompt).strip()
        try:
            value = float(user_input)
            return value 
        except ValueError:
            print("Error: Please enter a valid numeric value.\n")

def main():
    print("\nSalary Adjustment Calculator")
    print("-" * 30)

    current_salary = get_valid_float("Enter the employee's current salary ($): ")
    adjustment_percentage = get_valid_float("Enter the adjustment percentage (%): ")
    
    if adjustment_percentage < 0:
        print("Error: Adjustment percentage cannot be negative.\n")
        return

    if current_salary < 0:
        print("Error: Current salary cannot be negative.\n")
        return
    
    new_salary = current_salary * (1 + adjustment_percentage / 100)

    print(f"\nThe new salary after a {adjustment_percentage:.2f}% adjustment is: ${new_salary:.2f}")

if __name__ == "__main__":  
    main()

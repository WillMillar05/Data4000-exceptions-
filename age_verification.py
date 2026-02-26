#Develop a program for a marketing team in a consumer goods company. The program should ask for a customer's age (an integer) to determine eligibility for age-restricted promotions (e.g., must be 18 or older). Use try-except to catch ValueError for non-integer inputs and NameError if a variable is referenced incorrectly (simulate this by initially commenting out a variable definition). Implement a function get_customer_age that loops until a valid positive integer is provided, then prints whether the customer is eligible for the promotion based on their age.
# Age Verification Program
# This program checks if a customer is eligible for age-restricted promotions
# Ask user for valid age (positive integer)
def get_customer_age():
    while True:
        user_input = input("Please enter your age: ").strip()
        try:
            age = int(user_input)
            if age < 0:
                print("Error: Age must be a positive integer.\n")
            else:
                return age
        except ValueError:
            print("Error: Please enter a valid integer for age.\n")
        except NameError:
            print("Error: A variable was referenced incorrectly. Please try again.\n")

def main():
    print("\nAge Verification for Promotions")
    print("-" * 30)

    age = get_customer_age()

    if age >= 18:
        print("Congratulations! You are eligible for our age-restricted promotions.")
    else:
        print("Sorry, you must be at least 18 years old to be eligible for our promotions.")

if __name__ == "__main__":
    main()
    
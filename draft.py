def menu():
    print("Welcome to the Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

print("Calculator")

menu()

while True:
    try:
        opt = int(input("Enter your choice: "))
        while opt != 5:
            if opt == 1:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"Result: {num1 + num2}")
            elif opt == 2:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"Result: {num1 - num2}")
            elif opt == 3:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"Result: {num1 * num2}")
            elif opt == 4:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                try :
                    print(f"Result: {num1 / num2}")
                except ZeroDivisionError:
                    print("Error: Division by zero is not allowed.")
            elif opt == 5:
                print("Exiting the calculator. Goodbye!")
                break
        else:
            print("Invalid option, please try again.")
    except ValueError:
        print("Invalid input, please enter a number.")
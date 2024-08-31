def main():

    print("Welcome to the Simple Calculator 😄!")

    print("<------------------------------------>")

    num1:int = int(input("Enter the first number: "))

    num2:int = int(input("Enter the second number: "))
    
    print("\nChoose an operation:")
    operation = input("Enter the operation (+ , - , * , /, %): ")
    
    if operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")

    elif operation == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")

    elif operation == "%":
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")

    elif operation == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")

    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")

        else:
            print("Error: Division by zero!")
            return
    else:
        print("Error: Invalid operation!")
        return
    
    
    again = input("\nDo you want to perform another calculation? (yes/no): ")
    
    if again.lower() == "yes":
        main()
    else:
        print("Thank you for using the Calculator! 👍")

main()
    
    
    
    
    

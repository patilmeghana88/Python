try:
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result = num1 / num2
    print(f"The result is: {result}")

except ZeroDivisionError:
    print("Error: you cannot divide by Zero.")
except ValueError:
    print("Error: please enter valid numbers.")
finally:
    print("Progarm execution completed.")

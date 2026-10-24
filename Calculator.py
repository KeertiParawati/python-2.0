def add(a,b):
    return a + b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b
try:
    print("=====SIMPLECACULATOR=====")
    print("1.Addition")
    print("2.Subtraction")
    print("3.multiplication")
    print("Division")

    choice = int(input("Enter your choice"))

    num1 = float(float("Enter your first number"))
    num2 = float(float("Enter your second number"))

    if choice == 1:
        print("Result:",add(num1,num2))

    elif choice == 1:
            print("Result:",sub(num1,num2))

    elif choice == 1:
            print("Result:",multi(num1,num2))      

    elif choice == 1:
            print("Result:",div(num1,num2))              

else:
print("Invalid choice! Please select between 1 and 4.")

except ValueError:
print("Error: Please enter valid numbers.")

except ZeroDivisionError as e:
print("Error:", e)

except Exception as e:
print("Something went wrong:", e)

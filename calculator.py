import math
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a , b):
    return a / b
def square(c):
    return c ** 2
def sqrt(c):
    return math.sqrt(c)

print("Please select a Operator:-")
print("1 :- add")
print("2 :- subtract")
print("3 :- multiply")
print("4 :- divide")
print("5 :- Square")
print("6 :- Squareroot")


operator = input ("Enter your choice:- ")
if operator <= "4" :
    a = int(input ("Enter the first number:- "))
    b = int(input ("Enter the second number:- "))
else:
    c = int(input("Enter the value :- "))


if operator == "1":
    print("Sum of numbers are :- " + str(add(a,b)) )
elif operator == "2":
    print("Substraction of numbers is :- " + str(subtract(a,b)))
elif operator == "3":
    print("Multiplication of numbers is:- " + str(multiply(a,b)))
elif operator == "4":
    print("Division of numbers is :- " + str(divide(a,b)))
elif operator == "5":
    print("Square  of numbers is :- " + str(square(c)))
elif operator == "6":
    print("Square root  of numbers is :- " + str(sqrt(c)))
else:
    print("Enter a valid operator.")

   
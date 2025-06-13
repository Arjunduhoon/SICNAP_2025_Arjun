# Printing the details about myself
print("Myself Arjun, my college is IIT Guwahati and we all know that Python is powerful!")

#Creating 3 variables with type integer, float and string and printing their types
a=3
b=3.0
c="me"
print("a is of type", type(a)," b is of type", type(b)," c is of type", type(c))

# Question 3 taking input from the user
x = int(input("Write a number :"))
y = int(input("Write second number :"))
print("Sum :", x+y, "Product :", x*y, "Difference :", x-y)

# Code that outputs about the nature of number input
m = int(input("Write a number :"))
if m > 0:
    print("Given no. is positive")
elif m == 0:
    print("Given no. is 0")
else:
    print("Given no. is negative")

#Creating list
fruits = ["Mango", "grapes", "apple", "banana", "watermelon","strawberry"]
print("First item of the list is", fruits[0],"and last item of the list is", fruits[-1])
fruits.append("guava")
print("Appended list of fruits is",fruits)



# Program to check for even or odd no.
x = int(input("Write any number :"))
if x % 2 == 0:
    print("x is an even number")
else:
    print("x is an odd number")

# Creating for loop for printing square of number form 1 to 10
for i in range(1,11):
    print(i**2, end = " ")    # To print the numbers in the same line instead of the new one
print()   # To print a empty line so that the next output is in next line

# while loop for printing no. in reverse order
m = 10
while m >= 1:
    print(m, end = " ")   # To print the numbers in the same line instead of the new one
    m -= 1
print()

# Asking user for the password
a = input("Write the password: ")
if a == 'Astro@123':
    print("Access Granted")
else:
    print("Access Denied")

# Defining greet function
def greet(name):
    print(f"Hello, <{name}>!")
greet("Arjun")

# Trying to modify the tuple
x = (2.3,3.3,4.5)
#x.append(3)

# Creating the bio-data dictionary
Biodata = {"name": "Arjun", "age": "23", "field of study": "Physics"}
for key, value in Biodata.items():
    print(f"{key}: {value}")

#Code for pointing out the largest number
a, b, c = map(int, input("Write 3 numbers with space: ").split())   #Split splits the string and map applies int to every input
if a >= b and a >= c:
    print("a is the largest number")
elif a >= b and a <= c:
    print("c is the largest number")
elif a <= b and c >= b:
    print("c is the largest number")
else:
    print("b is the largest number")
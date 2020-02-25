import math
import random
"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 5.2 - calling an existing function
print("=" * 10, "Section 5.2 call an existing function", "=" * 10)


# Beneath the following function, write the code to call it
# Remove the """ """ before testing
# Note: Python requires two blank lines before a function definition


def hello():
    print("Hello Sweetie!")


hello()
# Write the code to call the hello function on the next line


# TODO 5.2 - creating and calling a function
print("=" * 10, "Section 5.2 create and call an existing function", "=" * 10)


# Write a function called joke that prints a joke on the screen
# Call the function

def joke():
    print("Funny joke")


joke()

# TODO 5.3 designing a program in functions
print("=" * 10, "Section 5.3 design a program using functions", "=" * 10)


# Create a main function that will call separate functions that
# print each line in a knock knock joke. Make sure to call main
# as the last line of your code.

def main():
    print("Knock Knock")
    print("Who's there?")
    print("Capitalism")
    print("Capitalism who?")
    print("Capitalism kills economies")


main()

# TODO 5.4 local variables
print("=" * 10, "Section 5.4 using local variables", "=" * 10)


# 1) Write a program with a main2 function. In main2, define a variable
#    called name and assign a name to it, then print hello
#    and the name variable. Have main2 call a second function get_name().
# 2) In the get_name function, ask the user for their name,
#    then greet them using a print statement.
# 3) Call the main2 function.
# Note - you would not normally have more than one main function
# in a program, we are just adding the number after main to allow
# us to write multiple short practice programs in a single file.
def main2():
    def name():
        name = (input("What is your name?"))
        return name
    print("Hello "+name())

main2()

# TODO 5.5 passing arguments to Functions
print("=" * 10, "Section 5.5 passing arguments", "=" * 10)


# Complete the code below to pass the my_number variable value from
# main3() into square() using a parameter name of value.
# Remove the """ """ before testing


def main3(value):
    def square():
     squared_value = value * value
     return squared_value
    print(square())


main3(7)

# TODO 5.6 passing multiple arguments
print("=" * 10, "Section 5.6 passing multiple arguments", "=" * 10)


# Complete the code below to pass the variables from main into
# parameters for add. Look at the code to determine the correct
# variable / parameter names. Remove the """ """

def main4():
    num_one = 5
    num_two = 7
    def add(num_one,num_two):
        total = num_one + num_two
        print(total)
    add(num_one,num_two)
main4()



# TODO 5.7 value returning functions
print("=" * 10, "Section 5.7 value returning functions", "=" * 10)


# import random - Add a statement importing the random library at the top of this file
# Add a global constant PI with a value of 3.14 before the main5 function definition
PI=3.14
def main5():
    r = int(random.randint(1,100))
    r2 = r * r



    def area(radius_squared):
        my_area = math.pi*r2
        print(format(my_area, ",.2f"))

    area(r2)

main5()

# TODO 5.8 value returning functions
print("=" * 10, "Section 5.8 value returning functions", "=" * 10)
# Complete the following program, remove the """  """ before testing

def main6():
    def bmi():
        print("This program will calculate your BMI")
        height = float(input("What is your height in inches?  "))
        weight = float(input("What is your weight in pounds"))
        patient_bmi =  (weight / (height * height)) * 703
        return patient_bmi
    print(bmi())
    # TODO print the variable answer, make sure to format it to 1 decimal place
    
    # TODO modify the bmi function to accept the height and weight
    # read the code to determine the parameter names

main6()


# TODO 5.9 the math module
print("=" * 10, "Section 5.9 use the math module", "=" * 10)
# import math - Add the import math statement at the top of this file
# Write a statement that uses the ceil function on the following variable
# Display the result


number_to_round = 4.243
answer = math.ceil(4.243)
print(answer)

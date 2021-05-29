import addition
import subtraction
import multiplication
import division

print("Welcome to the simple calculator please select from the following options:\n1: Addition \n2: Subtraction \n3: Multiplication  \n4: Division")
selection = int(input("Please enter your selection:"))
num_one = float(input("Please enter your first number:"))
num_two = float(input("Please enter your second number:"))
if (selection == 1):
    sum_num = addition.add_things(num_one, num_two)
    print(f"Your result:{sum_num}")
elif (selection == 2):
    diff_num = subtraction.subtract_things(num_one, num_two)
    print(f"Your result:{diff_num}")
elif (selection == 3):
    product_num = multiplication.multiply_things(num_one, num_two)
    print(f"Your result:{product_num}")
elif (selection == 4):
    quot_num = division.divide_things(num_one, num_two)
    print(f"Your result:{quot_num}")

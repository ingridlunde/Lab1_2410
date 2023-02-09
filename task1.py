# Task 1
# Write a function named jains that takes
# two throughput values (int and/or float) as arguments and returns a JFI.

# Function Jains with two input values.
def jains(value1, value2):
    result = ((value1 + value2)**2)/(2*(value1**2 + value2**2))
    return result


# Program excecution starts here.
# Input values
n1 = input('Enter number 1: ')  # input 1
n2 = input('Enter number 2: ')  # input 2

# Function is called here.
output = jains(float(n1), float(n2))

# print the result
print('The JFI is: ', output)


'''1.(i) Write a Python function named "circle_area" that takes the radius of a circle as a parameter 
and returns the area of the circle. Use the formula: area = π * r^2. (Assume π ≈ 3.14). Test the 
function with a radius of 4. (5 marks) '''

import math

def circle_area(radius):
    return math.pi * radius ** 2

# Test the function
radius = 4
print("The area of the circle is:", circle_area(radius))


'''
1.(ii) Given a list of integers [4, 7, 2, 9, 12, 15], write a program using a for loop to find the sum 
of all odd numbers and print the result. (5 marks)
'''

numbers = [4, 7, 2, 9, 12, 15]
odd_sum = 0

for num in numbers:
    if num % 2 != 0:
        odd_sum += num

print("The sum of all odd numbers is:", odd_sum)


'''
1.(iii) Write a Python function that takes two numbers as input and returns their sum, difference, 
product, and quotient.
'''

def calculate(a, b):
    return a + b, a - b, a * b, a / b if b != 0 else "Division by zero is not allowed"

# Test the function
a, b = 10, 5
results = calculate(a, b)
print("Sum:", results[0], "Difference:", results[1], "Product:", results[2], "Quotient:", results[3])


'''
1.(v) Given the dictionary below, update the value of 'age' to 26 and add a new key-value pair 
('city', 'Kampala’'). student_info = {'name': 'Alice', 'age': 20, 'grade': 'A'}
'''
student_info = {'name': 'Alice', 'age': 20, 'grade': 'A'}

# Update and add new key-value pair
student_info['age'] = 26
student_info['city'] = 'Kampala'

print(student_info)
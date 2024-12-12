'''
4(i)
 a) Define Object-Oriented Programming (OOP) and its significance. 
''' 
#Object-Oriented Programming (OOP) is a programming concept that organizes data and behavior into reusable structures called objects created using classes. 

#Significance in software development:
'''
- can allow code to be reused through inheritance.  
- Helps organizing code into classes and objects.  
- Facilitates maintainability by enabling code encapsulation.  
- Supports polymorphism, allowing objects to take on multiple forms.  
''' 


#### b) What is a class in OOP? How does it differ from an object?  

'''
A class is a blueprint for creating objects. It defines the structure, attributes, and behavior of an object while
an object is an instance of a class. 
 
'''




### 4(ii) Count word occurrences in a sentence.

# Program to count word occurrences
sentence = input("Enter a sentence: ")
words = sentence.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)


# 4(iii) Function to return the sum of two numbers.

def add_numbers(a, b):
    return a + b

# Test the function
a, b = 3, 4
print(f"The sum of {a} and {b} is: {add_numbers(a, b)}")

### 4(iv) Define a `Car` class and instantiate an object.

class Car:
    def __init__(self, brand, name, color):
        self.brand = brand
        self.name = name
        self.color = color

# Instantiate the object
my_car = Car("Toyota", "Corolla", "Red")
print(f"Brand: {my_car.brand}, Name: {my_car.name}, Color: {my_car.color}")




### 4(v) Add a `start_engine` method to the `Car` class.

class Car:
    def __init__(self, brand, name, color):
        self.brand = brand
        self.name = name
        self.color = color

    def start_engine(self):
        print(f"The engine of the {self.name} has started.")

# Instantiate and call the method
my_car = Car("Toyota", "Corolla", "Red")
my_car.start_engine()


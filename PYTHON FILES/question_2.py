'''
2. (i). Given the following students details and marks: Enter these details from the keyboard ( 
Student name=Gloria Arinda, Student Number= SEP23/BCS/088U/F, Programming=90, Data 
Science= 87,Computer applications=77). Calculate the average mark and print the answer in 3 
decimal places. Display full details of the student

'''

student = {
    "name": input("Enter student name: "),
    "number": input("Enter student number: "),
    "programming": float(input("Enter Programming marks: ")),
    "data_science": float(input("Enter Data Science marks: ")),
    "computer_applications": float(input("Enter Computer Applications marks: "))
}

# Calculate the average
average = (student["programming"] + student["data_science"] + student["computer_applications"]) / 3

# Display details and average
print("\nStudent Details:")
print(f"Name: {student['name']}")
print(f"Number: {student['number']}")
print(f"Average Marks: {average:.3f}")



'''
2. (ii) A car's miles per gallon can be calculated with the following formula. Write a program 
that asks the user for the number of miles driven and gallons used. It should calculate the car's 
miles-per-gallons-used and display the result MPG = milesDriven / gallonsOfGasUsed (10 
marks)
'''

miles = float(input("Enter the number of miles driven: "))
gallons = float(input("Enter the gallons of gas used: "))

# Calculate MPG
if gallons != 0:
    mpg = miles / gallons
    print(f"The car's miles per gallon (MPG) is: {mpg:.2f}")
else:
    print("Gallons used cannot be zero.")


'''
2. (iii) Write a Python program to print all the numbers from 1 to 100 that are not divisible by 2 
( 5 marks)
'''
#using a for loop
for num in range(1, 101):
    if num % 2 != 0:
        print(num, end=" ")

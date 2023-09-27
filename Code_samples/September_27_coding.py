# in class coding from Wednesday, September 27

#for problem 5
#days_of_week = ['Thursday','Friday','Saturday','Sunday','Monday','Tuesday','Wednesday']

#daynum = int(input("What day of the month?"))
#num = daynum%7
# to get the proper day of the week I just print out days_of_week[num]

# every loop could be written as a while loop
# but for loops are simpler, less error-prone

#syntax: while <some_boolean_condition>:
#           one or more lines of code

# compute n factorial for some n

n = 1    # initial value - priming read or priming load
prod = 1
while n <= 5:
    prod *= n
    n += 1   # if you leave this statement out you get an infinite loop
print(prod)

#the same code as a for i loop:
prod = 1
for i in range(1,6):
    prod *= i
print(prod)

# an example of a problem you can't solve with a for loop

# get some user input and stop when the user enters valid items

num = int(input("enter a number between 1 and 30, inclusive"))
while num < 1 or num > 30:
    print("I'm sorry, that is not a number between 1 and 30, inclusive")
    num = int(input("enter a number between 1 and 30, inclusive"))

#now we have valid input
print(num)


#sentinel loop
student_list = []
name = input("Enter the first student name; type 'q' to quit") # 'q' is the sentinel
while name.lower() != 'q':  # this is a sentinel loop
    student_list.append(name)
    name = input("Enter the next student name; type 'q' to quit")
print(student_list)

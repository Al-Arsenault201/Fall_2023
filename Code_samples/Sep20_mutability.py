
"""
a = 2
print(id(a))
a *= 4
print(id(a))
#a is an int and it's immutable

#same with strings
string1 = "Purdue"
print(id(string1))
string1 = "UC-Berkeley"
print(id(string1))

#now with lists
grocery_list = []
print(id(grocery_list))
grocery_list.append("Milk")
print(id(grocery_list))
grocery_list.append("Eggs")
grocery_list.append("Cheese")
print(grocery_list)
grocery_list[1] = "Grapes"
print(grocery_list)
print(id(grocery_list))
"""

truth = "Purdue's football team will always break your heart by losing to teams they should beat"
# can I split that up into words?
# yes, "split" for strings
truth_list = truth.split()
print(truth_list)
# split takes a string and returns a list of words
# any time split encounters white space, it considers that a new word
# important: split throws away the white space

"""
my_grades = input("Please enter your name, major, gpa, and height, separated by tabs")
print(my_grades)
my_data = my_grades.split()
print(my_data)
my_data[2] = float(my_data[2])
my_data[3] = int(my_data[3])
print(my_data)
"""
# a more general case truth.split(',')
my_grades = input("Please enter your name, major, gpa, and height, separated by commas")
#print(my_grades)
my_data = my_grades.split(',')
#print(my_data)
#my_data[2] = float(my_data[2])
#my_data[3] = int(my_data[3])
print(my_data)
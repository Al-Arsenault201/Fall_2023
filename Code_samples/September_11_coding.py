# in-class coding from Monday, September 7

# first, we're going to do some input
# variable_name = input("meaningful prompt")

fav_cookie = input("What is your favorite type of cookie?")

#print out the value
#print(fav_cookie)

#make our print statement more useful
print("you said your favorite cookie is", fav_cookie)

#you don't have to have blank spaces
print("you said your favorite cookie is"+fav_cookie)

#by default, Python automatically prints a newline (enter, carriage return)
# after every print statement

# you can avoid that using end
print("you said your favorite cookie is", fav_cookie, end="///")
print("you said your favorite cookie is"+fav_cookie, end="done")

#what if you want to input a number?
print("We will tell you how many gallons you need", end = " ")
print("When you enter the number of quarts")
quarts = input("How many quarts do you have?")

#to fix the problem - cast
# change the type
quarts = int(quarts)  #changes quarts from string to integer
gallons = quarts * 0.25
print (quarts, "quarts equals", gallons, "gallons")

#casting to other types
quarts = 10
print(quarts)
pints = float(quarts * 2)
print(pints)

#casting to a string
pints = 2
print(pints)
two_cups = str(pints)
print(two_cups)

#Python gives you a lot of flexibility; write code you understand

print("We will tell you how many gallons you need", end = " ")
print("When you enter the number of quarts")
quarts = int( input("How many quarts do you have?"))
gallons = quarts * 0.25
print (quarts, "quarts equals", gallons, "gallons")

# the input prompt must be a single string
birthdate = input("Enter the date of your birth", "in month and day")

# division
# floating point division: /
# integer division: //
x = 1/3
y = 1//3
print("x = ", x)
print("y = ", y)
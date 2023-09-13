# in-class coding from Wednesday, September 13

# sequential execution
# execute each statement in order, exactly once

num_cakes = int(input("How many cakes will you make?"))
#print("You will need", 3 * num_cakes, " eggs")
num_eggs = 3 * num_cakes
print("You will need", num_eggs, " eggs")

# conditional execution
# you execute code (1 or more lines) ONLY if some condition is True

# remember boolean - True and False
if 4 > 3:
    print("Of course that's true")

# if (some boolean condition):
# whatever code is indented is executed when the boolean is true

if 4 > 3:
    print("of course that's true")
    print("why would it not be?")

if 3 > 4:
    print("that can't be true")
print("we're done with the conditional")

#summary: this is the case where we do something if condition is true
# we do nothing otherwise

# case: we want to do one thing if a condition is True
# do something else if the condition is False

grade = input("Enter your letter grade in this class")
if grade == "A":
    print("Congratulations")
else:
    print("Not bad but you could do better")

# more complex:  sometimes we want to look at a value
# do one thing for one value; a second thing for a second value,
# and so on

# consider for your age in years
# if you're under 18, you're a minor. No voting; no drinking; no gambling
# if you're 18, 19, or 20, you can vote, but still no drinking, no gambling
# if you're 21 or older, you're an adult - do what you want

age = int(input("Enter your age in years"))
#if you're under 18 you're a minor
if age < 18:
    print(" you're a minor")
    print("you can't vote yet")
elif age < 21:
    print("you can and should vote")
    print("but no drinking or gambling yet")
elif age < 25:
    print("you're an adult but be careful")
    print("your car insurance rates stink")
else:
    print("You're an adult")
    print("You're on your own")
print ("The conditional is over")
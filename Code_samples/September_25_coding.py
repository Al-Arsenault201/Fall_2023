# in class coding from Monday, September 25

grocery_list = ["Milk", "Eggs", "Cereal", "Coffee", "Apples",
     "Strawberries", "Broccoli", "Cucumber", "Tomatoes",
     "Green Onions"]

# for each loop to print out each item on the list exactly once
#for item in grocery_list:
#  print(item)

mixed_list = ["UMBC", 1967, "Maryland", 1789.2, "Harvard", 1636,
              True,42]
#create a new variable that will be a list of all string elements
new_list = []
for item in mixed_list:
  new_list.append(str(item))
print(new_list)
silly_string = "\t".join(new_list)
print(silly_string)

#this won't work
"""
for item in mixed_list:
  item = str(item)
silly_string = ",".join(mixed_list)
print(silly_string)
"""

# You CANNOT change the values of the items in a list in for each loop


states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado", "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

# Suppose I want to print out each state that ends in 'a'
"""
for state in states:
  if state[-1] == 'a':
    print(state)
"""
# print each state that ends in a vowel
vowels = ['a','e','i','o','u','y']
for state in states:
  if state[-1] in vowels:
    print(state)

for i in range(0, len(mixed_list),1):
    if mixed_list[i] == str(mixed_list[i]):
        print(mixed_list[i])


#this is the code that converts non-strings in the list to be strings
# for i loop CAN change the values in the list
for i in range(0, len(mixed_list), 1):
  if mixed_list[i] == str(mixed_list[i]):
    print(mixed_list[i])
  else:
    mixed_list[i] = str(mixed_list[i])
print(mixed_list)


#those values in the range statement have defaults
# if you do not specify an initial value, the default is 0
# start at the first element in the list

# if you don't specify a hop count, it will default to 1
for i in range(0, len(states)):  #only have two values
  print(states[i])

for i in range(len(states)):  # only have the end value
  print(states[i])

DIGITS = ['0','1','2','3','4','5','6','7','8','9']
score = input("Please enter your lab grade")
d_score = 2 * score
print (d_score)

#input validation

DIGITS = ['0','1','2','3','4','5','6','7','8','9']
score = input("Please enter your lab grade")
is_digit = True
for char in score:
    if not char in DIGITS:
        print("I'm sorry; we only accept numeric scores")
        is_digit = False
if is_digit == True:
    d_score = float(score)/2
    print (d_score)
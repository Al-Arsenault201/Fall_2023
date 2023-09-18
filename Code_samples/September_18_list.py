# list programming - in class September 18

# declare a new variable that is an empty list
grocery_list = []
print ("The list is currently", grocery_list)

# we'll add elements to the list
grocery_list.append("Milk")

#append adds whatever's in the parentheses to the END of the list
grocery_list.append("Eggs")
print("The list is currently", grocery_list)

#referencing an element
print(grocery_list[0])

if grocery_list[1] == "Eggs":
    print("Eggs are on the list")


# what if we want to insert an item that isn't at the end

#insert gives the index, and the value:
grocery_list.insert(1,"Strawberries")
print("The list is currently", grocery_list)

if grocery_list[1] == "Eggs":
    print("Eggs are on the list")
else:
    print("No that's wrong")

# everything after what's inserted gets pushed down and gets a new index number
# nothing gets over-written

#what if I wanted to add more than one entry at a time
#grocery_list.append("dog food","yogurt")
# not allowed -the above statement is an error

#grocery_list.insert(1,"dog food", "yogurt")
# you can only insert one element at a time

# can you have different types in the same list? yes
"""
grocery_list.append(5)
grocery_list.append(True)
grocery_list.append(9.8)
print("After latest additions", grocery_list)
"""

# can we create a list that's not empty at the start?
new_list = ['Milk',"Eggs","Strawberries","dog food","yogurt"]
print("New_list is ", new_list)

#length of a list = the number of elements currently in the list
another_list = []
print(len(another_list))

# the index of the last element in the list is ALWAYS one less than the length
#print(new_list[len(new_list)])
# the above statement is ALWAYS an error because there can never be such an element
# the correct reference for the last element in a list is ALWAYS
print(new_list[len(new_list)-1])

#computer scientists are lazy - we prefer fewer keystrokes
print(new_list[-1]) #last element in the list

#removing an item from the list by its value
print(new_list)

# i go through the store. I pick up yogurt from the dairy aisle
new_list.remove("yogurt")
print(new_list)

# this works if the item's there.
# what if it's not there
#new_list.remove('chicken')

# in is a Python function that returns True if an item is in a list
# and returns False if it's not
# syntax:  value in list_variable

if 'chicken' in new_list:
    new_list.remove("chicken")
else:
    print("You don't need that")

# what if you want to remove whatever value is in index 2
# remove by index not value

del new_list[2]
print("After delete", new_list)

# another way to do this - pop
new_list = ['Milk', 'Eggs', 'Strawberries', 'dog food', 'yogurt']
new_list.pop(4)
print("After pop", new_list)

# difference between pop and delete
# pop can remove one item
# del can remove multiple items

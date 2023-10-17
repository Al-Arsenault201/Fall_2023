#in-class coding for Monday, October 16

dogs ={"bonnie":"beagle","doug":["beagle","boxer","bulldog"],"penny":"cocker spaniel",
       "baron1":"beagle", }

#dictionary of states and their Governors
governors= {}
#to insert a value, specify
governors["Maryland"] = "Moore"
governors["Virginia"] = "Youngkin"
governors["Louisiana"] = "Edwards"

#change an element in a dictionary
# reassign it
governors["Louisiana"] = "Landry"

#print the value of a key
print(governors["Virginia"])

#find the state of which Wes Moore is Governor:

for g in governors.keys():
    if governors[g] == "Moore":
        print(g)

# deleting all cocker spaniels from dogs
dogs ={"bonnie":"beagle","doug":["beagle","boxer","bulldog"],"penny":"cocker spaniel",
       "baron1":"beagle", }

dogs.pop("lady", None)
dogs.pop("lady", -1)

for k in recipe.keys():
    recipe[k] = str(recipe[k])+"sugar"
    recipe[k].append("sugar")

states = ["Alabama","Alaska","Arizona"..]
govs = []

def funstuff():
    return None

def second_function():
    return 1

if __name__ == "__main__":

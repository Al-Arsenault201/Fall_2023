# problem 1 - gauss sum

target = int(input("Enter the number to exceed"))

iterations = 0
sum = 0
while sum <= target:
    iterations += 1
    sum += iterations
#print results

#problem 2 as two separate loops
item = input("enter the next item on the burger")
while item != "bottom bun":
    print("you must start with a bottom bun")
    item = input("enter the next item on the burger")

condiments = []
burgers =[]
num_burgers = 0
while item != "top bun":
    item = input("")
    burgers.append(item)
    if not item in condiments:
        condiments.append(item)

#print results


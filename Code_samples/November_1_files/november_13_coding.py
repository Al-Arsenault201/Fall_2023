#in-class coding from Monday, November 13

import random
nums = []
length = int(input("how many numbers in the list?"))
for i in range(length):
   nums.append(random.randint(1,1000000))
print(nums[0])

#linear search
target = int(input("For what number are you searching?"))
comparisons = 0
found = False
for num in nums:
    comparisons += 1
    if num == target:
        found = True
        print("Found ", target, "in ", comparisons, " comparisons")
if not found:
    print("After ", comparisons,
          " comparisons we determined that ", target, "was not in the list")
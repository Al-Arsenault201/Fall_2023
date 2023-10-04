# Function definition

def fourth_root(num):
    if num >= 0:
        ans = num**(1 / 4)
        return ans
    else:
        return None
# we could have also said
#		return
# or just omitted the entire else: clause and
# have no return statement at all. The code
# works the same
# get the original value from the user
# then call the function
original_number = float(input("enter a number"))
done = False
while not(done):
   final_number = fourth_root(original_number)
   if final_number != None:
       print("The fourth root of", original_number, end = '')
       print(" is ", final_number)
       done = True
   else:
       original_number = float(input("we were serious about needing a non-negative number"))

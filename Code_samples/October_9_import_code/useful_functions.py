def print_error(message):
    print("sorry, that is an error")
    if message == "Not an integer":
        print("You did not enter an integer")
    else:
        print (message)

def square_root(number):
    if number >= 0:
        return number**(1/2)
    else:
        print_error("Square roots of negative numbers are not defined")

if __name__ == "__main__":
    test_num = float(input("please enter a number"))
    y = square_root(test_num)
    if y != None:
        print (y)
    else:
        print ("error checking worked")
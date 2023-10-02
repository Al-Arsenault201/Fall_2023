def print_day(day_number):

    get_started()

    if day_number == 1 or day_number == 21:
        print(str(day_number) + "st")
    elif day_number == 2 or day_number == 22:
        print(str(day_number) + "nd")
    elif day_number == 3 or day_number == 23:
        print(str(day_number) + "rd")
    else:
        print(str(day_number) + "th")

def get_started():
        print("I'm proving the program works")
        return

if __name__ == "__main__":



    date = int(input("Enter the day in September"))
    print_day(date)
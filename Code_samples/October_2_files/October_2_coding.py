# in-class coding for Monday, October 2

def calculate_days(years, months,days):
    num_days = 365 * years + 30 * months + days
    if years >4:
        num_days += 1
    return num_days

if __name__ == "__main__":
    yrs = 23
    mos = 3
    days = 22
    length_of_time = calculate_days(yrs, mos, days)
    print("you have been alive", length_of_time, "days")

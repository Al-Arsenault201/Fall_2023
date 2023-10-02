# multiple return statements

def fourth_root(number):  # number is a float
    if number < 0:
        return "negative numbers do not have real fourth roots"
    else:
        return str(number**(1/4))
    print("see we never got here")

if __name__ == "__main__":
    n = float(input("Enter the number"))
    ans = fourth_root(n)
    if ans[0]  == "n":
        print(ans)
    else:
        print("the fourth root of ",n, "is", ans)
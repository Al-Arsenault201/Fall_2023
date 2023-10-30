#in-class coding for Monday, October 30

def to_octal(decimal):
    result = []
    while (decimal//8 > 0):
        result.append(decimal%8)
        decimal = decimal//8
    result.append(decimal)
    answer = ""
    for i in range(len(result)-1,-1,-1):
        answer = answer + str(result[i])
    print("0o"+answer)

def oct(number):
    result = [0]
    while number//8>0:
        result.insert(0, number%8)
        number = number//8
    result.insert(0,number)
    answer = "0o"
    for i in range(len(result)-1):
        answer = answer + str(result[i])
    print(answer )

def to_binary(number):
    result = []
    while (number // 2 > 0):
        result.append(number % 2)
        number = number // 2
        print (result)
    result.append(number)
    answer = ""
    for i in range(len(result) - 1, -1, -1):
        answer = answer + str(result[i])
    print("0b" + answer)


if __name__ == "__main__":
#    to_octal(64)
#    to_binary(126)
    oct(64)

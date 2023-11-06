select = int(input("please enter your cup selection"))
#input validation
for i in range((select+1)%14, (cups[select]+select+1)%14):
    cups[i] += 1
cups[select] = 0 
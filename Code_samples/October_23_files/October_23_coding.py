# in-class coding for Monday, October 23
table = []
size = int(input("how many rows"))
sym_a = input("What is symbol a")
sym_b = input("what is symbol b")
for i in range(size):
    row = []
    for j in range(size):
        if (i+j)%2 == 0:
            row.append(sym_a)
        else:
            row.append(sym_b)
    table.append(row)
for k in range(len(table)):
    print(table[k])



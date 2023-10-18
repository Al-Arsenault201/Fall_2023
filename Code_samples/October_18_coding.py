#in-class coding from Wednesday, October 18

#in Python you have to open a file before you can use it
#there are many ways to do it
#this is the method we will use in this class

with open("/Users/alfredarsenault/Python_data/Medal_table.csv","r") as infile:
#    data = infile.read()
    datalist = infile.readlines()
#    print(datalist)
    datalist.pop(0)
#   print(datalist)
    for i in range(len(datalist)):
        datalist[i] = datalist[i].split(',')
#        print(datalist[i])
#    print(datalist)
    for i in range(len(datalist)):
        datalist[i][2] = int(datalist[i][2])
        datalist[i][3] = int(datalist[i][3])
        datalist[i][4] = int(datalist[i][4])
        datalist[i].pop(5)
        datalist[i].append(datalist[i][2] + datalist[i][3] + datalist[i][4])
        print(datalist[i])

# not:  [i,3] nor [i, [3]]
# row always comes first; then column

#I can only write strings to files
#not working with the infile anymore
for j in range(len(datalist)):
    datalist[j][2] = str(datalist[j][2])
    datalist[j][3] = str(datalist[j][3])
    datalist[j][4] = str(datalist[j][4])
    datalist[j][5] = str(datalist[j][5])
    datalist[j] = ";".join(datalist[j])
    print(datalist[j])
outgoing_data = "\n".join(datalist)
print(outgoing_data)

#now I can write out a string to a file
with open ("/Users/alfredarsenault/Python_data/results.txt","w") as outfile:
    outfile.write(outgoing_data)
    print("file_done")
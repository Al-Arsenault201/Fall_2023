import os
os.chdir("/Users/alfredarsenault/Downloads")
with open ("1976-2020-president.tab","r") as infile:
    data_list = infile.readlines()
#    print(data_list[0])
data_list.pop(0)
print(data_list[0])
for i in range(len(data_list)):
    data_list[i] = data_list[i].split("\t")
for j in range(20):
    print (data_list[j])
new_list = []
for i in range(len(data_list)):
    new_row = []
    new_row.append(int(data_list[i][0]))
    new_row.append(data_list[i][1].strip('\"'))
    new_row.append(data_list[i][8].strip('\"'))
    new_row.append(int(data_list[i][10]))
    new_row.append(int(data_list[i][11]))
    new_list.append(new_row)
#print out the first 20
for j in range(20):
    print(new_list[j])
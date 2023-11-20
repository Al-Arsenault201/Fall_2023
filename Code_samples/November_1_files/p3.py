import os
os.chdir("/Users/alfredarsenault/Downloads")
PARTIES = ['"DEMOCRAT"','"REPUBLICAN"']
with open("1976-2020-president.tab","r") as infile:
    data = infile.readlines()
#    print (data)
    for i in range(len(data)):
        data[i]=data[i].split("\t")
    shortened_data = []
    for j in range(len(data)):
        if data[j][8] in PARTIES:
#            print(data[j][8])
            for k in range(10,12):
                data[j][k] = int(data[j][k])
            shortened_data.append(data[j])
    print ("original data: ", len(data))
    print ("edited data: ", len(shortened_data))
    print (shortened_data)


import os
print(os.getcwd())
print(os.listdir())
filename = "$DATA_PATH$" + "/stopwords.txt"
with open(filename,"r") as infile:
    data = infile.read()
    print(data)
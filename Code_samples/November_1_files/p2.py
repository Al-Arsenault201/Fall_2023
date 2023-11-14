name = 'Jones"'
new_name = ""
for letter in name:
    if letter != '"':
        new_name = new_name+letter
print(new_name)
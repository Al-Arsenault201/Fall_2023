schools = {
    "UMBC":"Retrievers",
    "UMCP": "Terrapins",
    "JHU": "Blue Jays"
  }
#What will be printed if I try to get a value from the dictionary using the statement:
print(schools.get("MSU", -1))
Y = schools.pop("MSU")
print(Y)

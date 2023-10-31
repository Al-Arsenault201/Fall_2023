class Dog:
    def __init__(self, name, age, breed, tricks):
        self.name = name
        self.age = age
        self.breed = breed
        self.tricks = tricks

    def learn_tricks(self,new_tricks):
        for i in range(len(new_tricks)):
            self.tricks.append(new_tricks[i])

if __name__ == "__main__":
    my_dog = Dog("Doug",10,"Beagle",[])
    print(my_dog.name)
    print(my_dog.tricks)
    my_dog.learn_tricks(["sit","down","with me","roll"])
    print(my_dog.tricks)


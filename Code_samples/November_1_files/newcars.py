class Car:

    def __init__ (self,make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = self.make + self.model + self.year
        return long_name

if __name__ == "__main__":
    my_new_car = Car("Audi","A5", "2024")
    #creates an object called "my new car"
    #instantiates my_new_car
#    print(my_new_car.make)
    print(my_new_car.get_descriptive_name())

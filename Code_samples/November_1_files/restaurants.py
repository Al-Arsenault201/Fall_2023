# definitions for a class "Restaurants"

class Restaurant:
    def __init__(self, name, cuisine,price,meals):
        self.name = name
        self.cuisine = cuisine
        self.price = price
        self.meals = meals
        self.menu = []

    def specials(self):
        spec = input ("Please enter today's specials, one per line. Enter 'q' to quit.")
        while spec.lower() != "q":
            self.menu.append(spec)
            spec = input ("Please enter today's specials, one per line. Enter 'q' to quit.")
        print("The menu now includes", self.menu)

class Fast_Food(Restaurant):

    def __init__(self, name, cuisine,price, meals):
        super().__init__(name, cuisine, price, meals)


if __name__ == "__main__":
    my_chow = Restaurant("My_Chow","Fast_Food","$$",["B","L"])
    my_chow.specials()
    print(my_chow)
    Wendys = Fast_Food("Wendys", "Burgers", "$",["B","L","D"])
    print(Wendys.name)

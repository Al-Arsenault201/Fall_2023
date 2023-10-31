import restaurants

if __name__ == "__main__":
    my_chow = restaurants.Restaurant("My_Chow","Fast_Food","$$",["B","L"])
    my_chow.specials()
    print(my_chow)
    Wendys = restaurants.Fast_Food("Wendys", "Burgers", "$",["B","L","D"])
    print(Wendys.name)

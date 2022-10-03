###we want to make modules...thie first module:
def make_pizza(size,*topings):
    print(f"You want a {size} inch pizza with the topings:  ")
    for topping in topings:
        print(f" ** {topping}")
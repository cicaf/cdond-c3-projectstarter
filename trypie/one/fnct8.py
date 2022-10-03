####A FUNCTION THAT TAKES AN ORDER AND APPENDS IT TO AN ORDER LIST...
def food(toppings,done):
	while toppings:
        print(f"this the toppings you want {toppings} ")
	    cooking = toppings.pop()
	    print(cooking)
	    done.append(cooking)
def complete(done):
	for items in done:
	    print(f"This food {items} is done")

topp = ['anchovies','pineapple','oranges','melons','tits']
dane = []
food(topp,dane)
complete(dane)

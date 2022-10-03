#polling a list and elimminating them oone by one onto another list

from sqlite3 import complete_statement


topping = ['mushrooms','pineapple','just dough','chapati','boerwoers','mambotu']
complete_order = []
while topping:
    food = topping.pop()
    print(f" here is your pizza topping of {food} for you sir")
    complete_order.append(food)

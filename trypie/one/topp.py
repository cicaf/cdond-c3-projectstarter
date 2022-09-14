#prompting user to enter toppings till....
toping = ''
Active = True
while Active:
    toping = input("Enter topping you want  please :")
    if toping == 'done':
        Active = False
    else:
        print (f"is {toping} the toping that you want???")
        continue
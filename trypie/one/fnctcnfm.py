#FUNCTIN CONFIRMATION...
def capital(name1,name2, name3 = ''):
    if name3:
        name1 = input("Name 1 please: ")
        name2 = input("Name 2 please: ")
        name3 = input("Name 3 please : ")
        print(f"The name capitalized is {name1.upper()} and {name2.upper()} and name 3rd is {name3.upper()} ")
    else:
        name1 = input("Name 1 please: ")
        name2 = input("Name 1 please: ")
        print(f"The name capitalized is {name1.upper()} and {name2.upper()}")


capital('1','2','3') 
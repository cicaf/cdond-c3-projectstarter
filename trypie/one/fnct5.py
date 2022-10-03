#function with 2 loops a while and if statements for input...

def formName(l_name,f_name):
    print("The name of the person are :")
    print(f"{l_name.upper()} and {f_name.upper()} ")



while True:
    a = input("please insert first name :")
    if a == 'q':
        break
    b = input("Please give us second name : ")
    if b =='q':
        break
    else:
        formName(a,b)

#using a flag here to determine if a while loop ought to run or nuuuh...
active = True
while active:
    message = input("your name please ")
    if message == 'quit':
        active = False
    else:
        print(f" is this your name {message} ?")


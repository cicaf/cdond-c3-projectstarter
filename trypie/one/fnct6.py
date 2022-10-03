##Just passing a simple list of names through our weird ass function
def greetings(names):
    for name in names:
        msg = f"Hi {name.title()} hope youre good have a seat... "
        print(msg)


guys = ('anto','gea','rashy','roro','malacia')
greetings(guys)
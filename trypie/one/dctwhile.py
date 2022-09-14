#lists and while loops...
#WE WILL USE A WHILE LOOP TO MOVE USSERS FROM THE UNCONFIRMED LIST TO THE CONFIRMED USER LIST...
unconfirmed = ['ati','anyi','osoro','odipo','msambati','msahulu','wekesa','naliaka']
confirmed = []

while unconfirmed:
    user = unconfirmed.pop()
    print(f"This is the confimed list {confirmed}")
    print(user)
    confirmed.append(user)
for name in confirmed:
    print (f"\n this is the second list {name} ")
    print(f"This is the  confirmed list {confirmed}")
    print(f"this is the unconfirmed list {unconfirmed}")



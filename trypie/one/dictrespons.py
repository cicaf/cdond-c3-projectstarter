#a programm that uses users name and response and stores them ina dictionary...
#instatiate an empty dictioinary...

from httplib2 import Response


Responses = {}

polling_Active = True

while polling_Active:
    name = input("\n what is your name please :")
    count = input("\n What is your body count ?")
    
    #THIS LINE SAVES THE COUNT TO THE NAME AND RESPONSES DICTIONARY...

    Responses[name] = count

    stop = input("\n you dont want to continue ?")
    if stop == 'yes':
        polling_Active = False
        break
    else:
        print("\n Next respondent please! ")

        print(f"\n AS for you {name} your count is {count} ")
print(Responses)

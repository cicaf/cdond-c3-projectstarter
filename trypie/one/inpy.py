#just input ref
message = input("Asake them never see me what: ")
print(message)
#a programme that asks for use input and checks if its a multiple of ten...
prompt ="Pleas we are conducting some research on the most common occurence on multples of 10 in guesses"
prompt+= "Please insert your number here please"

number = input(f"{prompt } :")
number = int(number)
if number % 10 == 0:
    print(f" {number} is divisible by 10")
else:
    print(f"{number} is not divisible")
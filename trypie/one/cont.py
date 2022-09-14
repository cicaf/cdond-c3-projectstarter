#test continue statement...
#programme to check for divisibility or if prime...using while loop.
number = 0
while number < 100:
    number = input()
    number = int(number)
    if number % 2 == 0:
        print(f"{number} is even")
        continue
    else:
        print(number)
        break
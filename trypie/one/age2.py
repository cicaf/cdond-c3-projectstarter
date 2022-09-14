#asking for customers age and telling them the tickets cost...
#people below 3 are free...3 to 12 years is just 10 dollars and over 12 is 15 usd
age = 0
while age == 0:
    age = input("Please insert your age :")
    age = int(age)
    if age <= 3:
        print("Hi baby! its free for you today")
    elif age > 12:
        print("Youre old enough...you need to pay 15USD ")
    else:
        print("youre lucky youre under 12 years but you still need to pay 10 USD")

        continue

    
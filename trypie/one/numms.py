from lib2to3.pgen2.token import STAREQUAL


square = []
for number in range(1,1000):
    number = number**2
    square.append(number)

#print (square)
#print(len(square))
#print(sum(square))
cube = [value **3 for value in range(1,21)]
print (cube)
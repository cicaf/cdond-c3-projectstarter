numbers = [value  for value in range(1,21)]
print(numbers)

numbers2 =[]
for digits in range(21,51):
    numbers2.append(digits)

print (numbers2)
#4.3 making a list from 0 to a million,and printing it out...
amilli = list(range(1,1000001))
#for num in amilli:
 #   print (num)

#4.4 adding and also finding the min and max in the amilli list
print(min(amilli))
print(max(amilli))
print(sum(amilli))
#Make a dictionary containing three major rivers and the country river runs through.
Rivers = {'brazil':'amazon','egypt':'nile','kenya':'tana-athi','usa':'mississipi'}

#Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

for k, v in Rivers.items():
    print(f" The {v}  runs through {k}")
for country in Rivers:
    print(country)

for river in Rivers.values():
    print(river)
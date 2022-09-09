#maybe a game scenario
#using dictionaries,we want to update the speed of a moving targte
alien = {'x_position': 0,'y_position': 25,'speed': 'medium'}
print (f"original position of the alien is:{alien['x_position']}")

if alien["speed"] == "slow":
    x_incr = 1
elif alien["speed"] == "medium":
    x_incr = 2
else:
    x_incr = 3

alien["x_position"] = alien["x_position"] +  x_incr
print(alien["x_position"])


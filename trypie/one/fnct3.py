#FOR FUNCTION OVERLOADING HIVI...
def city(president,country,colonizer = ''):
    if colonizer:
        print(f"The CIC of {country} and the  president is {president} ,however the colonizer was {colonizer} ")
    else:
        print(f"The CIC of {country.title()} is {president.title()}")

city('omar waka','Kenya','British are cumming')
city('omar wakah','Kenya')xit

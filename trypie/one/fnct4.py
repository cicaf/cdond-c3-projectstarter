##### function that accjoepts all names and age and occupation...

def persona(name1,name2,occupation = None,age = None):

    mtu = {'1st':name1,'2nd':name2}
    if occupation and age:
        mtu = {'1st':name1,'2nd':name2, 'kazi':occupation,'miaka':age}
    elif occupation:
        mtu['kazi'] = occupation
    else:
        mtu['miaka'] = age
        
    print(mtu)

persona('Omar','Wakah','president','39')
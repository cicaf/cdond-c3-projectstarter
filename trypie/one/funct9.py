###A function with multiple arguements...
def person(name1,name2,**user_info):
    user_info['firstname'] = name1
    user_info['lastname'] = name2
    return user_info

this = person('John','Muyale',career='civil engineer',finance='wealthyluhyaman2')
print(this)
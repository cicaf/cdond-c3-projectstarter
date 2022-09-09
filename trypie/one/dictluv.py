guys = {'ann':'ui-ux','rae':'legal work','tijo':'c','omar':'devops'}
couple = {'rae','omar'}

for name in guys:
    print (name)
    if name in couple :
        language = guys[name]
        print(f"hi {name} you work in {language}")
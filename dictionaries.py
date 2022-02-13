alien ={'color':'green','points':5}
print(alien['color'])
#print(f"you have {points} point")

name={}
name['fname']="Taha"
name['lname']="Azam"
print(name)



check = name.get('point','Not found')
print(check)

for key in name.keys():
    print(key)
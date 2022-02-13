bicycle = ['trek','redline']
print(bicycle)

names = ['string', 1,6.5,['1','bicycle']]
print(names)

print(names[:])

message = f"My first bick was {bicycle[0].title()}"

name = ['Taha','Azam']
for i in name:
    print(f"hello {i}")

name[0] = 'Muhammad'

print(name)

name.append('Taha')
print(name)

name.insert(1,"Taha")
print(name)


name.pop()

del name[0]
print(name)

name.sort()
print(name)

# name.sort(reverse=True)
# print(name)

name.reverse()
print(name)

print(name)
'/n'.join (name)


for i in range(0,100,10):
    print(i)


for j in range (0, len(name),1):
    print(name)
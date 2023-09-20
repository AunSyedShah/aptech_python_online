random = ['saqib',5,48,'moiz','waleed',19]
lenght  =  len(random)
intlist = []
strlist = []

for a in range(lenght):
    if isinstance(random[a], int):
        intlist.insert(a,random[a])
    else:
        strlist.insert(a,random[a])
print("Random Data type List")
print(random)
print("Int type List")
print(intlist)
print("String type List")
print(strlist)
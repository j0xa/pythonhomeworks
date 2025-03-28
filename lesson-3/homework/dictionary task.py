#1
x={'name':"jahongir", 'lname':"Abdirashitov", 'age':18}
a=str(input("what u want"))
print(x[a])

#2
x={'name':"jahongir", 'lname':"Abdirashitov", 'age':18}
a=str(input("what u want"))
if a in x:
    print("yes")
else:print("no")

#3
x={'name':"jahongir", 'lname':"Abdirashitov", 'age':18}
count=0
for i in x:
    count+=1
print(count)

#4
x={'name':"jahongir", 'lname':"Abdirashitov", 'age':18}
for i in x:
    print(i)

#5
x={'name':"jahongir", 'lname':"Abdirashitov", 'age':18}
for i in x:
    i=str(i)
    print(x[i])

#6
x={'name':"jahongir", 'lname':"Abdirashitov", 'age':18}
y={"email":"asdf@gmail.com"}
x.update(y)
print(x)

#7

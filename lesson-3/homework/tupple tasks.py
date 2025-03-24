#q1
x=(1,2,3,4,5,6,7,8,9,0)
print(x.count(1))

#q2
x=(1,2,3,4,5,6,7,8,9,0)
print(max(x))

#q3
x=(1,2,3,4,5,6,7,8,9,0)
print(min(x))       

#q4
x=(1,2,3,4,5,6,7,8,9,0)
y=int(input("Enter a number: "))
if y in x:
    print("Yes")
else:
    print("No")

#q5
x=(1,2,3,4,5,6,7,8,9,0)
print(x[0])

#q6 
x=(1,2,3,4,5,6,7,8,9,0)
print(x[-1])

#q7
x=(1,2,3,4,5,6,7,8,9,0)
print(len(x))

#q8
x=(1,2,3,4,5,6,7,8,9,0)
y=x[0:3]
print(y)

#q9
x=(1,2,3,4,5,6,7,8,9,0)
y=(0,9,8,7,6,5,4,3,2,1)
x.extend(y)
print(x)

#q10
x=(1,2,3,4,5,6,7,8,9,0)
if len(x)==0:
    print("Empty")
else:
    print("Not empty")


#q11
x=(1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0)
y=int(input("Enter a number: "))
for i in range(len(x)):
    if x[i]==y:
        print(i)
        continue

#q12
x=(1,2,3,4,5,6,7,8,9,0)
x.remove(max(x))
print(max(x))

#q13
x=(1,2,3,4,5,6,7,8,9,0) 
x.remove(min(x))
print(min(x))

#q14
x=(1,)
print(type(x))

#q15    
x=[1,2,3,4,5,6,7,8,9,0]
x=tuple(x)
print(type(x))

#q16
x=(1,2,3,4,5,6,7,8,9,0)
y=sorted(x)
if x==y:
    print("Yes")
else:    
    print("No")
    
#q17
x=(1,2,3,4,5,6,7,8,9,0)
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
y=x[a:b]
print(max(y))

#q18
x=(1,2,3,4,5,6,7,8,9,0)
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
y=x[a:b]
print(min(y))

#q19
x=(1,1,2,3,4,5,6,7,8,9,0)
y=list(x)
y.remove(1)
print(tuple(y))

#q20
x=(1,2,3,4,5,6,7,8,9,0),
y=(0,9,8,7,6,5,4,3,2,1),
z=x+y
print(z)

#q21
x=(1,2,3,4,5,6,7,8,9,0)
y=int(input("Enter a number: "))
x=list(x)
x=x*y
print(tuple(x))

#q22
x=int(input("Enter a number: "))
y=list(range(1,x+1))
y=tuple(y)
print(y)   

#q23
x=(1,2,3,4,5,6,7,8,9,0)
x=list(x)
x.reverse()
print(tuple(x))

#q24
x=(1,2,3,4,5,6,7,8,9,0)
y=list(x).reverse()
if x==y:
    print("Yes")
else:        
    print("No")

#q25
x=(1,2,3,4,5,4,6,8,3,1,6,7,8,9,0)
y=list()
x=list(x)
for i in range(len(x)):
    if x.count(x[i])==1:
        y.append(x[i])
print(tuple(y))

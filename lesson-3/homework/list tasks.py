n=int(input("enter the number of items to be entered: "))
a = [input(f"Enter element {i+1}: ") for i in range(n)]
if n==0:
    print("the list is empty")
else:
    print(a[0])
    print(a[-1])
newlist=a[0:3]
print(newlist)
print(sorted(a, reverse=True))
a.sort()
print(a)
b=list(set(a))
print(b)
c=input("Enter the item to be added: ")
a.append(c)
print(a)
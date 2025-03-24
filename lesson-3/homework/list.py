#q1
mylist=["apple", "brown", "carry","weapon", "apple"]
item=input("Enter the item to be searched: ")
count=0
for i in mylist:
    if i==item:
        count=count+1
print(count)

#q2-4
list=[1,2,3,4,5,6,7,8]
count=0
for i in list:
    count=count+i
print(count)
print(max(list))
print(min(list))

#q5
x=["and", "bro", "cmon"]
z=input("Enter the item to be searched: ")
if z in x:
    print("Yes, it is present")
else:
    print("No, it is not")

#q6-12
n=int(input("enter the number of items to be entered: "))
a = [input(f"Enter element {i+1}: ") for i in range(n)]
if n==0:
    print("the list is empty")
else:
    print(a[0])
    print(a[-1])
newlist=a[0:3]
print(newlist)
reverse=a[::-1]
print(reverse)
a.sort()
print(a)
b=list(set(a))
print(b)
c=input("Enter the item to be added: ")
a.append(c)
print(a)




#q13-14
itemnum=int(input("enter the number of items to be entered: "))
neuList = [input(f"Enter element {i+1}: ") for i in range(itemnum)]
search=input("Enter item whose index you need: ")
index=neuList.index(search)
print("index", index)
print(len(neuList)==0)

#q15-16
ran=int(input("enter the number of items to be entered: "))
numbers = [int(input(f"Enter element {i+1}: ")) for i in range(ran)] 
count_even=0
count_odd=0
for i in numbers:
    if i%2==0:
        count_even=count_even+1
    else:
        count_odd=count_odd+1
print("even: ", count_even)
print("odd: ", count_odd)
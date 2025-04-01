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

#17
list2 = [2,6,3,4,6,9,1,5]
new_list = lst.extend(list2)
new_list


#18
sub_list = [2,4,5]
sub_list in lst

#19
another_element = 7
for i in range(len(lst)):
    if(lst[i]==element):
        lst[i]=another_element

#20
unique_list.remove(max(unique_list))
second_largest = max(unique_list)

#21
unique_list.remove(min(unique_list))
second_smallest = min(unique_list)

#22
even_numbers = lst
for num in even_numbers:
    if(num%2==1):
        even_numbers.remove(num)
#23
odd_numbers = lst
for num in even_numbers:
    odd_numbers.remove(num)

#24
list_length = len(lst)

#25
list_copy = lst.copy()

#26
if(len(lst)%2==1):
    print(lst[int((len(lst)+1)/2)])
else:
    print(lst[int(len(lst)/2)]," ", lst[int(len(lst)/2+1)])
#27
start = 2
end = 5
max_of_sublist = max(lst[start:end+1])
#28
min_of_sublist = min(lst[start:end+1])
#29
lst.remove(lst[index])
lst
#30
lst==lst.sort()

#31
number = 2
repeated_list = []
for num in lst:
    for i in range(number):
        repeated_list.append(num)

#32
merged_list = lst
merged_list.extend(sorted(list2))
#33
for j in range(len(lst)):
    if(lst[j]==element):
        print(j)

#34
rotated_list = [lst[-1]]
for k in range(len(lst)-1):
    rotated_list.append(lst[k])
rotated_list
#35
range_list = []
for num in range(start,end+1):
    range_list.append(num)
range_list
#36
sum_of_positive=0
for num in lst:
    if(num>0):
        sum_of_positive+=num
sum_of_positive

#37
sum_of_negative=0
for num in lst:
    if(num<0):
        sum_of_negative+=num
sum_of_negative

#38
lst == lst.reverse()

#40
unique_list_inorder = []
uniq = list(set(lst))
for a in uniq:
    if(lst.count(a)==1):
        unique_list_inorder.append(a)
unique_list_inorder
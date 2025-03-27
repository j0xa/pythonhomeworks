list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
list3=[]
for i in range(len(list1)):
    if list1[i] not in list2:
        list3.append(list1[i])
for i in range(len(list2)):
    if list2[i] not in list1:
        list3.append(list2[i])
print(list3)
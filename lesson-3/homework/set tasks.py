
#1
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
set1|set2

#2
set1&set2

#3
set1-set2

#4
set2 in set1
#5
element = 8
element in set1


#6
len(set1)

#7
list_set = [1,2,2,3,4,4,5,5,6]
set(list_set)
#8
if(element in set1):
    set1.remove(element)
#9
set3 = {4,1,2,7,8,0,5,7,2,1,5}
empty_set = set3.clear()

#10
set1 != {}

#11
(set1|set2)-(set1&set2)

#12
set1.add(element)

#13
set1.pop()
#14
max(set1)
#15
min(set1)

#16
even_set = list(set1)
for num in even_set:
    if(num%2==1):
        even_set.remove(num)
even_set = set(even_set)

#17
odd_set = set1-even_set

#18
range_set = []
for k in range(10):
    range_set.append(k+1)
range_set = set(range_set)

#19
set1^set2

#20
set1&set2=={}

#21
list_to_set = [1,1,2,2,3,4,5]
list(set(list_to_set))
#22
len(set(list_to_set))

#23
import random
random_set = []
while(len(set(random_set))<6):
    rand = random.randint(1,10)
    random_set.append(rand)
set(random_set)
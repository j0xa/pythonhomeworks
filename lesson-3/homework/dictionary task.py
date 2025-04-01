
#1
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer",
    "hobby": "Reading",
    "language": "Python"
}
my_dict["age"]

#2
key = "city"
key in my_dict

#3
len(my_dict.keys())
#4
keys = my_dict.keys()

#5
values = my_dict.values()

#6
my_dict2 = {
    "favorite_color": "Blue",
    "pet": "Cat",
    "favorite_food": "Pizza"
}
merged_dict = my_dict
merged_dict.update(my_dict2)
merged_dict

#7
my_dict.pop(key)
my_dict


#8
my_dict2.clear()

#9
my_dict2 != {}

#10
if key in my_dict:
    key_value = {key: my_dict[key]}
else:
    print("Key does not exist")
#11
new_key = "age"
new_value = "31"
my_dict[new_key]= new_value
my_dict

#12
my_dict_values = list(my_dict.values())
my_dict_values.count(new_value)

#13
swap_list = list(my_dict.items())
swap_list.reverse()
dict(swap_list)

#14
keys_list = []
for d in list(my_dict.keys()):
    if my_dict[d]==new_value:
        keys_list.append(d)
keys_list

#15
new_dict = {}
list_keys = ["apple","banana","cherry"]
list_values = ["olma","banan","olcha"]
for i in range(len(list_keys)):
    new_dict.update({list_keys[i]:list_values[i]})
new_dict

#16
values_dict = list(my_dict.values())
for v in values_dict:
    if type(v)==dict:
        print("yes")
else:
    print("no")

#17
nested_dict = {"dict1":{"nested":"value"},"dict2":{"apple":"olma"}}
nest_val = dict(nested_dict["dict1"])
val = nest_val["nested"]
val

#18
kys=["key1","key2","key3"]
default_dict = {}
for k in kys:
    default_dict.update({k:"def_value"})
default_dict

#19
uniq_dict = {"key1":2,"key2":4,"key3":1,"key4":3,"key5":5,"key6":4}
vl = list(uniq_dict.values())
len(set(vl))

#20
dct = {"bbb":"ccc","aaa":"bbb","ddd":"aaa","ccc":"ddd"}
dct_keys = sorted(list(dct.keys()))
dct_sort_key = {}
for i in range(len(dct_keys)):
    dct_sort_key.update({dct_keys[i]:dct[dct_keys[i]]})
dct_sort_key

#21
dct_sort_val = dict(sorted(dct.items(), key=lambda item: item[1]))
dct_sort_val

#22
dict1 = {"key1":2,"key2":4,"key3":1,"key4":3,"key5":5,"key6":4}
new_dict1 = {}
for ky in list(dict1.keys()):
    if (dict1[ky]>2):
        new_dict1.update({ky:dict1[ky]})
new_dict1

#23
dct1 = {"apple":"olma","cherry":"olcha","kiwi":"kivi"}
dct2 = {"banana":"banan","kiwi":"kiwi","apricot":"olxo'ri"}
for i in list(dct1.keys()):
    if i in list(dct2.keys()):
        print("yes, there is a common key")
        break
else:
    print("no common keys found")

#24
tuple_to_dict = (["key1",2],["key2",4],["key3",1],["key4",3],["key5",5],["key6",4])
tple2dct = {}
for pair in tuple_to_dict:
    tple2dct.update({pair[0]:pair[1]})
tple2dct

#25
dd = {"key1":2,"key2":4,"key3":1,"key4":3,"key5":5,"key6":4}
list(dd.items())[0]
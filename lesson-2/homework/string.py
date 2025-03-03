
#q18 
j=str(input("Entrer the sentence: "))
k=j.split()
last=k[-1]
erste=k[0]
if erste==last:
    print("ends and starts with the same words")
else:
    print("they dont")
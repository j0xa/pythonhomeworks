step1=[]
for i in range(2,101):

    is_prime=True
    for x in range(2,int(i/2)):
        if i%x==0:
            is_prime=False
            break
    if is_prime:
        step1.append(i)
print(step1)
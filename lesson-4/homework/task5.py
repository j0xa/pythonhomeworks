password=str(input("enter your password: "))
l=False
c=False
if len(password)<=8:
    print("Too short")
else:l=True
if password.lower()==password:
    print("At least one uppercase required")
else:c=True
if c==True and l==True:
    print("Everything good")
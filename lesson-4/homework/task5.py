password=str(input("enter your password: "))
if len(password)<=8:
    print("Too short")
    count=0
    for char in password:
        if password[count].isupper()==False:
            print("At least one uppercase required")
            break
else:print("eveything good")
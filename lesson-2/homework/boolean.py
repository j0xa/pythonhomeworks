#q1
username=str(input("Enter the username: "))
password=str(input("Enter the password: "))
if not bool(username.strip()) or not bool(password.strip()):
    print("fill up the blank space")

#q2
first=int(input("enter the first nnumber: "))
second=int(input("enter the second number: "))
if bool(first==second):
    print("theyre the same number")

#q3
number=int(input("Enter the number: "))
if bool(number%2==0) and bool(number>0):
    print('it is positive and even')
else:print("it is not positive and even")

#q4
num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))
num3=int(input("Enter the 3rd number: "))
if bool(num1!=num2) and bool(num2!=num3) and bool(num1!=num3):
    print("theyre different")
else:
    print("theyre not different")

#q5
txt1=str(input("Enter the text 1: "))
txt2=str(input("Enter the text 2: "))
if bool(len(txt1)==len(txt2)):
    print("they have the same length")
else: print("they have different length")

#q6
a=int(input("Enter the number: "))
if bool(a%3==0) and bool(a%5==0):
    print(" it is divisible by both 3 and 5")
else:
    print(" it is not divisible by both 3 and 5")

#q7
b=float(input("enter the number: "))
c=float(inout("Enter the number: "))
d=c+b
if bool(d>50.8):
    print("Their summ is greate than 50.8")
else:
    print("Their summ is not greate than 50.8")

#q8
e=float(input("enter the number"))
if bool(e>10)and bool(e<20):
    print("the given number is in between 10 and 20")
else:print("it is not between 10 and 20")
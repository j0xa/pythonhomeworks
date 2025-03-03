#q1
a=float(input("enter a: "))
print(f"{a:.2f}")

#q2
num1=float(input("enter first number: "))
num2=float(input("enter second number: "))
num3=float(input("enter third number: "))
print(f"Max: {max(num1, num2, num3)}")
print(f"Min: {min(num1, num2, num3)}")

#q3
km=float(input("Enter the distance in kilometers: "))
m=km*1000
cm=m*100
print(m," meters")
print(cm, " centimeters")

#q4
b=float(input("enter b: "))
c=float(input("enter c: "))
d=b%c
e=b//c
print("reaminder is: ", d)
print("division is: ", e)

#q5
temp=float(input("enter the temperature in celsius: "))
F=temp*1.8+32
print("your temperature in farenheit is: ", F)

#q6
f=int(input("enter the whole number: "))
g=repr(f)
print(g[-1])

#q7
Zahle=int(input("Enter the number: "))
if Zahle%2==0 and Zahle!=0:
    print("its even")
elif Zahle%2==1:
    print("its odd")
else:print("its zero")
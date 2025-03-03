#q1
name=str(input("Enter your name: "))
year=int(input("Enter your year of birth: "))
age=2025-year
print("You are ",name, " and you are", age, "years old")

#q2

#q3
text=str(input("Enter your text: "))
print(len(text))
print(text.lower())
print(text.upper())

#Q4
word=str(input("Enter your word: "))
if word==word[::-1]:
    print("your word is palindrome")
else:
    print("It is not a palindrome")

#q5
vowel=0
consonant=0
my_str=str(input("Enter your word:"))
vowels="euioa"
for i in my_str.strip():
    if i in vowels:
        vowel=vowel+1
    else:
        consonant=consonant+1
print(vowel)
print(consonant)

#q6
first=str(input("Enter your main text: "))
second=str(input("Enter the word to be searched: "))
if second in first:
    print("string found")
else:
    print("not found")

#q7
sentence=str(input("Enter the sentence: "))
word=str(input("enter the word:"))
replacement=str(input("enter the word:"))
print(sentence.replace(word, replacement))

#q8
txt=str(input("enter the text: "))
start=txt[0]
end=txt[-1]
print(start)
print(end)

#q9
ent=str(input("enter the text: "))
print(ent[::-1])

#q10
text=str(input("Enter the text: "))
count=len(text.split())
print(count)

#q11
digits="1234567890"
q=input("enter the stuff: ")
t=0
for i in q:
    if i in digits:
        t=t+1
    else:
        t=t
if t!=0:
    print("there is a digit")
else:
    print("there is no digit")

#q12
y=str(input("enter the sentence: "))
u=[" ",",","."]
for i in y:
    if i in u:
        y=y.replace(i,"")
print(y)

#q13
o=str(input("Enter the text: "))
p=o.replace(" ", "")
print(p)

#q14
idk=str(input("enter the first: "))
idkk=str(input("enter the second: "))
if idk==idkk:
    print("theyre same")
else:
    print("theyre different")

#q15
full=str(input("enter the full form: "))
acr="".join(x[0].upper() for x in full.split())
print(acr)

#q16
g=str(input("Enter the string: "))
char=str(input("Enter the char to remove: "))
g=g.replace(char, "")
print(g)

#q17
h=str(input("enter the text: "))
chara=str(input("enter the character to be removed: " ))
print(h.replace(chara, ""))

#q18 
j=str(input("Entrer the sentence: "))
k=j.split()
last=k[-1]
erste=k[0]
if erste==last:
    print("ends and starts with the same words")
else:
    print("they dont")
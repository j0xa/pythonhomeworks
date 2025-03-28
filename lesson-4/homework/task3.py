txt = str(input("Enter the text: "))
txt = list(txt)
vowels="aeuioAEUIO"
changes = []
for i in range(len(txt)):
    if (i + 1) % 3 == 0 and txt[i] not in vowels and i+1!=len(txt):
        changes.append(i + 1)
    elif (i+1)%3==0 and txt[i] in vowels and i+1!=len(txt):
        changes.append(i+2)
for c in reversed(changes):
    txt.insert(c, "_")
print("".join(txt))
print(changes)

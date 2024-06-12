a= input("1")
b = int(input("2"))
text =""
for i in a:
    c = ord(i) + b
    if c > 122:
        c = c%122      
    text += chr(c)
print(text)
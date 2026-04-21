mega=list(input())
a=int(mega[0])
c=int(mega[-1])
b=str(mega[2])

# print(a,b,c)

if b==">":
    if a>c:
        print("Right")
    else:print("Wrong")
elif b=="=":
    if a==c:
        print("Right")
    else:
        print("Wrong")
else:
    if a<c:
        print("Right")
    else:
        print("Wrong")
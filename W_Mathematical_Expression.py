a,b,c,d,e = input().split()
a,c,e = int(a), int(c), int(e)
if b=="+":
    if (a+c)==e:
        print("Yes")
    else:
        print(a+c)
elif b=="-":
    if (a-c)==e:
        print("Yes")
    else:
        print(a-c)
else:
    if (a*c)==e:
        print("Yes")
    else:
        print(a*c)
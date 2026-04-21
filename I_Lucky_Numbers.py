mega=list(input())
a1=int(mega[0])
a2=int(mega[1])

if (a1%a2==0 and a2!=0) or (a2%a1==0 and a1!=0):
    print("YES")
else:
    print("NO")

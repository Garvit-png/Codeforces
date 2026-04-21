a,b,c,d=map(int,input().split())
mega=(a*b*c*d)
if mega%100!=0:
    if mega%100<10:
        print(0,mega%100,sep="")
    else:
        print(mega%100)
else:
    print("00")
a,b,c=map(int,input().split())
if a%c==0 and b%c==0:print("Both")
elif (a%c==0 and b%c!=0 ):
    print("Memo")
elif (a%c!=0 and b%c==0):
    print("Momo")
else:
    print("No One")
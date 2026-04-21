a,b,c=map(int,input().split())
if (max(a,b,c)-min(a,b,c)>=10):
    print("check again")
else:
    sumy=a+b+c
    maxi=max(a,b,c)
    mini=min(a,b,c)
    print("final",sumy-(maxi+mini))
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    
    if a % 2 != 0:
        print("NO")
    else:
        print("YES")
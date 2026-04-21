a=int(input())
year=0
month=0

while a>=30:
    if a>=365:
        year+=1
        a-=365
    elif a>=30:
        month+=1
        a-=30
    

print(year,"years")
print(month,"months")
print(a,"days")
    

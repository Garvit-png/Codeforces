# a=float(input())
# value=int(a)+0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

# if (a-value)==0:print("int",int(a))
# else:
#     print("float",int(a),round(a-value,3))


a = float(input())
if a % 1 == 0:
    print("int", int(a))
else:
    print("float", int(a), round(a % 1, 3))
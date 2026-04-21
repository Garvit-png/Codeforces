a=float(input())
if 0<=a<=25:
    print("Interval [0,25]")
elif 25<a<=50:
    print("Interval (25,50]")
elif 50<a<=75:
    print("Interval (50,75]")
elif 75<a<=100:
    print("Interval (75,100]")
else:
    print("Out of Intervals")
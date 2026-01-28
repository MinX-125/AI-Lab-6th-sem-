num=int(input("Enter number:"))
if 0<=num<=9 or -9<=num<=0:
    print("Single digit")
elif 10<=num<=99 or -99<=num<=-10:
    print("Two digit")
elif 100<=num<=999 or -999<=num<=-100:
    print("Three digit")
else:
    print("More than three digits")

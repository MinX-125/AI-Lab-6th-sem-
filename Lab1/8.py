a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a+b>c and a+c>b and b+c>a:
    print("Triangle is possible")
else:
    print("Triangle is not possible")

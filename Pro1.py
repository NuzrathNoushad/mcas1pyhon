#find area of triangle
a=float(input("Enter ist numbers"))
b=float(input("Enter 2nd number"))
c=float(input("Enter 3rd number"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("area of triangle is;",area)

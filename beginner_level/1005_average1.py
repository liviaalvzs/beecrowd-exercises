# Read two floating points' values of double precision A and B, corresponding to two student's 
# grades. After this, calculate the student's average, considering that grade A has weight 3.5 
# and B has weight 7.5. Each grade can be from zero to ten, always with one digit after the 
# decimal point.


a=float(input())
b=float(input())

print("MEDIA = %.5f" % (((a*3.5)+(b*7.5))/11))
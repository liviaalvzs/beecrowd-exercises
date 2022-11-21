''' Make a program that reads three floating point values: A, B and C. Then, calculate and show:
a) the area of the rectangled triangle that has base A and height C.
b) the area of the radius's circle C. (pi = 3.14159)
c) the area of the trapezium which has A and B by base, and C by height.
d) the area of ​​the square that has side B.
e) the area of the rectangle that has sides A and B. '''

num1,num2,num3=map(float,input().split()) 

pi=3.14159


a=(num1*num3)/2
b=pi*(num3*num3)
c=num3*(num1+num2)/2
d=num2*num2
r=num1*num2


print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" % (a, b, c, d, r))
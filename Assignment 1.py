pi = int(3.142)#taking pi as a constant
g = int(9.125)#taking g as a gravitational constant

#calculating the area of a semi-circle
print("This Program calculates the area of a semicircle")
radius = int(input("enter radius "))
area = 0.5 * pi * radius * radius #area of a semicircle
print("the area of the semicircle is ", area)

#cal;culating the force of an object falling down
print("This program calculates the force of a falling objects ")
mass = int(input("enter mass"))
force = g * mass
print("the force of the falling object is ", force)

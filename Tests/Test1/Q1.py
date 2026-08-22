lenght = float(input("Enter the length of rectangle:"))
breadth= float(input("Enter the breadth of rectangle:"))
radius= float(input("Enter the radius of semicircle:"))

R_area=lenght*breadth
S_area=0.5*3.14*radius*radius
total_area=R_area+S_area
perimeter=(2*lenght)+breadth*(3.14*radius)
print("Area=",total_area)
print("perimeter=",perimeter)
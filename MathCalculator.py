print("This program will calculate the area of various shapes")
print("It can calculate squares, rectangles, circles and triangles")

shape = input("What shape would you like to calculate \n")

if shape == "square": 
	square_side = float(input("What is its side length? \n"))
	square_area = square_side * square_side
	print("The area of this square is", square_area, "!")
	
elif shape == "rectangle": 
	rectangle_width = float(input("what is its width? \n"))
	rectangle_length = float(input("what is its length? \n"))
	rectangle_area = rectangle_length * rectangle_width
	print ("The area of this rectangle is", rectangle_area, "!")

elif shape == "circle":
	radius = float(input("what is its radius? \n"))
	circle_area = radius * radius * 3.14
	print ("The area of this circle is", circle_area, "!")


elif shape == "triangle": 
	base = float(input("what is its base? \n"))
	altitude = float(input("what is its altitude? \n"))
	triangle_area = (base * altitude)/2 
	input(altitude)
	print((base * altitude)/2)

else: print("Please try again...")








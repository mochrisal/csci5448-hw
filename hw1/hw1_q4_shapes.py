"""
Implementation of an object oriented program that implements creating various Shapes

author: Morgan Allen
course: csci 5448 Object Oriented Analysis and Design
due date: 2/1/2019
"""

# ======================================================================================================================
# === Class Definitions ================================================================================================
# ======================================================================================================================

# Parent Shape Class
class Shape(object):
    def __init__(self, name, sides):
        self.name = name
        self.sides = sides

    def __repr__(self):
        return "I am a Shape called {} with {} sides".format(self.name, self.sides)

# Circle Class
class Circle(Shape):
    def __init__(self):
        Shape.__init__(self, "Circle", "infinite")

    def display(self):
        print("This is a method to display a Circle.")

# Triangle Class
class Triangle(Shape):
    def __init__(self):
        Shape.__init__(self, "Triangle", 3)

    def display(self):
        print("This is a method to display a Triangle")

# Square Class
class Square(Shape):
    def __init__(self):
        Shape.__init__(self, "Square", 4)

    def display(self):
        print("This is a method to display a Square.")

# ======================================================================================================================
# === Main Program =====================================================================================================
# ======================================================================================================================

# Create a collection of shapes through instantiation
c = Circle()
t = Triangle()
s = Square()

# Create a 'database' of these shapes
database = [c,t,s,t,s,c,c,t,s,c,t,s,s]

# Print number of shapes in the 'database'
print("There are {} shapes in database.".format(len(database)))
print('\n')

# Print each shape in the 'database'
print("Printing each shape in database")
for shape in database:
    print(shape)
print('\n')

# Call the display() function for each shape in the 'database'
print("Calling display() function of each shape in database")
for shape in database:
    shape.display()
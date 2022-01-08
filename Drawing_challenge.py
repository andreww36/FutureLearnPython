# task 1.9: Create a drawing using rectangles, ovals, and triangles.
from shapes import Paper, Triangle, Rectangle, Oval
paper = Paper()
# draw 4 trianges
tri1 = Triangle(200, 50, 525, 300, 200, 550, color='red')
tri2 = Triangle(400, 50, 75, 300, 400, 550, color='red')
tri3 = Triangle(50, 200, 550, 200, 300, 525, color='red')
tri4 = Triangle(50, 400, 550, 400, 300, 75, color='red')
tri1.draw()
tri2.draw()
tri3.draw()
tri4.draw()

# draw 3 squares
square1 = Rectangle(width=350, height=350, x=125, y=125, color='blue')
square2 = Rectangle(width=250, height=250, x=175, y=175, color='red')
square3 = Rectangle(width=150, height=150, x=225, y=225, color='blue')
square1.draw()
square2.draw()
square3.draw()

# draw 4 ovals
oval1 = Oval(width=100, height=300, x=250, y=150, color='yellow')
oval2 = Oval(width=300, height=100, x=150, y=250, color='yellow')
oval3 = Oval(width=50, height=200, x=275, y=200, color='green')
oval4 = Oval(width=200, height=50, x=200, y=275, color='green')
oval1.draw()
oval2.draw()
oval3.draw()
oval4.draw()
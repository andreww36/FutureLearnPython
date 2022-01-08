# This code requires Python 3 and tkinter (which is usually installed by default)
# This code will NOT work on trinket.io as the tkinter module is not supported
# Raspberry Pi Foundation 2020
# CC-BY-SA 4.0

try:
    from tkinter import Tk, Canvas, BOTH
except ImportError:
    raise Exception("tkinter did not import successfully - check you are running Python 3 and that tkinter is available.")

import random


class Paper():

    # the tk object which will be used by the shapes
    tk = None

    def __init__(self, width=600, height=600):
        """
        Create a Paper object which is required to draw shapes onto.

        It is only possible to create 1 Paper object.

        Args:
            width (int): The width of the display. Defaults to 600.
            height (int): The height of the display. Defaults to 600.

        Returns:
            Paper: A Paper object
        """

        if Paper.tk is not None:
            raise Exception("Error: Paper has already been created, there can be only one.")

        try:
            Paper.tk = Tk()
        except ValueError:
            raise Exception("Error: could not instantiate tkinter object")

        # Set some attributes
        Paper.tk.title("Drawing shapes")
        Paper.tk.geometry(str(width)+"x"+str(height))
        Paper.tk.paper_width = width
        Paper.tk.paper_height = height

        # Create a tkinter canvas object to draw on
        Paper.tk.canvas = Canvas(Paper.tk)
        Paper.tk.canvas.pack(fill=BOTH, expand=1)

    def display(self):
        """
        Displays the paper
        """
        Paper.tk.mainloop()

class Shape():

    # Constructor for Shape
    def __init__(self, width=50, height=50, x=None, y=None, color="black"):
        """
        Creates a generic 'shape' which contains properties common to all
        shapes such as height, width, x y coordinates and color.

        Args:
            width (int): The width of the shape. Defaults to 50.
            height (int): The height of the shape. Defaults to 50.
            x (int): The x position of the shape. If None, the x position will be the middle of the screen. Defaults to None.
            y (int): The y position of the shape. If None, the y position will be the middle of the screen. Defaults to None.
            color (string): The color of the shape. Defaults to "black"
        """
        if Paper.tk is None:
            raise Exception("A Paper object has not been created. There is nothing to draw on.")

        # Set some attributes
        self.height = height
        self.width = width
        self.color = color

        # Put the shape in the centre if no xy coords were given
        if x is None:
            self.x = (Paper.tk.paper_width/2) - (self.width/2)
        else:
            self.x = x
        if y is None:
            self.y = (Paper.tk.paper_height/2) - (self.height/2)
        else:
            self.y = y

    # This is an internal method not meant to be called by users
    # (It has a _ before the method name to show this)
    def _location(self):
        """
        Internal method used by the class to get the location
        of the shape. This shouldn't be called by users, hence why its
        name begins with an underscore.
        """
        x1 = self.x
        y1 = self.y
        x2 = self.x + self.width
        y2 = self.y + self.height
        return [x1, y1, x2, y2]

    # Randomly generate what the shape looks like
    def randomize(self, smallest=20, largest=200):
        """
        Randomly generates width, height, position and color for a shape. You can specify
        the smallest and largest random size that will be generated. If not specified, the
        generated shape will default to a random size between 20 and 200.

        Args:
            smallest (int): The smallest the shape can be. Defaults to 20
            largest (int): The largest the the shape can be. Defaults to 200.

        """
        self.width = random.randint(smallest, largest)
        self.height = random.randint(smallest, largest)

        self.x = random.randint(0, Paper.tk.paper_width-self.width)
        self.y = random.randint(0, Paper.tk.paper_height-self.height)

        self.color = random.choice(["red", "yellow", "blue", "green", "gray", "white", "black", "cyan", "pink", "purple"])

    # Getters and setters for Shape attributes
    def set_width(self, width):
        """
        Sets the width of the shape.

        Args:
            width (int): The width of the shape
        """
        self.width = width

    def set_height(self,height):
        """
        Sets the height of the shape.

        Args:
            height (int): The height of the shape.
        """
        self.height = height

    def set_x(self, x):
        """
        Sets the x position of the shape

        Args:
            x (int): The x position for the shape.
        """
        self.x = x

    def set_y(self, y):
        """
        Sets the y position of the shape

        Args:
            y (int): The y position for the shape.
        """
        self.y = y

    def set_color(self, color):
        """
        Sets the color of the shape

        Args:
            color (string): The color of the shape.
        """
        self.color = color

    def get_color(self):
        """
        Returns the color of the shape

        Returns:
            color (string): The color of the shape
        """
        return self.color


# Rectangle class is a subclass of Shape
class Rectangle(Shape):

    # This is how to draw a rectangle
    def draw(self):
        """
        Draws a rectangle on the canvas. The properties of the rectangle
        can be set using the getter and setter methods in Shape
        """
        x1, y1, x2, y2 = self._location()

        # Draw the rectangle
        Paper.tk.canvas.create_rectangle(x1, y1, x2, y2, fill=self.color)


class Oval(Shape):

    def draw(self):
        """
        Draws an oval on the canvas. The properties of the oval
        can be set using the getter and setter methods in Shape
        """
        x1, y1, x2, y2 = self._location()

        # Draw the oval
        Paper.tk.canvas.create_oval(x1, y1, x2, y2, fill=self.color)


class Triangle(Shape):

    # Every constructor parameter has a default setting
    # e.g. color defaults to "black" but you can override this
    def __init__(self, x1=0, y1=0, x2=20, y2=0, x3=20, y3=20, color="black"):
        """
        Overrides the Shape constructor because triangles require three
        coordinate points to be drawn, unlike rectangles and ovals.

        Args:
            x1 (int): The x position of the coordinate 1. Defaults to 0.
            y1 (int): The y position of the coordinate 1. Defaults to 0.
            x2 (int): The x position of the coordinate 2. Defaults to 20.
            y2 (int): The y position of the coordinate 2. Defaults to 0.
            x3 (int): The x position of the coordinate 3. Defaults to 20.
            y4 (int): The y position of the coordinate 3. Defaults to 20.
            color (string): The color of the shape. Defaults to "black"
        """
        # call the Shape constructor
        super().__init__(color=color)

        # Remove height and width attributes which make no sense for a triangle
        # (triangles are drawn via 3 xy coordinates)
        del self.height
        del self.width

        # Instead add three coordinate attributes
        self.x = x1
        self.y = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def _location(self):
        """
        Internal method used by the class to get the location
        of the triangle. This shouldn't be called by users, hence why its
        name begins with an underscore.
        """
        return [self.x, self.y, self.x2, self.y2, self.x3, self.y3]

    def draw(self):
        """
        Draws a triangle on the canvas. The properties of the triangle
        can be set using the getter and setter methods in Shape
        """
        x1, y1, x2, y2, x3, y3 = self._location()
        # Draw a triangle
        Paper.tk.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=self.color)

    def randomize(self):
        """
        Randomly chooses the location of all 3 triangle points as well
        as the color of the triangle
        """
        # Randomly choose all the points of the triangle
        self.x = random.randint(0, Paper.tk.paper_width)
        self.y = random.randint(0, Paper.tk.paper_height)
        self.x2 = random.randint(0, Paper.tk.paper_width)
        self.y2 = random.randint(0, Paper.tk.paper_height)
        self.x3 = random.randint(0, Paper.tk.paper_width)
        self.y3 = random.randint(0, Paper.tk.paper_height)

        # Randomly choose a color of this triangle
        self.color = random.choice(["red", "yellow", "blue", "green", "gray", "white", "black", "cyan", "pink", "purple"])

    def set_width(self, width):
        """
        Sets the width of the shape.

        Args:
            width (int): The width of the shape
        """
        self.width = width

    def set_height(self,height):
        """
        Sets the height of the shape.

        Args:
            height (int): The height of the shape.
        """
        self.height = height


    # Change the behaviour of set_width and set_height methods for a triangle
    # because triangles are not drawn in the same way
    def set_width(self, width):
        """
        Overrides the setter method for width

        Args:
            width (int): The width of the shape
        """
        raise Exception("Width cannot be defined for Triangle objects")

    def set_height(self, height):
        """
        Overrides the setter method for height

        Args:
            height (int): The height of the shape
        """
        raise Exception("Height cannot be defined for Triangle objects")


# This if statement means
# "if you run this file (rather than importing it), run this demo script"
if __name__ == "__main__":

    my_drawing = Paper()

    # Random size and location triangle
    tri = Triangle()
    tri.randomize()
    tri.draw()

    # Specific size and location rectangle
    rect = Rectangle(height=40, width=90, x=110, y=20, color="yellow")
    rect.draw()

    # Default oval
    oval = Oval()
    oval.draw()

    # Oval with setters
    oval2 = Oval()
    oval2.set_height(200)
    oval2.set_width(100)
    oval2.set_color("fuchsia")
    oval2.set_x(30)
    oval2.set_y(90)
    oval2.draw()

    my_drawing.display()
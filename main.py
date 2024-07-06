from random import randint
import turtle


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rect):
        if rect.lower_left.x < self.x < rect.upper_right.x \
                and rect.lower_left.y < self.y < rect.upper_right.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, lower_left, upper_right):
        self.lower_left = lower_left
        self.upper_right = upper_right

    def area_of_rectangle(self):
        return ((self.upper_right.x - self.lower_left.x) *
                (self.upper_right.y - self.lower_left.y))


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        # goto certain coordinates
        canvas.penup()
        canvas.goto(self.lower_left.x, self.lower_left.y)
        canvas.pensize(5)
        canvas.pendown()
        canvas.color("blue")
        canvas.forward(self.upper_right.x - self.lower_left.x)
        canvas.left(90)
        canvas.color("green")
        canvas.forward(self.upper_right.y - self.lower_left.y)
        canvas.left(90)
        canvas.color("blue")
        canvas.forward(self.upper_right.x - self.lower_left.x)
        canvas.left(90)
        canvas.color("green")
        canvas.forward(self.upper_right.y - self.lower_left.y)


class GuiPoint(Point):

    def draw(self, canvas, size=10, color="red"):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


point1 = Point(randint(0, 99), randint(0, 99))
point2 = Point(randint(100, 200), randint(100, 200))
rectangle = GuiRectangle(point1, point2)

print(f"Rectangle Coordinates {rectangle.lower_left.x}, {rectangle.lower_left.y} and "
      f"{rectangle.upper_right.x}, {rectangle.upper_right.y}.")

try:
    value_of_x = int(input("guess x: ".upper()))
    value_of_y = int(input("guess y: ".upper()))
except Exception as err:
    print(err)

user_guess_point = GuiPoint(value_of_x, value_of_y)


choice = user_guess_point.falls_in_rectangle(rectangle)

if choice:
    print("great guess the point is in the rectangle.".title())
else:
    print("oops! your point is out of the rectangle.".title())

user_guessed_area = float(input("guess the area of rectangle: ".upper()))

if user_guessed_area == rectangle.area_of_rectangle():
    print("wow boy you have guessed the right area!".title())
else:
    print(f"your guess was way off by: {rectangle.area_of_rectangle() - user_guessed_area}".title())

myturtle = turtle.Turtle()
rectangle.draw(myturtle)
user_guess_point.draw(myturtle)
turtle.done()
print(rectangle.area_of_rectangle())

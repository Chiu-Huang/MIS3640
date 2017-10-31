from Point1 import *
import copy


class Circle:
    """Represents a circle.

    Attributes: center, radius
    """

def point_in_circle(point, circle):
    """Checks whether a point lies inside a circle (or on the boundary).

    point: Point object
    circle: Circle object
    """
    if (circle.center.x - circle.radius < point.x < circle.center.x + circle.radius) and (circle.center.y - circle.radius < point.y < circle.center.y + circle.radius):
        return True
    else:
        return False


def rect_in_circle(rect, circle):
    """Checks whether the corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """
    corner1 = (rect.corner.x + rect.width,rect.corner.y)
    corner2 = (rect.corner.x ,rect.corner.y + rect.height)
    corner3 = (rect.corner.x + rect.width,rect.corner.y + rect.height)
    if point_in_circle(rect.corner, circle) and point_in_circle(corner1, circle) and point_in_circle(corner2, circle) and point_in_circle(corner3, circle):
        return True
    else:
        return False

def rect_circle_overlap(rect, circle):
    """Checks whether any corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """
    corner1 = Point()
    corner1.x = rect.corner.x + rect.width
    corner1.y = rect.corner.y
    corner2 = Point()
    corner2.x = rect.corner.x 
    corner2.y = rect.corner.y + rect.height
    corner3 = Point()
    corner3.x = rect.corner.x + rect.width
    corner3.y = rect.corner.y + rect.height

    if point_in_circle(rect.corner, circle):
        return True
    elif point_in_circle(corner1, circle):
        return True
    elif point_in_circle(corner2, circle): 
        return True
    elif point_in_circle(corner3, circle):
        return True
    else:
        return False
    # point_in_circle(corner1,circle)
def main():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    print(box.corner.x)
    print(box.corner.y)

    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print(circle.center.x)
    print(circle.center.y)
    print(circle.radius)

    print(point_in_circle(box.corner, circle))
    print(rect_in_circle(box, circle))
    print(rect_circle_overlap(box, circle))


if __name__ == '__main__':
    main()

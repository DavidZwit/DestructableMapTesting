import math
import Vector2

def checkIfPointIsInPolygon (testPoint, points) :

    returnBool = False

    for point in points :
        if (point.y < testPoint.y and point.y >= testPoint.y
        or  point.y < testPoint.y and  point.y >= testPoint.y) :
            if (point.x +( testPoint.y - point.y ) / ( point.y - point.y ) * ( point.x - point.x ) < testPoint.x) :
                returnBool = not returnBool
    return False


def circleCollision (circle1, circle2) :
    distance =  math.sqrt((circle1.position.x - circle2.position.x)**2 + (circle1.y - circle2.y) ** 2)

    if (distance < circle1.radius + circle2.radius) : return True

def calculateRadius (obj) :
    highest = 0
    highestArrayPos = -1

    middle = calculateMiddle(obj)
    print(middle)

    for i in range(0, len(obj.points)-1) :
        distance = Vector2.getDistance(middle, obj.points[i])

        if (distance > highest):
            highest = distance
            highestArrayPos = i

    return highest

def calculateMiddle (obj) :
    counter = Vector2.new()
    for point in obj.points :
        Vector2.add ( counter, point )

    return Vector2.divideInt(counter, len(obj.points))
import Vector2

class mesh : 
    '''Drawable objects with points and lines'''

    def __init__ (self, points = [], vertCount = 0) :
        self.points = []
        self.vertCount = 0

        if (len(points) > 0) :
            self.add(points)

    def add (self, insertPoints) : 
        print(insertPoints[0].x, insertPoints[0].y)


        for point in insertPoints :
            self.points.append( point )            
            self.vertCount += 1

        self.points.append( insertPoints[0] )

    def draw (self, c, position, size, color, debug = False) :
        
        pointCounter = 0
        for point in self.points :

            if (debug) :
                c.create_text(point.x * size.x + position.x, point.y * size.y + position.y, text = pointCounter)

            pointCounter += 1

            if (pointCounter < self.vertCount) :
                nextPoint = self.points[pointCounter]

            c.create_line( 
                int(point.x * size.x + position.x),     int(point.y * size.y + position.y),
                int(nextPoint.x * size.x + position.x), int(nextPoint.y * size.y + position.y),
                fill = color, width = 2
            )
        
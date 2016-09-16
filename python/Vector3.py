from random import randint
import math

class new () :
    '''create a new vector2'''

    def __init__(self, x = 0, y = 0, z = 0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def log (self) :
        print(self.x, self.y, self.z)

    def normalize(self) :
        self.x = math.fabs(self.x)
        self.y = math.fabs(self.y)
        self.z = math.fabs(self.z)
    
    def __add__(self, other):
        '''Add a vector to a vector'''
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def mult(self, multiplication) :
        self.x *= multiplication
        self.y *= multiplication
        self.z *= multiplication

    def add(self, addition) :
        self.x += addition
        self.y += addition
        self.z += addition

    def addSelf(self, addVec) :
        self.x += addVec.x
        self.y += addVec.y
        self.z += addVec.z

    def rand(self, randOffsetX, randOffsetY, randOffsetZ) :
        '''Set vector to a random vector'''
        self.x = randint(-randOffsetX, randOffsetX)
        self.y = randint(-randOffsetY, randOffsetY)
        self.z = randint(-randoffsetZ, randoffsetZ)

    def distance(self, target) :
        '''calculate distance between vectors'''

        print("deze vector calculatie moet nog gefixt worden!!!")
        return math.sqrt( (target.x - self.x)**2 + (target.y - self.y)**2 )

    def nonRootedDistance(self, target) :
        '''calculate unrooted distence between to vectors'''
        print("deze vector calculatie moet nog gefixt worden!!!")
        
        return (target.x - self.x)**2 + (target.y - self.y)**2

    def copy(self) :
        return new(self.x, self.y, self.z)

    def offset(self, other) :
        return new(self.x - other.x, self.y - other.y, self.z - other.z)

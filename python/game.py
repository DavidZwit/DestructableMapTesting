import Vector2
import objects
import fileLoader
import collision

'''The dictionary with all the objects in the game in it'''
GameObjects = {}

class GridPos :
    
    def __init__ (self, position = Vector2.new()) :
        pos = position  

GameGrid = [[ Vector2.new() ] * 800  ] * 1200   

counter = Vector2.new()
counter.x = 0
for x in GameGrid :
    counter.x += 1
    counter.y = 0
    for y in x :
        counter.y+=1 

        y.x = counter.x
        y.y = counter.y

class GameObject :
    '''The global object used to make any object'''

    def __init__ (self, name, position = Vector2.new(), size = Vector2.new(), mesh = objects.mesh(), color = 'blue') :
        global GameObjects
        '''Dictionary for all the updates in this object'''
        self.updates = {}
        '''Dictionary for all the mashes in this object (the standard one included)'''
        self.meshes = {'mainMesh': mesh }
        '''The position of the object'''
        self.position = position
        '''The size of the object'''
        self.size = size
        '''The velocity (the speed at wich it moves)'''
        self.velocity = Vector2.new()
        '''The colour'''
        self.color = color
    
        '''If it's new add it to the GameObjects list else throw error'''
        if name not in GameObjects : 
            GameObjects[name] = self
        else : Exception('Gameobject already exists!!')

    def draw (self, c) :
        #draws all the meshes
        for mesh in self.meshes:
            self.meshes[mesh].draw(c, self.position, self.size, self.color, True)
        
    def update (self, inputs) :
        #adds velocity to the position
        
        Vector2.divideInt(self.velocity, 1.4)
        Vector2.add(self.position, self.velocity)

        #updates all the updates
        for funct in self.updates :
            self.updates[funct](self, inputs)


def createMesh (filePath, vertCount = 0) :
    '''Function that adds the object data to the game'''
    fileData = fileLoader.loadHTMLVector(filePath)

    return objects.mesh( fileData['points'] )



GameObject('bitmap', Vector2.new( 0, 0 ), Vector2.new(1, 1), )


GameObject('ground', Vector2.new(100, 300) , Vector2.new(1, 1), createMesh('objects/ground.html'), 'red')
GameObject('circle', Vector2.new(600, 0) , Vector2.new(2, 2), createMesh('objects/tekening.html'), 'blue')

groundMesh = GameObjects['ground']
hitMesh = GameObjects['circle'].meshes['mainMesh']

groundMesh.meshes['mainMesh'].add( hitMesh.points )



def circleUpdate(self, inputs) :
    if (inputs['keysDown'][87] == True) :
        self.velocity.y -= 10
    if (inputs['keysDown'][68] == True) :
        self.velocity.x += 10
    if (inputs['keysDown'][83] == True) :
        self.velocity.y += 10
    if (inputs['keysDown'][65] == True) :
        self.velocity.x -= 10

        

GameObjects['circle'].updates['movement'] = circleUpdate

print(collision.calculateRadius(groundMesh.meshes['mainMesh']))

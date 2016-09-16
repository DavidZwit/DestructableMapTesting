import Vector3
import Vector2


def loadHTMLVector(filePath, countOffset = 0) :
    
    finalPackage = {'points' : [],'vertCount' : 0}

    text = open(filePath, 'r').read()
    lines = text.split('\n')

    '''For counting how many lines have past'''
    lineCounter = countOffset

    #looping th elines
    for line in lines :
        #the start of a new shape
        if 'moveTo' in line :
            finalPackage['points'].append( stripHTMLNumbs(line) )
            lineCounter+=1  
             
        #the data in a new shape
        elif 'lineTo' in line :
            finalPackage['points'].append( stripHTMLNumbs(line) )
            lineCounter+=1       

        #the end of a shape
        elif 'fill' in line :
            pass
            

    finalPackage['vertCount'] = lineCounter
    return finalPackage

def stripHTMLNumbs (line) :
    seperatedTwo = line.split(',')

    return Vector2.new( float(seperatedTwo[0].split('(')[1]), float(seperatedTwo[1].split(')')[0]) )
        





def loadObj (filePath) :
    '''Load a 3d object's file'''
    #adding and empty vector so the array can start at 1
    finalPackage = {'points': [Vector3.new()], 'lines': []}

    text = open(filePath, 'r').read()
    lines = text.split('\n')

    for line in lines :
        if (len(line) > 0) :
            
            if line[0] == 'v' and line[1] == ' ' :
                finalPackage['points'].append(splitVertice(line))

            elif line[0] == 'f' and line[1] == ' ':
                finalPackage['lines'].append(splitFace(line))

    return finalPackage    

def splitVertice(line) :
    '''converting the vertices lines in to vector3's'''
    parts = line.split(' ')

    return Vector3.new( float(parts[1]), float(parts[2]), float(parts[3]) )

def splitFace(line) :
    '''Splittng the faces lines in to point arrays'''
    parts = line.split(' ')

    return Vector3.new(int(parts[1].split('/')[0]), int(parts[2].split('/')[0]), int(parts[3].split('/')[0]))
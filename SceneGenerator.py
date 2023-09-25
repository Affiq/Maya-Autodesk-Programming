import maya.cmds
import random

def makeCone(xposition, zposition, conenumber):
    # Dimensions for the cone
    coneheight = 1.5 
    coneradius = 0.4 
    
    # Dimensions for the cone base
    baseheight = 0.2
    baseyposition = (baseheight/2) # How much z should move so the base just touches the floor
    
    # Unique name generation for each object (if conenumber is unique)
    conename = "cone"+str(conenumber) 
    conebasename = "conebase"+str(conenumber) 
    coneyposition = ((coneheight/2) + baseheight) # How much z should move so cone just touches base
    
    # Generate cone base object and move to appropriate xyz position
    maya.cmds.polyCube(n=conebasename, height=baseheight)
    maya.cmds.move(xposition,baseyposition, zposition, conebasename, absolute=True)
    
    # Generate cone object and move to appropiate xyz position
    maya.cmds.polyCone(n=conename, height=coneheight, radius=coneradius) 
    maya.cmds.move(xposition,coneyposition, zposition, conename, absolute=True)


def makeOilDrum(xposition, zposition, drumnumber):
    # Dimensions for oil drum
    barrelradius = 1.4
    barrelheight = 3
    stripradius = barrelradius+0.05 # Has to be bigger than barrelradius to 'protrude' out
    stripheight = 0.2
    
    # Y position for the barrel and strips of the barrel
    cylindery = barrelheight/2
    strip1y = 0.4
    strip2y = barrelheight/2
    strip3y = barrelheight - 0.4
    
    # Unique name generation for each object
    cylindername = "cylinder"+str(drumnumber)
    strip1name = "cylinder"+str(drumnumber)+"strip1"
    strip2name = "cylinder"+str(drumnumber)+"strip2"
    strip3name = "cylinder"+str(drumnumber)+"strip3"

    # Main barrel frame
    maya.cmds.polyCylinder(n=cylindername, height=barrelheight, radius=barrelradius)
    maya.cmds.move(xposition,cylindery, zposition, cylindername, absolute=True)
    
    # Strips for barrel
    maya.cmds.polyCylinder(n=strip1name, height=stripheight, radius=stripradius)
    maya.cmds.move(xposition,strip1y, zposition, strip1name, absolute=True)
    maya.cmds.polyCylinder(n=strip2name, height=stripheight, radius=stripradius)
    maya.cmds.move(xposition,strip2y, zposition, strip2name, absolute=True)
    maya.cmds.polyCylinder(n=strip3name, height=stripheight, radius=stripradius)
    maya.cmds.move(xposition,strip3y, zposition, strip3name, absolute=True)
    
def makeRotatedCrates(xposition, zposition, cratesnumber):
    
    # Box dimensions - same length, height and width
    length = 1.9
    # Amount each box should rotate by
    box1turn = 11
    box2turn = 23
    box3turn = 67
   
    # Calculates y position of first 2 boxes
    y = length/2
    
    # Calculates y position of third box to allow boxes on top of boxes
    box3y = length + y
   
    # Calculates z positions of first 2 boxes so they don't intersect
    box1z = zposition + length/2
    box2z = zposition -length/2
   
    # Unique name generation for each box
    box1name = "crates"+str(cratesnumber)+"box1"
    box2name = "crates"+str(cratesnumber)+"box2"
    box3name = "crates"+str(cratesnumber)+"box3"
   
    # Box 1 has unique z position
    maya.cmds.polyCube(n=box1name, width=length,depth=length, height=length )
    maya.cmds.move( xposition, y, box1z, box1name)
    maya.cmds.rotate(0, box1turn, 0, box1name)

    # Box 2 has unique z position
    maya.cmds.polyCube(n=box2name, width=length,depth=length, height=length )
    maya.cmds.move( xposition, y, box2z, box2name)
    maya.cmds.rotate(0, box2turn, 0, box2name)
    
    # Box 3 has unique y position
    maya.cmds.polyCube(n=box3name, width=length,depth=length, height=length )
    maya.cmds.move( xposition, box3y, zposition, box3name)
    maya.cmds.rotate(0, box3turn, 0, box3name)
    

# recommended is 4 before it starts going off grid
scenedimensions = 4

# dimension width - the 'plot' of land each object takes - largest area an object takes up
# This would be the crate objects which is roughly 4
dimensionwidth = 5

# USER ENTER VARIABLES
emptyplotnum = 2
oildrumnum = 1
conenum = 1
cratesnum = 1

# Creates a list with those occurences until 
# there are enough objects in the list to populate the scene
objectlist = []
objectsneeded = dimensionwidth * dimensionwidth
while len(objectlist) < objectsneeded:
    for i in range(0,emptyplotnum):
        objectlist.append("empty")
    for i in range(0,oildrumnum):
        objectlist.append("oil")
    for i in range(0,conenum):
        objectlist.append("cone")
    for i in range(0,cratesnum):
        objectlist.append("crates")

random.shuffle(objectlist)
print(objectlist)


originx = -7.5
originz = -7.5

# Variables needed for the below algorithm
currentx = originx
currentz = originz
count = 0 # Used to count inside both nested loops so that you can get a unique object name

for xcounter in range(0, scenedimensions):
    
    for zcounter in range(0, scenedimensions):

        # Used to get the string from the list to determine which object to create
        currentobject = objectlist[count]
        
        # Block of code deciding which function to do
        if currentobject == "cone":
            makeCone(currentx, currentz, count)
        if currentobject == "oil":
            makeOilDrum(currentx, currentz, count)
        if currentobject == "crates":
            makeRotatedCrates(currentx, currentz, count)
        
        count = count + 1
        currentz = currentz + dimensionwidth # Z value increments every loop
    
    currentz = originz # The z position resets to the origin
    currentx = currentx + dimensionwidth # But x position increases so it goes to next row

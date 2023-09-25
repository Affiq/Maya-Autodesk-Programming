import maya.cmds as cmds

# User specifications
# The ball will bounce on max height at first bounce and travel xperbounce horizontally
# The ball will then halve in height per bounce
maxheight = 20
xperbounce = 2
totalbouncetime = 400
framenumber = totalbouncetime

# number of bounces should be based on frames - 40 frames per bounce
# May be a decimal so we convert it to an int
numberofbounces = int(framenumber / 40)

# Variables needed for functions below
currentx = 0
currenty = 2 * maxheight

# Working out the coordinates for the bouncing ball
coordinates = []
coordinates.append((0,0,0)) # origin from when the ball starts
for i in range(0, numberofbounces):
    # Calculating position when ball is in the air
    currentx = currentx + (xperbounce/2)
    currenty = currenty / 2
    coordinates.append((currentx, currenty, 0))
    
    # Calculating position when ball hits the floor
    currentx = currentx + (xperbounce/2)
    coordinates.append((currentx, 0, 0))    

# Creating path, sphere object and path animation for bouncing ball
myPath = cmds.curve(d = 1, p = coordinates)
mySphere = cmds.polySphere()
cmds.pathAnimation(mySphere[0], c = myPath, stu = 0, etu = totalbouncetime,f = True)

# Working out the coordinates for the curved rolling ball
# radius from origin
d2 = 10
node1 = (d2,0,d2)
node2 = (-d2,0,d2)
node3 = (-d2,0,-d2)
node4 = (d2,0,-d2)
rollordinates = [node1,node2,node3,node4]

# Creating path, sphere object and path animation for curved rolling ball
rollPath = cmds.curve(d = 3, p = rollordinates)
mySphere2 = cmds.polySphere()
cmds.pathAnimation(mySphere2[0], c = rollPath, stu = 0, etu = totalbouncetime/2, f= True)

# Calculating coordinates for the straight rolling ball
diagonalnodes = []
diagonalnodes.append(node4)
diagonalnodes.append(coordinates[len(coordinates)-1])

# Creating path, sphere object and path animation for straight rolling ball
diagonalpath = cmds.curve(d=1, p = diagonalnodes)
mySphere3 = cmds.polySphere()
cmds.pathAnimation(mySphere3[0], c = diagonalpath, stu = (totalbouncetime/2), etu = totalbouncetime, f=True)

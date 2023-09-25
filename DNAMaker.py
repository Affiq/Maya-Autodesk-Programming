import maya.cmds as mc
import math

def group_rotater(x_rotate):
    # Degrees to be rotated about the x axis
    
    # Get selected objects
    selectedObjects = mc.ls(orderedSelection=True)
    
    # We want to rotate about the x axis...
    mc.rotate(x_rotate,0,0, p=[0,0,0])


def makeStrand(copy_number, y_factor, x_inc, wavelength):
    # Code for object duplication with position y = y * sin x
    
    # User variables...
    # Copy number - Number of times to be duplicated
    # y_factor - Change value below to change height of sin wave
    # x_inc - How much x should increase by each time
    x_value_increment = x_inc
    # Wavelength - increase to increase size of wave
    
    
    # Get selected objects
    selectedObjects = mc.ls(orderedSelection=True)
    
    # Check if the user has selected only one object
    if len(selectedObjects) == 0:
        print("Select an object")
    elif len(selectedObjects) != 1:
        print("Please select one object only")
    else:
        print("Duplicating object")
        # Gets the first and only object in the list
        selectedObject = selectedObjects[0]
        print("Selected object: ",selectedObject)
        
        # Starting from origin...
        x_value = 0
        y_value = 0
        # Do the following copy_number times
        for count in range(copy_number):
            # Select original object, and duplicate
            mc.select(selectedObject)
            mc.duplicate() # Duplicate from origin
            # Calculate move values
            x_value = x_value + x_value_increment
            y_value = y_factor * math.sin(x_value/wavelength)
            # Move object
            mc.move(x_value, y_value, 0)
            
            
            
def makeBar(copynumber, y_factor, x_increment, divisor):
    # Bar maker - makes cubes with height dependent on sin x
    # User variables
    # X-Increment - Space between objects
    # copynumber - number of copies
    # y_factor- Bar peak value
    # Divisor - Wavelength equivalent of sin command - increase to reduce number of peaks
    
    # Starting from origin...
    x_value = 0
    
    # Origin bond bar so that the numbering at the end matches the spheres...
    mc.polyCube(name="bondbar")

    
    bar_height = 0
    # Do the following copy_number times
    for count in range(copy_number):
        
        # Work out x value and bar height first
        x_value = x_value + x_value_increment
        bar_height = 2* y_factor * math.sin(x_value/divisor)
        
        # If we have a negative value, we invert to positive
        if bar_height < 0:
            bar_height = bar_height * -1
        
        # Select original object, and duplicate it
        mc.polyCube(name="bondbar", height = bar_height)
    
        # Move object in x axis only
        mc.move(x_value, 0, 0)

# Uses the group rotater, make bar and make strand functions
def makeDNA(cop_num, y_fac, wavelen, x_inc):
    # Function creates polySphere cube and DNA strands 
    # - no objects need to be selected
    
    # Creating strand 1
    mc.polySphere(name="strand1Sphere")
    makeStrand(cop_num,y_fac,x_inc,wavelen)
    # List, select and rotate strand 1
    strand1list = mc.ls("strand1*")
    mc.select(strand1list)
    group_rotater(180)
    
    # Creating strand 2 with no rotation
    mc.polySphere(name="strand2Sphere")
    makeStrand(cop_num,y_fac,x_inc,wavelen)
    mc.ls("strand2*")
        
    # Making the bonds between the strands
    makeBar(cop_num,y_fac,x_inc,wavelen)
    
cop_num = 50
y_fac = 8
wavelen = 10
x_inc = 3

makeDNA(cop_num, y_fac, wavelen, x_inc)

    
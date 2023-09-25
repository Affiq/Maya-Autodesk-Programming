
import maya.cmds as mc
import random
import math

# import libraries for ui
from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

class TornadoGeneratorDialog(QtWidgets.QDialog):
    
    def __init__(self, parent = maya_main_window()):
        super(TornadoGeneratorDialog, self).__init__(parent)
        
        self.setWindowTitle("Tornado Generator")
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
        
        self.create_widgets()
        self.create_layouts()
        
    def create_widgets(self):
        # Labels, spinboxed and button widgets
        self.titlelabel = QtWidgets.QLabel("Tornado generator ")
        self.instructionlabel1 = QtWidgets.QLabel("Select objects to add to tornado, click generate ")
        self.instructionlabel2 = QtWidgets.QLabel("SEnsure shader 'tornadoshader' exists")
        
        self.tradiuslabel = QtWidgets.QLabel("Tornado radius: ")
        self.tradiusspinbox = QtWidgets.QSpinBox()
        self.tradiusspinbox.setValue(20) # Sets default value to 3
        self.tradiusspinbox.setRange(0,1000)
        
        self.theightlabel = QtWidgets.QLabel("Tornado height: ")
        self.theightspinbox = QtWidgets.QSpinBox()
        self.theightspinbox.setValue(60) # Sets default value to 2
        self.theightspinbox.setRange(0,1000)


        self.objectnumberlabel = QtWidgets.QLabel("Number of objects: ")
        self.objectnumberspinbox = QtWidgets.QSpinBox()
        self.objectnumberspinbox.setValue(50) # Sets default value to 2
        self.objectnumberspinbox.setRange(0,1000)


        self.sheightlabel = QtWidgets.QLabel("Start height: ")
        self.sheightspinbox = QtWidgets.QSpinBox()
        self.sheightspinbox.setValue(10) # Sets default value to 1
        self.sheightspinbox.setRange(0,1000)


        # Create button and link button to function
        self.generatebutton = QtWidgets.QPushButton("Generate")
        self.generatebutton.clicked.connect(self.generate_button_function)

    def create_layouts(self):
        # Adding all the widgets to the layout
        main_layout = QtWidgets.QVBoxLayout(self)
        
        main_layout.addWidget(self.titlelabel)
        main_layout.addWidget(self.instructionlabel1)
        main_layout.addWidget(self.instructionlabel2)
        
        main_layout.addWidget(self.tradiuslabel)
        main_layout.addWidget(self.tradiusspinbox)
        
        main_layout.addWidget(self.theightlabel)
        main_layout.addWidget(self.theightspinbox)
        main_layout.addWidget(self.objectnumberlabel)
        main_layout.addWidget(self.objectnumberspinbox)  
        main_layout.addWidget(self.sheightlabel)
        main_layout.addWidget(self.sheightspinbox)
        
        main_layout.addWidget(self.generatebutton)         
        
    def generate_button_function(self):
        print("Generate button pushed")
        # Get the value from the spinbox widgets in the UI
        # These will be used as paramters for our generate scene function
        tradius = self.tradiusspinbox.value()
        theight = self.theightspinbox.value()
        numofobjects = self.objectnumberspinbox.value()
        startheight = self.sheightspinbox.value()
        
        # Call the function that generates the scene, passing the paramters we have obtained
        create_tornado_scene(tradius,theight,numofobjects,startheight)

# Objects inside tornado generator...
def create_tornado_object(radius, height):
    # We can create a tornado as a reference point for where 
    # to put the actual tornado
    # Tornado dimensions - user defined
    torn_rad = radius
    torn_height = height
    # Make cone of custome size
    mc.polyCone(r=torn_rad, h=torn_height, name="tornado")
    # Make it upside down
    mc.rotate(180,0,0)
    # Move to appropriate height
    mc.move(0,torn_height/2,0)
    # Apply tornado shader
    mc.hyperShade(a="tornadoshader")
 
# For y = mx
def calculate_m(radius, height):
    msquared = math.pow(radius,2) + math.pow(height,2)
    m = math.pow(msquared , 0.5) # This is the hypotenuse
    m = m / radius # Use this to get m value (y per x)
    return m     
    
def add_objects_to_tornado(objectList, number_of_objects, start_height, end_height):
    
    print("Adding objects")
    
    # We need the m value so that we can place objects exactly on the edge
    # of the tornado and not inside
    m = calculate_m(tornado_radius,tornado_height) 
    print(m)
    
    for count in range(number_of_objects):
        print("Adding object ",count)
        
        # Here we select a random object from the list
        listLength = len(objectList)
        randomIndex = random.randrange(listLength)
        objectToAdd = objectList[randomIndex]
        mc.select(objectToAdd)
        
        # We duplicate it and move it to origin
        mc.duplicate()
        mc.move(0,0,0)
        
        # We choose a random height in the boundary to move it to, and calculate the x position
        # This line ensures that the cone moves to the surface of the tornado
        randy = random.randrange(start_height,end_height)
        xvalue = randy/m # from y=mx you get x=y/m
        mc.move(xvalue,randy,0)
        
        # We rotate around the y axis (from origin) so all cones are not in one line/slant
        # We make the pivot at the same y height
        # We get a random rotational value first
        randroty = random.randrange(360)
        mc.rotate(0,randroty,0, p=[0,randy,0])
        
             
        # We apply a random rotation to make it look like object is mid air
        randrotx = random.randrange(360)
        randroty = random.randrange(360)
        randrotz = random.randrange(360)
        mc.rotate(randrotx, randroty, randrotz, r=True)

def create_tornado_scene(tornado_radius, tornado_height,
                        number_of_objects, object_start_height): 
    
    # List of objects user has selected to add to tornado
    objectList = mc.ls(orderedSelection=True)
    
    if len(objectList)==0:
        print("Error: Please select 1 or more objects ")
    else:
        # Create the tornado cone object     
        create_tornado_object(tornado_radius, tornado_height)
        # Add objects to tornado
        add_objects_to_tornado(objectList, number_of_objects,
                         object_start_height, tornado_height)

d = TornadoGeneratorDialog()
d.show()
 



    
    

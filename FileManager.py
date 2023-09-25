from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance
import os
import shutil
import maya.OpenMayaUI as omui


# Making the main window
def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget) # Returns the mainwindowptr as a QtWidget?

class FileManagerDialog(QtWidgets.QDialog):
    
    def __init__(self, parent = maya_main_window()):
        super(FileManagerDialog, self).__init__(parent)
        
        self.setWindowTitle("File Manager")
        self.setMinimumWidth(500)
        self.setMinimumHeight(500)
        
        self.create_widgets()
        self.create_layouts()
       
        
    def create_widgets(self):    
        print("creating widgets")
        
        # Message box to tell user what is going on
        # Read only means user cannot change text in here
        self.message = QtWidgets.QLineEdit("Welcome to file manager", readOnly = True)
        
        # Source container and its widgets - lineedit and 2 buttons
        self.sourcegroupbox= QtWidgets.QGroupBox("Source")
        self.srclineedit = QtWidgets.QLineEdit()
        self.srcfilebutton = QtWidgets.QPushButton("Select source file")
        self.srcdirectorybutton = QtWidgets.QPushButton("Select source directory")
        
        # Target container and its widgets - lineedit and 1 button
        self.targetgroupbox= QtWidgets.QGroupBox("Target")
        self.targetlineedit = QtWidgets.QLineEdit()
        self.targetdirectorybutton = QtWidgets.QPushButton("Select target directory")
        
        # Options container and its widgets - 2 buttons
        self.optionsgroupbox= QtWidgets.QGroupBox("Options")
        self.copybutton = QtWidgets.QPushButton("Copy")
        self.movebutton = QtWidgets.QPushButton("Move")

        # Linking the button clicks to functions
        self.srcfilebutton.clicked.connect(self.srcfilebuttonfunction)
        self.targetdirectorybutton.clicked.connect(self.targetdirectorybuttonfunction)
        self.copybutton.clicked.connect(self.copybuttonfunction)
        self.movebutton.clicked.connect(self.movebuttonfunction)
        self.srcdirectorybutton.clicked.connect(self.srcdirectorybuttonfunction)

      
        
    def create_layouts(self):
        print("creating layouts")
        main_layout = QtWidgets.QVBoxLayout(self)
        
        # Message box added at the start
        main_layout.addWidget(self.message)
        
        # Source container layout
        source_layout = QtWidgets.QVBoxLayout(self.sourcegroupbox)
        main_layout.addWidget(self.sourcegroupbox)
        source_layout.addWidget(self.srclineedit)
        source_layout.addWidget(self.srcfilebutton)
        source_layout.addWidget(self.srcdirectorybutton) # order is messed
        
        
        # Target container layout
        target_layout = QtWidgets.QVBoxLayout(self.targetgroupbox)
        main_layout.addWidget(self.targetgroupbox)
        target_layout.addWidget(self.targetlineedit)
        target_layout.addWidget(self.targetdirectorybutton)
        
        # Options layout
        options_layout = QtWidgets.QVBoxLayout(self.optionsgroupbox)
        main_layout.addWidget(self.optionsgroupbox)
        options_layout.addWidget(self.copybutton)
        options_layout.addWidget(self.movebutton)

    def get_file(self):
        unicodePath = maya.cmds.fileDialog2(
            caption="Choose folder or file",
            dialogStyle=1,
            fileMode=1) # File mode is any existing file
        return unicodePath[0]  
            
    def get_directory(self):
        unicodePath = maya.cmds.fileDialog2(
            caption="Choose folder or file",
            dialogStyle=1,
            fileMode=3) # File mode 2 is folder selection only
        return unicodePath[0]   
 
    # Function used to determine if src is file or directory
    # Returns string
    def get_src_type(self):
        # We create a variable to know if it file or folder named srctype
        srcpath = self.srclineedit.text()
        srctype = ""
        if os.path.isdir(srcpath):
            self.message.setText("Source directory detected")
            srctype = "directory"
            print("Directory detected")
        elif os.path.isfile(srcpath):
            self.message.setText("Source file detected")
            srctype = "file"
            print("File detected")
        else:
            self.message.setText("No source detected")
            srctype = "none"
            print("No source detected")
        return srctype
    
    # This function needs to be designed to handle file copying 
    # and folder (directory) copying    
    def copyfile(self):
            
        srctype = self.get_src_type()
        srcpath = self.srclineedit.text()
        targetpath= self.targetlineedit.text()
        
        # Used to get the name of the source file used to save
        # Split into string list by /, so Documents/project1/myfile.txt 
        # turns into the list ["Documents", "project1","myfile.txt"]
        # We then get the last item to get the file name
        pathlist = srcpath.split('/')
        filename = pathlist[len(pathlist) - 1]  # Subtract 1 cos index starts at 0
        targetpath = targetpath + '/' + filename
        
        if srctype == "directory":
            shutil.copytree(srcpath, targetpath)
            self.message.setText("Source directory copied successfully")
        elif srctype == "file":
            shutil.copy(srcpath, targetpath)            
            self.message.setText("Source file copied successfully")

    
    # No need to complex code as shutil.move allows moving both files and folders
    # So no need to find source file type
    def movefile(self):
        srcpath = self.srclineedit.text()
        targetpath= self.targetlineedit.text()
        
        # Get the name of file and add it to end of targetpath
        pathlist = srcpath.split('/')
        filename = pathlist[len(pathlist) - 1] 
        targetpath = targetpath + '/' + filename
        
        shutil.move(srcpath, targetpath)
        self.message.setText("Source file moved successfully")
    
        
    def srcfilebuttonfunction(self):
        self.message.setText("Select Source file button clicked.")
        selectedDirectory = self.get_file()
        self.srclineedit.setText(selectedDirectory)
        self.message.setText("New source file selected!")
        
    def targetdirectorybuttonfunction(self):
        self.message.setText("Select Target button clicked.")
        selectedDirectory2 = self.get_directory()
        self.targetlineedit.setText(selectedDirectory2)
        self.message.setText("New target directory selected!")
        
    def copybuttonfunction(self):
        self.message.setText("Copy button clicked.")
        self.copyfile()
        
    def movebuttonfunction(self):
        self.message.setText("Move button clicked")
        self.movefile()
        
    def srcdirectorybuttonfunction(self):
        self.message.setText("Select Source Directory button clicked.")
        selectedDirectory3 = self.get_directory()
        self.srclineedit.setText(selectedDirectory3)
        self.message.setText("New source directory selected!")
    
    
    
        
d = FileManagerDialog()
d.show()

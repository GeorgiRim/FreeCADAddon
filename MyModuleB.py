import FreeCADGui as Gui
import FreeCAD as App
import Image, ImageGui
import Part, PartGui
class My_Command_ClassB():
    """My new command"""

    def GetResources(self):
        return {"Pixmap"  : "My_Command_Icon", # the name of a svg file available in the resources
                "Accel"   : "Shift+S", # a default shortcut (optional)
                "MenuText": "My New Command",
                "ToolTip" : "What my new command does"}

    def Activated(self):
        """Do something here"""
        doc = App.activeDocument()
        App.Console.PrintMessage('Hello, World!')
        img_plane = doc.addObject('Image::ImagePlane', 'ImagePlane')
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True

Gui.addCommand("My_CommandA", My_Command_ClassB())

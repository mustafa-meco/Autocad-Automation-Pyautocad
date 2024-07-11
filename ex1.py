import win32com.client

# Connect to the running instance of AutoCAD
acad = win32com.client.Dispatch("AutoCAD.Application")
doc = acad.ActiveDocument

# Define the color you want (e.g., red)
color_red = 1

# Iterate through all objects in the current drawing
for obj in doc.ModelSpace:
    print(obj.ObjectName)
    obj.color = color_red

# Redraw the screen to see the changes
acad.Update()

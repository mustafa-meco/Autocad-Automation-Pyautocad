import win32com.client
import tkinter as tk

def get_object_names():
    acad = win32com.client.Dispatch("AutoCAD.Application")
    doc = acad.ActiveDocument
    
    object_names = set()  # Use a set to avoid duplicates
    
    for obj in doc.ModelSpace:
        object_names.add(obj.ObjectName)
    
    return list(object_names)

def get_layer_names():
    acad = win32com.client.Dispatch("AutoCAD.Application")
    doc = acad.ActiveDocument
    
    layer_names = set()  # Use a set to avoid duplicates
    
    for layer in doc.Layers:
        layer_names.add(layer.Name)
    
    return list(layer_names)

def change_color():
    selected_object = object_var.get()
    new_color = color_var.get()
    
    acad = win32com.client.Dispatch("AutoCAD.Application")
    doc = acad.ActiveDocument
    
    for obj in doc.ModelSpace:
        if obj.ObjectName == selected_object:
            obj.color = new_color

    acad.Update()

    status_label.config(text="Status: Color changed to " + str(new_color))

# make function to change layers color instead of objects
def change_layer_color():
    selected_layer = layer_var.get()
    new_color = color_var.get()
    
    acad = win32com.client.Dispatch("AutoCAD.Application")
    doc = acad.ActiveDocument
    
    for layer in doc.Layers:
        if layer.Name == selected_layer:
            layer.color = new_color

    acad.Update()

    status_label.config(text="Status: Color changed to " + str(new_color))


root = tk.Tk()
root.title("AutoCAD Object Color Changer")

# Get the object names from the AutoCAD document
object_names = get_object_names()

# Create a label for object selection
object_label = tk.Label(root, text="Select an object:")
object_label.pack()

# Create a dropdown menu for selecting an object
object_var = tk.StringVar()
object_dropdown = tk.OptionMenu(root, object_var, *object_names)
object_dropdown.pack()



# Create a label for color selection
color_label = tk.Label(root, text="Select a color (1=Red, 2=Yellow, etc.):")
color_label.pack()

# Create an entry field for color selection
color_var = tk.IntVar()
color_entry = tk.Entry(root, textvariable=color_var)
color_entry.pack()
color_entry.bind("<Return>", lambda event: change_color())

# Create a button to change the color
change_button = tk.Button(root, text="Change Object Color", command=change_color)
change_button.pack()


# Get the layer names from the AutoCAD document
layer_names = get_layer_names()

# Create a label for layer selection
layer_label = tk.Label(root, text="Select a Layer:")
layer_label.pack()

# Create a dropdown menu for selecting an layer
layer_var = tk.StringVar()
layer_dropdown = tk.OptionMenu(root, layer_var, *layer_names)
layer_dropdown.pack()
# Create a button to change the color
change_button = tk.Button(root, text="Change Layer Color", command=change_layer_color)
change_button.pack()


# Make a separation line before the status label
tk.Label(root, text="").pack()

status_label = tk.Label(root, text="Status: Ready")
status_label.pack()

root.mainloop()

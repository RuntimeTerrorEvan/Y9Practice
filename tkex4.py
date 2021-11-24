# Tkinter introductory example 
# Showing the use of the "grid" layout manager
# Enabling buttons to work 
# Introducing the "Label"

import tkinter as tk
root = tk.Tk() # root is the name of the GUI object
root.title("My TKinter Program") 
root.minsize(300, 300) # height and width in pixels
root.geometry ("600x500")

# Set up your variables
myBGColour = "yellow"

# Define all of your functions to be used later in the program
# Note: On Mac OSX there are strict guidelines for the appearance of buttons 
# and they cannot be changed using the "config" command.

def b1command():
	print ("executing b1 command")
	label1.config (bg = "red", text="This is Red!")

def b2command():
	print ("executing b2 command")
	label1.config (bg = "orange", text="This is Orange!")

def b3command():
	print ("executing b3 command")
	label1.config (bg = "yellow", text="This is Yellow!")

def b4command():
	print ("executing b4 command")
	label1.config (bg = "blue", text="This is Blue!")

def b5command():
	print ("executing b5 command")
	label1.config (bg = "green", text="This is Green!")

def b6command():
	print ("executing b6 command")
	label1.config (bg = "violet", text="This is Violet!")
	


# Create your buttons
# Note the height and the width are set in "units of text"
b1 = tk.Button(root, text = "Red", height = 10, width = 20, command = b1command) 
b2 = tk.Button(root, text = "Orange", height = 10, width = 20, command = b2command) 
b3 = tk.Button(root, text = "Yellow", height = 10, width = 20, command = b3command) 
b4 = tk.Button(root, text = "Blue", height = 10, width = 20, command = b4command) 
b5 = tk.Button(root, text = "Green", height = 10, width = 20, command = b5command) 
b6 = tk.Button(root, text = "Violet", height = 10, width = 20, command = b6command) 

# Create your label
label1 = tk.Label(root, bg=myBGColour, pady=5, height=30, width=30)

# Position everything using the Grid Layout Manager

# Along Row 0
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

# Along Row 1
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

# Label is placed in Column 3, Row 0 and will span 2 rows downward
label1.grid(row=0, column=3, rowspan=2)

root.mainloop()
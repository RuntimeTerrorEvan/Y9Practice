import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Math Tutor")
root.minsize(950, 950)
root.geometry("950x950")

def getGeometry():
	Title.config(text = "Geometry", font =("Courier", 44))
	R1 = tk.Radiobutton(root, text="1", padx = 20, variable=rb,value=1, 
		command = getRadio_Button).grid(row=1, column = 0)
	R2 = tk.Radiobutton(root, text="2", padx = 20, variable=rb, value=2,
	    command = getRadio_Button).grid(row=2, column = 1)

	R3 = tk.Radiobutton(root, text="3", padx = 20).grid(row=3, column = 0)

def getRadio_Button():
	state = rb.get()

	if (state == 1):
		R2.config(text = "aaa")
	
	if (state == 2):
		R1.config(text = "lkjlkjlkj")


	#	if (state == 2):
#		tk.Radiobutton(root, text="4", padx = 20, variable=geod,value=7).grid(row=4, column = 0)
#		tk.Radiobutton(root, text="5", padx = 20, variable=geod, value=8).grid(row=5, column = 0)	
#		tk.Radiobutton(root, text="6", padx = 20, variable=geod,value=9).grid(row=6, column = 0)
#		tk.Radiobutton(root, text="7", padx = 20, variable=geod, value=10).grid(row=7, column = 0)

#	if (state == 1):
#		tk.Radiobutton(root, text="0", padx = 20, variable=geos,value=3).grid(row=3, column = 0) 
		#tk.Radiobutton(root, text="1", padx = 20, variable=geos, value=4 ).grid(row=4, column = 0)				
		#tk.Radiobutton(root, text="2", padx = 20, variable=geos,value=5).grid(row=5, column = 0)
		#tk.Radiobutton(root, text="3", padx = 20, variable=geos, value=6).grid(row=6, colum= 0)
		#tk.Radiobutton(root, text="100", padx = 20, variable=geos, value=66).grid(row=7, colum= 0)
		#tk.Radiobutton(root, text="21", padx = 20, variable=geos, value=77).grid(row=8, colum= 0)

#It is critical that each set of 4 radio buttons share the same variable, as it allows the 
#program to easily identify which one is clicked based on its value (some where from 3 through 10).

def getInequality():
	Title.config(text = "Inequalities")

def clicker():
	contacts = tk.Toplevel(root) # Creates a seperate window from the main GUI.
	contacts.title("Help") 
	contacts.geometry("250x150")
	contacts.config(bg = "green")

# variables to store which radio button is clicked.

geos = tk.IntVar()
geod = tk.IntVar()
rb = tk.IntVar()


# An array to store the actual problems.
#Using an array or list here allows you to add or remove problems as you please, 
 #and the function will incorporate them into the test.

Simple_Absolute_Prompts = [ 
	"What is 1 + 1", 
	"What is 2 + 2",
	"What is 3 + 3",
	"What is 4 + 4"
]


#class simple_absolute:
#	def __init__(self, correct_letter, question, "7",  "8", "9", "10"): #Defining all of the properties of the class.
#		self.correct_letter = correct_letter
#		self.question = question 
#		self.7 = 7
#		self.8 = 8
#		self.9 = 9
#		self.10 = 10

# A class allows me to easily define a host of variable specific to each problem. 

#Simple_Absolute_Questions = [
#	Question(question_prompts[0], correct = 7, 7 = "1", 8 = "2", 9 ="3", 10 = "4"),
#	Question(question_prompts[1], "8" ),
#	Quesiton(question_prompts[2], "9"), 
#	Question(question_prompts[3], "10" )
#]

def run_test(questions):
	score = 0 
	for question in Simple_Absolute_Questions:
		answer = input(Simple_Absolute_Prompts) #need to convert to radio buttons
		if answer == question.correct_letter:
			score += 5 
		print ("You earned", score, "points. Congratulations!")


tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text = 'Tab 1')

Geometry_Button = tk.Button(root, height = 5, width = 25, command = getGeometry, padx = 20, pady = 20, text = "Geometry")
Submit_Button = tk.Button(root, height =5, width = 10, text = "Submit")
Inequality_Button = tk.Button(root, height = 5, width = 10, text = "Inequalities", command = getInequality)

Title = tk.Label(root, font = 'helvetica')

ttk.Label(tab1, text = "this is tab 1 ")

#Contact_Button = tk.Button(root, text = "Need Help?", command = clicker, fg = "dark blue")

Geometry_Button.grid(row = 0, column = 0)
Inequality_Button.grid(row = 0, column = 1)
#Contact_Button.grid(row = 2, column = 0)
Title.grid(row=0, column=2)			# The grid layout manager was helpful for organizing buttons on either end of the GUI


root.mainloop()
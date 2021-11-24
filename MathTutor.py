# For Mr. Jugoon
# "Math Tutor" by Evan Rosenberg 

#-----------Opening statements----------->



import tkinter as tk
import random 
from sys import exit
from tkinter.ttk import *


# | Root refers to the GUI as a whole: | 
 
root = tk.Tk()
root.title("Math Tutor")
root.minsize(950, 950)
root.geometry("950x950")  

#-----------Define Commands----------->

def simplecommand():
	print("Executing simplecommand...")
	simple_problems = ["What is 1+1?", "What is 2+2?", "What is 3+3?"]
	Display_Solution.config(text=Simple_Choose)
	print(random.choice(simple_problems))  
	simple_problems.remove(Simple_Choose)  

def difficultcommand():
	print("Executing difficultcommand...")
	Difficult_Problems = ["What is the meaning of life?", "Who are you?", "How does LIGO work?"] 
	Display_Solution.config(text = Difficult_Choose)
	print(random.choice(Difficult_Problems))
	Difficult_Problems.remove(Difficult_Choose) # Removes problem from problem set once viewed 

def clicker():
	contacts = tk.Toplevel(root) # Creates seperate window from main GUI
	contacts.title("Help") 
	contacts.geometry("250x150")
	contacts.config(bg = "green")	
#teacher1 = tk.label(text = "Natasha Mosdossy - Teacher of Mathematics, Upper Canada College: natasha.mosdossy@ucc.on.ca")
#	teacher2 = tk.label(text = "Pavel Volnyakov - PhD in Mathematics, IBM: pavel.volnyakov@gmail.com")
#	student1 = tk.label(text = "Evan Rosenberg - Year 9 Student, Upper Canada College, Developer: evan.rosenberg@ucc.on.ca")
#	student2 = tk.label(text = "Dillon Aristotle = Year 12 Student, Upper Canada College: dillon.aristotle@ucc.on.ca")
#	teacher1.grid(row=0, column = 0)
#teacher2.grid(row=0, column = 1)
#student1.grid(row=1, column = 0)
#student2.grid(row=1, column = 1) # The layout of the seperate widget must also be contained within this function

def getGeometry():
	Title.config(text = "Geometry", font =("Courier", 44))
	Geometry_Simple_Questions = tk.Button(root, height=80, width=415, command = simplecommand, image = photo)
	Geometry_Difficult_Questions = tk.Button(root, height=5, width=25, text="Difficult Problems", command= difficultcommand)
	Geometry_Simple_Questions.grid(row=3, column=0, padx=10, pady = 5 )
	Geometry_Difficult_Questions.grid(row=3, column=1, padx = 10, pady = 5)

def getInequality():
	Title.config(text = "Inequalities")

#def milestone():
#	milestoneRoot = Tk()
#	milestoneRoot.after(2000, exit)
#	milestoneRoot.geometry("400x700") 
#	milestoneRoot.mainloop()
# needs to happen when achieve certain number of points 
            
#-----------Variables----------->

#Simple_Topics = ["Absolute Value 101", "Inequalities 101"]
#Difficult_Topics = ["Hard Absolute Value", "Hard Inequalities"]

#simple problems and solutions 

#Absolute_Value_101_Problems = ["", "", ""]
#Inequalities_101_Problems = ["", "", ""]

#Absolute_Value_101_Solutions = ["", "", ""]
#Inequalities_101_Solutions = ["", "", ""]

#hard problems and solution

#Hard_Absolute_Value_Problems = ["", "", ""]
#Hard_Inequalities_Problems = ["", "", ""]

#Hard_Absolute_Value_Solutions = ["", "", ""]
#Hard_Inequalities_Solutions = ["", "", ""]


Difficult_Problems = ["What is the meaning of life?", "Who are you?", "How does work?"]
Difficult_Choose = random.choice(Difficult_Problems)

simple_problems = ["What is 1+1?", "What is 2+2?", "What is 3+3?"]
Simple_Choose = random.choice(simple_problems)

photo = tk.PhotoImage(file = "/Users/evan.rosenberg/Desktop/simpleproblems.png") 

Solution_Entry = tk.StringVar()

# | Labels/Text: | 

Display_Solution = tk.Label(root, font = 'helvetica')

Cover_Up_Simple = tk.Label(root, bg = "white", height = 30, width = 50)
Cover_Up_Difficult = tk.Label(root, bg = "white", height = 10, width = 20)

# | Interactive user features (buttons, entry boxes & message boxes): | 

GeometryProblems = tk.Button(root, height = 5, width = 25, command = getGeometry, padx = 10, pady = 10, text = "Geometry")
InequalityProblems = tk.Button(root, height = 5, width = 25, command = getInequality, text = "Inequalities", padx = 10, pady = 10)

Title = tk.Label(root, font = 'helvetica')


Number_Entry = tk.Entry(root, textvariable = Solution_Entry)
Contact_Button = tk.Button(root, text = "Need Help?", command = clicker, fg = "dark blue")


#if Solution_Entry == correct answer:
#	.config "you are correct"
#	button = next question 
#
#remove problem from the list 

#-----------Layout(Grid)----------->

GeometryProblems.grid(row = 1, column = 0)
InequalityProblems.grid(row = 2, column = 0)

Number_Entry.grid(row =2, column=1)
Contact_Button.grid(row = 5, column = 0)

Title.grid(row=0, column=4)

Display_Solution.grid(row = 0, column = 7)

# | Completes main loop |

root.mainloop()

	


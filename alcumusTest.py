# For Mr. Jugoon
# "Math Tutor" by Evan Rosenberg 

#-----------Opening statements----------->

import tkinter as tk
import tkinter.font as font
#import random

# | Root refers to the GUI as a whole: | 

root = tk.Tk()
root.title("Math Tutor")
root.minsize(950, 950)
root.geometry("950x950") 

#-----------Define Commands----------->

# | Entry box to gather responses from the user |

def getInfo():
    num1 = (number1.get())
    label2.config(text="The number entered was " + str(num1))

# | Commands which run both difficulty levels: |

def simplecommand():
	print("Executing simplecommand...")
	simple_problems = ["What is 1+1?", "What is 2+2?", "What is 3+3?"]
	label3.config(text=Simple_Choice)
	print(random.choice(simple_problems))    

def difficultcommand():
	print("Executing difficultcommand...")
	difficult_problems = ["What is the meaning of life?", "Who are you?", "How does LIGO work?"] 
	print(random.choice(difficult_problems))
            
#-----------Variables----------->

difficult_problems = ["What is the meaning of life?", "Who are you?", "How does LIGO work?"]

Difficult_Choice = random.choice(difficult_problems)

simple_problems = ["What is 1+1?", "What is 2+2?", "What is 3+3?"]

Simple_Choice = random.choice(simple_problems)

# | Data Variables: | 

Number_Response = tk.StringVar()

# | Labels/Text: | 

label1 = tk.Label(root, text="Enter your number: ")
label2 = tk.Label(root, 
    bg = "blue", 
    fg = "light green",
    font = "Helvetica 16 bold italic",
    text="Your number is: ")
label3 = tk.Label(root, text = Difficult_Choice)

# | Interactive user features (buttons & entry boxes): | 

Get_Number = tk.Button(root, text="Get Number", command=getInfo)

Get_Simple_Questions = tk.Button(root, bg = '#70ff9a', height=5, width=25, text = "Simple Problems", command = simplecommand)
Get_Difficult_Questions = tk.Button(root, bg= '#70ff9a', height=5, width=25, text="Difficult Problems", command= difficultcommand)

Number_Entry = tk.Entry(root, textvariable=Number_Response)

#-----------Layout(Grid)----------->

Get_Simple_Questions.grid(row=0, column=0)
Get_Difficult_Questions.grid(row=0, column=1)

label1.grid(row=1, column=0)
label2.grid(row=3, column=0)
label3.grid(row=5, column=0)

Number_Entry.grid(row=4, column=0)
Get_Number.grid(row=2, column=0)



# | Completes main loop |

root.mainloop()


#if response_n == solution_n:

	#score = total + 10

#else:
	#score = total 

#display total in progress bar 


#Want to attach video links with each solution  
# variable which adds 10 points for each correct answer
# Side button, which when opened displays "tips"
# After each answer, displays solutions SPECFIC to that question? and button to go to next problem
# Progress bar 
# Button which when opened, displays contacts 



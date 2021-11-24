import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Mentor")
root.minsize(1000, 600)
root.geometry("600x350")

icon = tk.PhotoImage(file = 'socrates.png') #Creates the icon image
root.iconphoto(False, icon) #Sets the icon 

#handles the pressing of the button: "Help"
def helper():
    help = tk.Toplevel(root)
    help.title("Help")
    help.geometry("700x150")
    tk.Label(help, text = "Natasha Mosdossy - Teacher of Mathematics, Upper Canada College: natasha.mosdossy@ucc.on.ca \n Emilia Martin - Teacher of Mathematics, Upper Canada College: emilia.martin@ucc.on.ca \n Alvin Jugoon - Teacher of Mathematics, Upper Canada College: ajugoon@ucc.on.ca", font = ('Helvetia', 15)).grid(row = 0, column =0)
    tk.Label(help, text = "Evan Rosenberg - Year 9 Student, Upper Canada College, Developer: evan.rosenberg@ucc.on.ca \n Dillon Aristotle -  Year 12 Student, Upper Canada College: dillon.aristotle@ucc.on.ca \n Karam Bambawale - Year 12 Student, Upper Canada College: karam.bambawale@ucc.on.ca", font = ('Helvetia', 15)).grid(row = 1, column = 0)
    tk.Label(help, text = "Note: Please include a screenshot of your problem if you are looking for help. ", font = ('Helvetia', 15, 'bold')).grid(row =2, column = 0 )

#handles the pressing of the menu selection: "Geometry"
def onGeometry():
    global Topic                    #Defined globally.
    global GI                       #GI stands for the topic: "Geometry Intermediate".
    global GC                       #GC stands for the topic: "Geometry Challenging".
    subject.set(1)                  #Default menu selection (Geometry).
    Ls.config(text = "Geometry")    #Sets the default text of the topic .
    if(difficulty.get() == 1):      #Setting the topic according to the difficulty selection (Intermediate or Challenging).
        Topic = GI
    else:
        Topic = GC
    populateFields()

def onInequal():
    global Topic
    global II                       #Stands for the topic: "Inequalities Intermediate".
    global IC                       #Stands for the topic: "Inequalities Challenging".
    subject.set(2)
    Ls.config(text = "Inequalities")
    if(difficulty.get() == 1):
        Topic = II
    else:
        Topic = IC
    populateFields()
     
def onDifficulty():
    global Topic
    global GI
    global GC
    global II
    global IC
    if(subject.get() == 1):
        if(difficulty.get() == 1):
            Topic = GI
        else:
            Topic = GC
    else:
        if(difficulty.get() == 1):
            Topic = II
        else:
            Topic = IC

    populateFields()
       
def onSubmit():
    global Topic
    ans = answer.get() - 1          #answer goes from 1-5. ans is the position in the list of answers for each question from 0-4. 
    q = Topic.getCurrentQuestion()
    if(not q.answered):             #Once submitted, the question becomes marked as answered. 
        q.answered = True
        if(ans == q.correct_ans):   #Adds onto total score if correct. 
            Topic.current_score += q.score

    populateFields()
    
def onNext():
    global Topic
    q = Topic.getCurrentQuestion()
    if(q.answered):
        num = len(Topic.questions)   #Finds the total number of questions in a topic
        pos = Topic.question_pos
        if(pos < num - 1):           #Pos stands for positiion of the question (from 0-2). Since there are 3 total, you must subtract 1 to find the last number in the list. 
            Topic.question_pos += 1
        populateFields()


subject = tk.IntVar()
subject.set(1)   
menubar = tk.Menu(root)             # Creates upper menu 

sub = tk.Menu(menubar, tearoff = 0)
dif = tk.Menu(menubar, tearoff = 0)

menubar.add_cascade(label = "Mentor Subject", menu = sub)
sub.add_command(label = "Geometry", command = onGeometry)
sub.add_command(label = "Inequalities", command = onInequal)

root.config(menu = menubar)


#Create all the main frames

fr_top = tk.Frame(root, width = 450, height = 30, pady = 10, bg = "#1e355d")
fr_cl = tk.Frame(root,  width = 100, height = 150, pady = 10, padx = 10)
fr_cr = tk.Frame(root,  width = 350, height = 150, padx = 20)
fr_b1 = tk.Frame(root,  width = 450, height = 20, padx = 20, pady = 10)
fr_b2 = tk.Frame(root,  width = 450, height = 100, padx = 20, pady = 20)



root.grid_rowconfigure(1, weight = 1)
root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 6)

fr_top.grid(row = 0, columnspan = 2, sticky = 'ew', pady = 3)
fr_cl.grid(row = 1, column = 0, sticky = 'nsew')
fr_cr.grid(row = 1, column = 1, sticky = 'nsew')
fr_b1.grid(row = 2, columnspan = 2, sticky = 'ew')
fr_b2.grid(row = 3, columnspan = 2, sticky = 'ew')

#Places topic radio buttons, and subject label on the Top frame

Ls = tk.Label(fr_top, text = "Geometry", pady = 10,padx = 20, bg = "#1e355d", fg = "#11d48f", font = ('Helvetia', 23, 'bold'))
Ls.grid(row = 0, column = 0, padx = 6, sticky = 'nsw')

difficulty = tk.IntVar()
difficulty.set(1)
Rs = tk.Radiobutton(fr_top, text = "Intermediate", padx = 20, pady = 3, variable = difficulty, value = 1, command = onDifficulty, bg = "#1e355d", fg = "#45c0f5", font = ('Helvetia', 18, 'bold'))
Rd = tk.Radiobutton(fr_top, text = "Challenging",padx =20, variable = difficulty, value = 2, command = onDifficulty, bg = "#1e355d", fg= "#45c0f5", font = ('Helvetia', 18, 'bold'))
Rs.grid(row = 0, column = 1, sticky = 'nse')
Rd.grid(row = 0, column = 2, sticky = 'nse')

#Places radio buttons on the center left frame

fr_cl.rowconfigure(0, weight = 1)
fr_cl.rowconfigure(1, weight = 1)
fr_cl.rowconfigure(2, weight = 1)
fr_cl.rowconfigure(3, weight = 1)
fr_cl.rowconfigure(4, weight = 1)

answer = tk.IntVar()
answer.set(1)

Ra1 = tk.Radiobutton(fr_cl, variable = answer, value = 1, text = "", font = ('Helvetia', 16))
Ra1.grid(padx = 10, row = 0, column = 0, sticky = 'nsw')

Ra2 = tk.Radiobutton(fr_cl, variable = answer, value = 2, text = "", font = ('Helvetia', 16,))
Ra2.grid(padx = 10, row = 1, column = 0, sticky = 'nsw')
Ra3 = tk.Radiobutton(fr_cl, variable = answer, value = 3, text = "", font = ('Helvetia', 16))
Ra3.grid(padx = 10, row = 2, column = 0, sticky = 'nsw')

Ra4 = tk.Radiobutton(fr_cl, variable = answer, value = 4, text = "3", font = ('Helvetia', 16))
Ra4.grid(padx = 10, row = 3, column = 0, sticky = 'nsw')

Ra5 = tk.Radiobutton(fr_cl, variable = answer, value = 5, text = "", font = ('Helvetia', 16))
Ra5.grid(padx = 10, row = 4, column = 0, sticky = 'nsw')


#Places problem/solution text  on the Center right frame

fr_lf = tk.LabelFrame(fr_cr, width = 300, relief = "groove", bd= "5")
fr_lf.pack(expand = 1, fill = 'both')

Lq = tk.Label(fr_lf, padx = 20, pady = 5, anchor = "center", wraplength = 700, text = "blah blah blah", font = ('Helvetia', 18, 'bold'))
Lq.pack(expand = 1, fill = 'both')

#Places label and progress bar on the Bottom frame 1
tk.Label(fr_b1, padx = 6, pady = 6, text = "Progress:", anchor = "center").pack(side = 'left')

Plb = tk.Label(fr_b1, padx = 6, pady = 6, text= "0 (0)", anchor = "w")
Plb.pack(side = 'left')

Pb = ttk.Progressbar(fr_b1, orient = 'horizontal', value = 40, maximum = 100, mode = 'determinate')
Pb.pack(expand = 1, fill = 'x', side = 'left')

#Places next, submit and help buttons on frame 2

fr_b2.columnconfigure(1, weight = 1)
fr_b2.columnconfigure(3, weight = 1)

Bsub = tk.Button(fr_b2, pady = 10, padx = 20, text = "Submit", width = 15, command = onSubmit, font = ('Helvetica', 17, 'bold'))
Bsub.grid(row = 0, column = 0, sticky = "ws")

Bnext = tk.Button(fr_b2, pady = 10, text = "Next", width = 15, command = onNext, state = "disabled", font = ('Helvetica', 17, 'bold'))
Bnext.grid(row = 0, column = 2)

Bhelp = tk.Button(fr_b2, pady = 10,  padx = 20, text = "Help", width = 15, font = ('Helvetica', 17, 'bold'), command = helper)
Bhelp.grid(row = 0, column = 4, sticky = "es")



################################
# Questions and answers
################################

class Question:
    def __init__(self):             #class constructor - sets the initial object values
        self.text = "Unknown"
        self.solution = "Unknown"
        self.answers = ["Unknown", "Unknown", "Unknown", "Unknown", "Unknown"]
        self.score = 1
        self.correct_ans = 0
        self.answered = False

class Subject:
    def __init__(self, name):       
        self.name = name
        self.questions = []
        self.max_score = 0
        self.current_score = 0
        self.question_pos = 0
        
    def prepare(self):          #scrolls through the questions and adds up their scores to the total score
        for x in self.questions:
            self.max_score += x.score       #+= adds score the max_score 

    def getCurrentQuestion(self):       
        return self.questions[self.question_pos]            #Returns the current question of the topic 

#Updates the problem descriptions, answers and the score. 
def populateFields():    
    q = Topic.getCurrentQuestion()
    Ra1.config(text = q.answers[0]) 
    Ra2.config(text = q.answers[1])
    Ra3.config(text = q.answers[2])
    Ra4.config(text = q.answers[3])
    Ra5.config(text = q.answers[4])
    if (q.answered ):
        Lq.config(text = q.solution)
    else:
        Lq.config(text = q.text)

    score_format = "questions: {}, score: {}({}) " #Place holders to stick topic score and maximum score 
    score_text = score_format.format(len(Topic.questions), Topic.current_score, Topic.max_score)
    Plb.config(text = score_text) #Plb stands for progress label bar 
    Pb.config(value = Topic.current_score, maximum = Topic.max_score) #Pb stands for progress bar 
    if (q.answered):
        Bsub.config(state = "disabled")
    else:
        Bsub.config(state = "active")

    if (not q.answered):
        Bnext.config(state = "disabled")
    else:
        pos = Topic.question_pos
        num = len(Topic.questions) 
        if (pos < num - 1):
            Bnext.config(state = "active")
        else:
            Bnext.config(state = "disabled")





#########################################
# Making Geometry Intermediate questions
#########################################

geom_inter_1 = Question()
geom_inter_1.text = "Problem 1: What is the y-intercept of y = |x-h| + k?"
geom_inter_1.solution = "Plugging in 0 for x yields y = |0-h| + k. \n We can find the negative and positive cases by removing the absolute value symbols. \n We end up getting h + k for both."
geom_inter_1.answers[0] = "h-k, h+k"
geom_inter_1.answers[1] = "h+k"
geom_inter_1.answers[2] = "2(h+k), (h-k)"
geom_inter_1.answers[3] = "h/k"
geom_inter_1.answers[4] = "None of the above"
geom_inter_1.score = 5
geom_inter_1.correct_ans = 1

geom_inter_2 = Question()
geom_inter_2.text = "Problem 2: Brett is holding 3 quarters and 5 dimes. \n Does Brett have more than one dollar or less than one dollar? \n Does the point (3,5) lie above or below the line 0.25x + 0.10y = 1.00?"
geom_inter_2.solution = "Please login with an Upper Canada College google account to view video solution: \n https://brightspace.ucc.on.ca/d2l/le/enhancedSequenceViewer/12007?url=https%3A%2F%2Fc1fe4e8a-1099-4ca2-a1f1-29906d3c031e.sequences.api.brightspace.com%2F12007%2F\nactivity%2F29435%3FfilterOnDatesAndDepth%3D1"
geom_inter_2.answers[0] = "Above, More "
geom_inter_2.answers[1] = "Below, Less "
geom_inter_2.answers[2] = "Below, More "
geom_inter_2.answers[3] = "Above, less "
geom_inter_2.answers[4] = "No idea"
geom_inter_2.score = 5
geom_inter_2.correct_ans = 0

geom_inter_3 = Question()
geom_inter_3.text = "Problem 3: Find the value of p that makes the linear graph: y = p - 3x pass through the point \n where the lines 4x - y = 6 and 2x -5y = 12 intersect. "
geom_inter_3.solution = "Please login with an Upper Canada College google account to view video solution: \n https://brightspace.ucc.on.ca/d2l/le/enhancedSequenceViewer/12007?url=https%3A%2F%2Fc1fe4e8a-1099-4ca2-a1f1-29906d3c031e.sequences.api.brightspace.com%2F12007%2Factivity%2F31005%3FfilterOnDatesAndDepth%3D1"
geom_inter_3.answers[0] = "1"
geom_inter_3.answers[1] = "3"
geom_inter_3.answers[2] = "2"
geom_inter_3.answers[3] = "5"
geom_inter_3.answers[4] = "All of the above"
geom_inter_3.score = 5
geom_inter_3.correct_ans = 0

GI = Subject("GI")
GI.questions.append(geom_inter_1)
GI.questions.append(geom_inter_2)
GI.questions.append(geom_inter_3)
GI.prepare()

#########################################
# Making Geometry Challenging questions
#########################################

geom_chal_1 = Question()
geom_chal_1.text = "Problem 1: Graph the equation y = 3|x-2| - 6. \n What is its vertex, x-intercept and y-intercept (in that order)?"
geom_chal_1.solution = "Both through graphing, and our knowledge that (h,k) is the vertex of any absolute value equation, we find that the vertex must (2, -6) \n Through either plugging in or looking at the graph, we find that the x-intercept is 0 and the y-intercept is 4. "
geom_chal_1.answers[0] = "(-8, -2), 3, 8"
geom_chal_1.answers[1] = "(8, 2), -2, - 2 "
geom_chal_1.answers[2] = "(6, -2), 4, 0 "
geom_chal_1.answers[3] = "(2,-6), 0, 4 "
geom_chal_1.answers[4] = "None of the above"
geom_chal_1.score = 10
geom_chal_1.correct_ans = 3

geom_chal_2 = Question()
geom_chal_2.text = "Problem 2: Two different points on the line y = 2 are each exactly 13 units \n from the point (7,14). Draw a picture of this situation, and then find the coordinates of these points. "
geom_chal_2.solution = "Please login with an Upper Canada College google account to view video solution here: \n https://brightspace.ucc.on.ca/d2l/le/enhancedSequenceViewer/12007?url=https%3A%2F%2Fc1fe4e8a-1099-4ca2-a1f1-29906d3c031e.sequences.api.brightspace.com%2F12007%2Factivity%2F31005%3FfilterOnDatesAndDepth%3D1"
geom_chal_2.answers[0] = "(13,2), (4,5)"
geom_chal_2.answers[1] = "(12,2), (2,2)"
geom_chal_2.answers[2] = "(4,6), (8,2)"
geom_chal_2.answers[3] = "(10,5), (9,3)"
geom_chal_2.answers[4] = "No idea"
geom_chal_2.score = 10
geom_chal_2.correct_ans = 1

geom_chal_3 = Question()
geom_chal_3.text = "Problem 3: Find both points on the line y = 3 that are 10 units from (2, -3)"
geom_chal_3.solution = "Please login with an Upper Canada College google account to view written solution here: \n https://brightspace.ucc.on.ca/d2l/le/enhancedSequenceViewer/12007?url=https%3A%2F%2Fc1fe4e8a-1099-4ca2-a1f1-29906d3c031e.sequences.api.brightspace.com%2F12007%2Factivity%2F31005%3FfilterOnDatesAndDepth%3D1"
geom_chal_3.answers[0] = "(-2,9), (-7,2)"
geom_chal_3.answers[1] = "(3,3), (4,4)"
geom_chal_3.answers[2] = "(-3,-4), (5,-3)"
geom_chal_3.answers[3] = "(10,3), (-6,3)"
geom_chal_3.answers[4] = "All of the above"
geom_chal_3.score = 10
geom_chal_3.correct_ans = 3

#Creates questions and adds them to the subject 
GC = Subject("GC")
GC.questions.append(geom_chal_1)
GC.questions.append(geom_chal_2)
GC.questions.append(geom_chal_3)
GC.prepare()

#############################################
# Making Inequalities Intermediate questions
#############################################
ineq_inter_1 = Question()
ineq_inter_1.text = "Graph the solutions on a number line: |x+8|<20"
ineq_inter_1.solution = "Please login with an Upper Canada College google account to view video solution: \n https://brightspace.ucc.on.ca/d2l/le/enhancedSequenceViewer/12007?url=https%3A%2F%2Fc1fe4e8a-1099-4ca2-a1f1-29906d3c031e.sequences.api.brightspace.com%2F12007%2Factivity%2F29882%3FfilterOnDatesAndDepth%3D1"
ineq_inter_1.answers[0] = "-28<x<12"
ineq_inter_1.answers[1] = "-1<x<24"
ineq_inter_1.answers[2] = "10<x<20"
ineq_inter_1.answers[3] = "19<x<31"
ineq_inter_1.answers[4] = "None of the above"
ineq_inter_1.score = 5
ineq_inter_1.correct_ans = 0

ineq_inter_2 = Question()
ineq_inter_2.text = "Graph the equation: 2x + 3y = 6. Now graph the inequality 2x + 3y <= 6 by shading all the points (x,y) which fit. \n Notice this means shading all the points on one side of the line you drew \n Which side? Use a test point to decide."
ineq_inter_2.solution = "Please login with an Upper Canada College google account to view video solution: \n https://brightspace.ucc.on.ca/d2l/le/enhancedSequenceViewer/12007?url=https%3A%2F%2Fc1fe4e8a-1099-4ca2-a1f1-29906d3c031e.sequences.api.brightspace.com%2F12007%2Factivity%2F29435%3FfilterOnDatesAndDepth%3D1"
ineq_inter_2.answers[0] = "On the line"
ineq_inter_2.answers[1] = "Below "
ineq_inter_2.answers[2] = "Above "
ineq_inter_2.answers[3] = "This area does not exist"
ineq_inter_2.answers[4] = "No idea"
ineq_inter_2.score = 5
ineq_inter_2.correct_ans = 1

ineq_inter_3 = Question()
ineq_inter_3.text = "Calculate the area of the region defined by the simultaneous inequalities y>= x - 4, y <= 10 and 5<= x + y. "
ineq_inter_3.solution = "Please login with an Upper Canada College google account to view video solution: \n https://brightspace.ucc.on.ca/d2l/le/enhancedSequenceViewer/12007?url=https%3A%2F%2Fc1fe4e8a-1099-4ca2-a1f1-29906d3c031e.sequences.api.brightspace.com%2F12007%2Factivity%2F32660%3FfilterOnDatesAndDepth%3D1"
ineq_inter_3.answers[0] = "90"
ineq_inter_3.answers[1] = "359/4"
ineq_inter_3.answers[2] = "357/4"
ineq_inter_3.answers[3] = "361/4"
ineq_inter_3.answers[4] = "All of the above"
ineq_inter_3.score = 5
ineq_inter_3.correct_ans = 3

II = Subject("II")
II.questions.append(ineq_inter_1)
II.questions.append(ineq_inter_2)
II.questions.append(ineq_inter_3)
II.prepare()

#############################################
# Making Inequalities Challenging questions
#############################################

ineq_chal_1 = Question()
ineq_chal_1.text = "The inequality |x - 1.96| <= 1.04 is equivalent to 'x is between ___ and ___.'"
ineq_chal_1.solution = "Please login with an Upper Canada College google account to view video solution: \n'https://brightspace.ucc.on.ca/d2l/le/enhancedSequenceViewer/12007?url=https%3A%2F%2Fc1fe4e8a-1099-4ca2-a1f1-29906d3c031e.sequences.api.brightspace.com%2F12007%2Factivity%2F28822%3FfilterOnDatesAndDepth%3D1"
ineq_chal_1.answers[0] = "1 & 5"
ineq_chal_1.answers[1] = "2 & 4 "
ineq_chal_1.answers[2] = "0.92 & 3 "
ineq_chal_1.answers[3] = "0.96 & 1"
ineq_chal_1.answers[4] = "None of the above"
ineq_chal_1.score = 10
ineq_chal_1.correct_ans = 2

ineq_chal_2 = Question()
ineq_chal_2.text = "Sketch the region that is common to the graphs of x>=2, y>=0 and x+y<=6. What is its area?"
ineq_chal_2.solution = "Please login with an Upper Canada College google account to view video solution: \n https://brightspace.ucc.on.ca/d2l/le/enhancedSequenceViewer/12007?url=https%3A%2F%2Fc1fe4e8a-1099-4ca2-a1f1-29906d3c031e.sequences.api.brightspace.com%2F12007%2Factivity%2F30568%3FfilterOnDatesAndDepth%3D1 "
ineq_chal_2.answers[0] = "24"
ineq_chal_2.answers[1] = "21"
ineq_chal_2.answers[2] = "8"
ineq_chal_2.answers[3] = "16"
ineq_chal_2.answers[4] = "No idea"
ineq_chal_2.score = 10
ineq_chal_2.correct_ans = 2

ineq_chal_3 = Question()
ineq_chal_3.text = "Sketch the region common to the graphs of y >= 1, y - 2x <= 3, x + y <= 6. Find the area of this region."
ineq_chal_3.solution = "Please login with an Upper Canada College google account to view video solution:\n https://brightspace.ucc.on.ca/d2l/le/enhancedSequenceViewer/12007?url=https%3A%2F%2Fc1fe4e8a-1099-4ca2-a1f1-29906d3c031e.sequences.api.brightspace.com%2F12007%2Factivity%2F30568%3FfilterOnDatesAndDepth%3D1"
ineq_chal_3.answers[0] = "27"
ineq_chal_3.answers[1] = "31"
ineq_chal_3.answers[2] = "21"
ineq_chal_3.answers[3] = "3"
ineq_chal_3.answers[4] = "No idea"
ineq_chal_3.score = 10
ineq_chal_3.correct_ans = 0

IC = Subject("IC")
IC.questions.append(ineq_chal_1)
IC.questions.append(ineq_chal_2)
IC.questions.append(ineq_chal_3)
IC.prepare()

####################################################

#Initial topic (in this case it is Geometry Intermediate)
Topic = GI
populateFields()

# end of Mentor
root.mainloop()
import tkinter as tk

 
root = tk.Tk()
root.title("Math Tutor")
root.minsize(950, 950)
root.geometry("950x950")

label1 = tk.Label(root, text = "")

count = 0

def clicked(event):
	global count

	count = count + 1 
	label1.configure(text = "Button was clicked")

button1 = tk.Button(root, command = clicked, text = "click me")

label1.grid(row = 1, column = 1 )
button1.grid(row = 0, column = 0)

root.mainloop()

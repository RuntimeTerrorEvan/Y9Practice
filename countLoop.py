import tkinter as tk

 
root = tk.Tk()
root.title("Math Tutor")
root.minsize(950, 950)
root.geometry("950x950")  

label1 = tk.Label(root, )

count = 0

def clicked(event):
    global count # inform funtion to use external variable `count`

    count = count + 1

    label1.configure(text=f'Button was clicked {count} times!!!')

label1.grid(row = 1, column = 1)

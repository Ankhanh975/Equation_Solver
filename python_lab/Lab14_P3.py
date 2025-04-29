# Problem 3: Simple calculator
import tkinter as tk

# Description:
# The file Lab14 P3.py contains the code snippet of a basic calculator using Tkinter in Python that can
# perform addition, subtraction, multiplication, and division. Complete the application by completing the
# following parts:

def click_button(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)
    
def clear_display():
    display.delete(0, tk.END)
    
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        clear_display()
        display.insert(0, "Error")
        
# Window initialization
# Create the main window
root = tk.Tk()
root.title("Simple Calculator") # title 
root.geometry("300x300") # size 

# Create an Entry widget
display = tk.Entry(root, width=10, font=('Arial', 35)) # Initiate the Entry widget here
display.grid(row=0, column=0, columnspan = 10)

# Define the layout for the calculator buttons ( 0-9 , + , - , * , / , and = ). Arrange them in
# a grid where each row contains a subset of the buttons logically grouped (e.g., digits on one row,
# operators on another).
# • Add a Clear button to reset the displayed value

# Buttons initialization
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), 
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), 
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), 
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), 
    ('C', 5, 0)
]
# Your code is here
# The button list's name is buttons
for (text, row, col) in buttons:
    if text == "C":
        tk.Button(root, text=text, width=9*1, height=2*1, command=lambda:
                    clear_display()).grid(row=row, column=col)
    elif text == "=":
        tk.Button(root, text=text, width=9*1, height=2*1, command=lambda:
                    calculate()).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=9*1, height=2*1, command=lambda text=text:
                click_button(text)).grid(row=row, column=col)
        
root.mainloop()

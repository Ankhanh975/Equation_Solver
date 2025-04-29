import tkinter as tk
import ttkbootstrap as ttk

# window, title
window = ttk.Window(themename = 'darkly', title="My Application")
# size
window.geometry("300x150")


def convert():
    mile_input = entry_int.get()
    km_output = float(mile_input) * 1.61
    output_string.set(km_output)
    
#  Add the label with text Miles to kilometers , and font Calibri 24 bold . This widget grids
# at column = 0 and row = 0 .
l1 = ttk.Label(window, text="Miles to kilometers", font="Calibri 24 bold")
l1.grid(row=0, column=0)

# • Add an Entry field that obtains integer input. This widget grids at column = 0 and row = 1 .
entry_int = ttk.Entry(window)
entry_int.grid(column=0, row=1)

# • Add a Button that has text Convert. This button obtains the function convert defined in the
# code snippet. This button grids at column = 0 and row = 2 .
convert_button = ttk.Button(
    window,
    text="Convert",
    command=convert
)
convert_button.grid(column=0, row=2)
# output
output_string = tk.StringVar()
output_label = ttk.Label(
        master = window,
        text = 'Output',
        font = 'Calibri 24',
        textvariable = output_string)
output_label.grid(column = 0, row = 3)
# run
window.mainloop()

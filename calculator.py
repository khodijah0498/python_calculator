import tkinter as tk
# create the main window
root = tk.Tk()
root.title('simple calaculator')

#Entry wi widget to display the result
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
entry.grid(row=0, column=0, columnspan=4)

current_input = ''

def button_click(value):
    global current_input
    current_input += str(value)
    entry.delete(0, tk.END)
    entry.insert(0, current_input)

def clear_lastchar():
    global current_input
    current_input = current_input[:-1]
    entry.delete(0, tk.END)
    entry.insert(0, current_input)

def clear():
    global current_input
    current_input = ''
    entry.delete(0, tk.END)

def calculate():
    global current_input
    try:
        result = str(eval(current_input))
        entry.delete(0, tk.END)
        entry.insert(0, result)
        current_input = result

    except:
        entry.delete(0, tk.END)
        entry.insert(0, 'Error')
        current_input = ''


buttons= [
    
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'CE', '<-', '0', '+',
    '%', '(',  ')', '='
]

row = 1
col = 0
for button in buttons:
    if button == 'CE':
        tk.Button(root, text=button, width=5, height=2, command=clear).grid(row=row, column=col)
    elif button == '=':
        tk.Button(root, text=button, width=5, height=2,  command=calculate).grid(row=row, column=col)       
    elif button == '<-':
        tk.Button(root, text=button, width=5, height=2,  command=clear_lastchar).grid(row=row, column=col)                                     
    else:
        tk.Button(root, text=button, width=5, height=2, command=lambda x=button: button_click(x)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

#run the main loop
root.mainloop()
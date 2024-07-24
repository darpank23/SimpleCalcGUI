import tkinter as tk


    # Function to update the display when buttons are pressed
def button_click(number):
        current = display.get()
        display.delete(0, tk.END)
        display.insert(0, str(current) + str(number))

    # Function to clear the display
def button_clear():
        display.delete(0, tk.END)

    # Function to perform calculations
def button_equal():
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0, result)
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(0, "ERROR")

    # Create the main window
root = tk.Tk()
root.title("Simple Calculator")

    # Create the display widget
display = tk.Entry(root, width = 16, font = ('Helvetica', 20), justify = 'right')
display.grid(row = 0, column = 0, columnspan = 4)

    # Define Buttons
buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), 
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), 
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), 
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), 
    ]

    # Create buttons and place them in the grid
for button_text, row, col in buttons:
        button = tk.Button(root, text = button_text, width = 4, height = 2, font = ('Helvetica', 14), command = lambda text = button_text: button_click(text))
        button.grid(row = row, column = col)

    # Clear Button
clear_button = tk.Button(root, text = 'C', width = 4, height = 2, font = ('Helvetica', 14), command = button_clear)
clear_button.grid(row = 5, column = 0)

    # Exit Button
exit_button = tk.Button(root, text = 'Exit', width = 4, height = 2, font = ('Helvetica', 14), command = root.quit)
exit_button.grid(row = 5, column = 1)

    # Equal Button
equal_button = tk.Button(root, text = '=', width = 4, height = 2, font = ('Helvetica', 14), command = button_equal)
equal_button.grid(row = 4, column = 2)

root.mainloop()
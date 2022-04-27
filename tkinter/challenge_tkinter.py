import tkinter

buttons_list = [['C', 'CE'], [7, 8, 9, '+'], [4, 5, 6, '-'], [1, 2, 3, '*'], [0, '=', '/']]
mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry('240x240')
mainWindow.minsize(150, 170)
mainWindow['padx'] = 8

# Widget to display the result
result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, columnspan=4, sticky='nsew')

# Buttons
row_num = 1
for b_row in buttons_list:
    col_num = 0

    for button in b_row:
        if button != '=':
            tkinter.Button(mainWindow, text=button).grid(row=row_num, column=col_num, sticky='nsew')
        else:
            tkinter.Button(mainWindow, text=button).grid(row=row_num, column=col_num, sticky='nsew', columnspan=2)
            col_num += 1
        col_num += 1
    row_num += 1

mainWindow.mainloop()

from tkinter import *

root = Tk()
root.title("Stock Analysis")

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=100, padx=200)

# Create company tkinter variable
campany_tnktr = StringVar(root)
# Set the default option
campany_tnktr.set('Select Company')
# Company options
company = {'1', '2', '3', '4', '5'}
# Create company option menu
popupMenu1 = OptionMenu(mainframe, campany_tnktr, *company)
Label(mainframe, text="Company").grid(row=1, column=1)
popupMenu1.grid(row=2, column=1)

# Create country tkinter variable
country_tnktr = StringVar(root)
# Set the default option
country_tnktr.set('Select Country')
# Country options
country = {'A', 'B', 'C', 'D', 'E'}
# Create country option menu
popupMenu2 = OptionMenu(mainframe, country_tnktr, *country)
Label(mainframe, text="Country").grid(row=1, column=3)
popupMenu2.grid(row=2, column=3)

# on change dropdown value
def change_dropdown(*args):
    print(campany_tnktr.get())

Button(mainframe, text ="Get Advisory", command = change_dropdown).grid(row=5, column=2)

# link function to change dropdown
campany_tnktr.trace('w', change_dropdown)
country_tnktr.trace('w', change_dropdown)

root.mainloop()
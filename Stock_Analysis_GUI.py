from tkinter import *
from tkinter import messagebox
import tkinter as tk
from data.Company_Data import getCompanyData

root = Tk()
root.title("Stock Analysis")

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=100, padx=200)

# Create country tkinter variable
country_tnktr = StringVar(root)
# Set the default option
country_tnktr.set('Select Country')
# Country options
country = getCompanyData([],[])['Country'].dropna().unique()
# Create country option menu
popupMenu1 = OptionMenu(mainframe, country_tnktr, *country)
popupMenu1.config(width=13,indicatoron=0,padx=10)
Label(mainframe, text="Country").grid(row=1, column=1)
popupMenu1.grid(row=2, column=1)

# Create Exchange tkinter variable
exchange_tnktr = StringVar(root)
# Set the default option
exchange_tnktr.set('Select Exchange')
# Create exchange option menu
popupMenu2 = OptionMenu(mainframe, exchange_tnktr, '')
popupMenu2.config(width=13,indicatoron=0,padx=10,state=DISABLED)
Label(mainframe, text="Exchange").grid(row=1, column=3)
popupMenu2.grid(row=2, column=3)

# spin = Spinbox(mainframe, from_=0, to=100, width=5)
# spin.grid(column=0, row=0)
# spin.get()

def resetOptions(menu,tnktr,msg):
    menu['menu'].delete(0,'end')
    tnktr.set(msg)

def getAdvisory():
    messagebox.showinfo('', 'Running Stock Advisory for '+exchange_tnktr.get()+' exchange of '+country_tnktr.get())
    resetOptions(popupMenu2, exchange_tnktr,'Select Exchange')
    popupMenu2.config(state=DISABLED)
    advisory_button.config(state=DISABLED)

advisory_button = Button(mainframe, text ="Get Advisory",state=DISABLED, command = getAdvisory,bg="black",fg="white")
advisory_button.grid(row=5, column=2)

def enableButton(*args):
    advisory_button.config(state=NORMAL)

# on change dropdown value
def enableExchange(*args):
    resetOptions(popupMenu2,exchange_tnktr,'Select Exchange')
    exchange_tnktr.set('Select Exchange')
    exchange = getCompanyData([country_tnktr.get()],[])['Exchange'].dropna().unique()
    popupMenu2.config(state=NORMAL)
    advisory_button.config(state=DISABLED)
    for value in exchange:
        popupMenu2['menu'].add_command(label=value, command=tk._setit(exchange_tnktr, value))

# link function to change country dropdown
country_tnktr.trace('w', enableExchange)
exchange_tnktr.trace('w', enableButton)

root.mainloop()
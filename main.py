from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        height1 = float(Height.get())
        weight2 = float(Weight.get())
        height = height1/100
        weight = weight2
        BMI.set(weight/(height*height))
    except ValueError:
        pass

root: Tk = Tk()


root.title("BMI Calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

Height = StringVar()
Weight=StringVar()
BMI = StringVar()

height_entry=ttk.Entry(mainframe,width=7,textvariable=Weight)
height_entry.grid(column=4,row=1,sticky=(N,S))
weight_entry = ttk.Entry(mainframe, width=7, textvariable=Height)
weight_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=2, sticky=E)

ttk.Label(mainframe, text="Height(cm)").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe,text="Weight(kg)").grid(column=3,row=1,sticky=N)
ttk.Label(mainframe, text="Your BMI").grid(column=2, row=3, sticky=E)
bmi_entry=ttk.Entry(mainframe,width=4,textvariable=BMI)
bmi_entry.grid(column=3,row=3,sticky=(E))


for child in mainframe.winfo_children(): child.grid_configure(padx=8, pady=8)


root.mainloop()

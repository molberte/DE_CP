import matplotlib
from matplotlib import pyplot as plt
from tkinter import *
from tkinter import ttk
from plotting import Points, Plot


root = Tk()
root.title("DE_practicum")
matplotlib.use('TkAgg')

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.configure(background='#f5dadf')


class Parameter:
    def __init__(self, text, row, column, value):
        self.text = text
        self.row = row
        self.column = column
        self.value = value
        t = Label(text=self.text, font=("Century Gothic", 12, "normal"))
        t.config(width=6, height=1, bg='#f5dadf')
        t.grid(row=self.row, column=self.column)
        self.entry = Entry(width=10, textvariable = self.value)
        self.entry.grid(row=self.row + 1, column=self.column)


def plot(event):
    x0.value = float(x0.entry.get())
    y0.value = float(y0.entry.get())
    X.value = float(X.entry.get())
    N.value = int (N.entry.get())
    n0.value = int (n0.entry.get())
    nmax.value = int(nmax.entry.get())
    return Plot.plot(x0.value, y0.value, X.value, N.value, n0.value, nmax.value)


label1 = Label(text="parameters", font=("Century Gothic", 12, "normal"))
label1.config(width=13, height=1, bg='#f5dadf')
label1.grid(row=1, column=3, columnspan = 2)

# Creating instances of class Parameter with given text and row/column position
x0 = Parameter("x_0", 2, 3, 0.0)
y0 = Parameter("y_0", 2, 4, 1.0)
X = Parameter("X", 4, 3, 10)
N = Parameter("N", 4, 4, 1)

label2 = Label(text="errors", font=("Century Gothic", 12, "normal"))
label2.config(width=13, height=1, bg='#f5dadf')
label2.grid(row=6, column=3, columnspan = 2)

n0 = Parameter("n_0", 7, 3, 2)
nmax = Parameter("n_max", 7, 4, 3)

label3 = Label(text="Enter values", font=("Century Gothic", 12, "normal"))
label3.config(width=13, height=1, bg='#f5dadf')
label3.grid(row=3, column=1, columnspan = 2)

button = Button(text = "Plot!", width=10, height=2, bg='white', fg = 'black')
button.bind("<Button-1>", plot)
button.grid(row=4, column=1, columnspan = 2)


root.mainloop()

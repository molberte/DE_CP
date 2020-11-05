# Differential equations
## Computational practicum
####Kseniya Kudasheva BS19-02




![first part](https://github.com/molberte/DE_CP/raw/main/screenshots/DE_1.jpg)

![second part](https://github.com/molberte/DE_CP/raw/main/screenshots/DE_2.jpg)

![third part](https://github.com/molberte/DE_CP/raw/main/screenshots/DE_3.jpg)

![forth part](https://github.com/molberte/DE_CP/raw/main/screenshots/DE_4.jpg)

####Implementation

I chose Python language for implementation with three libraries imported:
MatPlotlib for graph plotting, Tkinter for GUI, and Pandas for better experience 
of calculating the results of different Numerical Methods

**GUI**

GUI provides the possibility to input values of x0, y0, X, N, n0 and n_max

![window](https://github.com/molberte/DE_CP/raw/main/screenshots/window.jpg)

Insert some values into windows for corresponding parameters:

![window_data](https://github.com/molberte/DE_CP/raw/main/screenshots/window_and_values.jpg)

Press 'Plot!' button...

Wait for a little

And some magic  is happening:

![plot](https://github.com/molberte/DE_CP/raw/main/screenshots/plot.jpg)


**UML diagrams**

I divided code into 4 parts: numeric_methods, error_calculator, plotting and main

Well, names give description of each part intuitively

![UML](https://github.com/molberte/DE_CP/raw/main/screenshots/uml_white.jpg)

**numeric_methods** is a directory that contains all methods and functions used
for calculations

**error_calculator** is also a directory that contains a .py file which performs 
calculation of local errors

**plotting.py** is responsible for graphs plotting

and **main.py** is responsible for set and start of software itself


Each numeric method contains the function *solve*, which allows to find
values of a particular approximation method




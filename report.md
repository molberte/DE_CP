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

Wait for a little.....

And some magic  is happening:

![plot](https://github.com/molberte/DE_CP/raw/main/screenshots/plot.jpg)


**Convergence**

Testing my program on different grid sizes showed that the value of error
of Runge-Kutta method is the biggest with the lowest amount of points and vice versa

The picture below illustrates the dependence of maximum error for each method
on the number of grid cells (N)
Graphs for IVP in my task and N = 10, 50, 100, 500, 1000 respectively

![graphs](https://github.com/molberte/DE_CP/raw/main/screenshots/te1.jpg)

The larger N, the closer the methods are to the correct value. This fact explains that the
smaller the step, the fewer errors in general

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


Each numeric method is a class that contains the function *solve*, which allows to find
values of a particular approximation method

![methods](https://github.com/molberte/DE_CP/raw/main/screenshots/classes.jpg)

#### Most interesting parts of code

Honestly speaking, I do not find any pieces of my code interesting somehow
but I would like to impress my reader and add some examples.

While I was searching for examples, I found the piece of code which *I
 very proud of:*

![proud](https://github.com/molberte/DE_CP/raw/main/screenshots/class_parameter.jpg)

Why am I proud? 

Firstly, I did not know how to initialize instance of a class

Secondly, I prevented nested and copied parts of code

So now, when you need to create additional parameter with entry window,
you can just create instance of this class with some values and do not write 
it manually


*Base functions*

![base](https://github.com/molberte/DE_CP/raw/main/screenshots/base.jpg)

There are very basic function of given differential equation: equation itself,
constant C, and exact solution of given equation

*Improved Euler*

![IEM](https://github.com/molberte/DE_CP/raw/main/screenshots/class_improved.jpg)

Also, there are few classes which based on previous one (*Functions*)

Along with Improved Euler method, there also are Euler method, Exact solution,
and Runge-Kutta method

I decided to provide an example of these methods with Improved Euler method

*Errors*

![error](https://github.com/molberte/DE_CP/raw/main/screenshots/class_error.jpg)

Here you can see the class that is used for local errors calculation.
It takes two lists of points (points of approximation method 
and exact solution points) and find the absolute value of their difference

*Plotting*

![plot](https://github.com/molberte/DE_CP/raw/main/screenshots/class_plot.jpg)

There is an example of one graph (out of three) plotting 
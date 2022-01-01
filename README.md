# Function-Plotter
Function Plotter is a simple application with GUI to plot mathematical functions. User enter a function and its boundaries and the application plot the function. Application can only draw polynomial functions in which only these operators in the fucntion are allowed: + - * / ^ (where ^ is the power operator).

## Prerequisites 
python is needed to be installed on the device. In addition, install these libraries: PyQt5, matplotlib, and numpy using:
```
pip install [library name]
```
## How to Run
run command:
```
python3 Function_Plotter.py
```

## Program Results Screenshots
#### Note: Program enforce function input field to only accept allowed symbols and letter 'x'. Also enforce minimum value and maximum value to be numeric values
* Program Interface <br/><br/>

![Design](https://github.com/El-Nebo/Function-Plotter/blob/main/Screens/Design.PNG)

![Valid1](https://github.com/El-Nebo/Function-Plotter/blob/main/Screens/Valid1.PNG)

![Valid2](https://github.com/El-Nebo/Function-Plotter/blob/main/Screens/Valid2.PNG)

![Valid3](https://github.com/El-Nebo/Function-Plotter/blob/main/Screens/Valid3.PNG)

* Entering empty function <br/><br/>

![EmptyFunction](https://github.com/El-Nebo/Function-Plotter/blob/main/Screens/EmptyFunction.PNG)

* Entering empty minimum value of x <br/><br/>

![EmptyMinX](https://github.com/El-Nebo/Function-Plotter/blob/main/Screens/EmptyMinX.PNG)

* Entering empty maximum value of x <br/><br/>

![emptyMaxX](https://github.com/El-Nebo/Function-Plotter/blob/main/Screens/emptyMaxX.PNG)

* Entering nonvalid function <br/><br/>

![NonValidFunction](https://github.com/El-Nebo/Function-Plotter/blob/main/Screens/NonValidFunction.PNG)

* Entering minimum value greater than maximum value <br/><br/>

![minGreaterThanMax](https://github.com/El-Nebo/Function-Plotter/blob/main/Screens/minGreaterThanMax.PNG)

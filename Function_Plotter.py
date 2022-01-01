import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QGridLayout, QPushButton, QMessageBox
from PyQt5 import QtGui, QtCore


class Function_Plotter(QDialog):
    def __init__(self):
        """
        Plotter construtor: initializing the window and values of the plotter 
        """
        super().__init__()
        self.setWindowTitle("Function Plotter")
        self.setGeometry(80, 80, 800, 800)

        self.createHeader()
        self.createCanvas()
        self.setLayoutStyle()

        #for testing 
        self.xValues = []
        self.yValues = []
        self.errorcode =0
        """
        there are 5 error codes from 1 to 5 corrosponding to different errros:
            1 - empty function
            2 - empty minimum value of x
            3 - empty maximum value of x
            4 - minimum value of x is greater than maximum value of x
            5- nonvalid function
        """

    def showError(self, message):
        """
        function to show error to user when violating program rules 
        Args:
            message (string): message to show to user
        """
        messageBox = QMessageBox()
        messageBox.warning(self, 'Error', message)

    def createHeader(self):
        """
        function to create header widgets (function input, min value of x, max value of x, and plot button)
        """
        regex = QtCore.QRegExp("(?:[0-9-+*/^()x])+")
        functionvalidator = QtGui.QRegExpValidator(regex)

        self.functionLabel = QLabel('f(x):')
        self.functionInput = QLineEdit()
        self.functionInput.setPlaceholderText('function can only contain: x + - * / ^ ( ) ')
        self.functionInput.setValidator(functionvalidator)

        minmaxValidator = QtGui.QDoubleValidator(self)

        self.minXLabel = QLabel('Minimum Value of x:')
        self.minXInput = QLineEdit()
        self.minXInput.setPlaceholderText('Must be a number')
        self.minXInput.setValidator(minmaxValidator)

        self.maxXLabel = QLabel('Maximum Value of X:')
        self.maxXInput = QLineEdit()
        self.maxXInput.setPlaceholderText('Must be a number')
        self.maxXInput.setValidator(minmaxValidator)

        self.PlotButton = QPushButton('Plot')
        self.PlotButton.clicked.connect(self.onClickListner)
    
    def createCanvas(self):
        """
        function to create canvas widgets and axes 
        """
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        self.canvas.axes = self.fig.add_subplot(111)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('function f(x)')
        self.toolbar =  NavigationToolbar(self.canvas, self)
        
    def setLayoutStyle(self):
        """
        function to add layout widgets (header and canvas) to the main layout 
        and adjust their positions 
        """
        layout = QGridLayout()
        layout.addWidget(self.functionLabel,0,0)
        layout.addWidget(self.functionInput,0,1)
        layout.addWidget(self.minXLabel,1,0)
        layout.addWidget(self.minXInput,1,1)
        layout.addWidget(self.maxXLabel,2,0)
        layout.addWidget(self.maxXInput,2,1)
        layout.addWidget(self.PlotButton,3,0,1,2)
        layout.addWidget(self.toolbar,4,0,1,2)
        layout.addWidget(self.canvas,5,0,1,2)
        self.setLayout(layout)

    def validateInput(self):
        """
        function to validate user input. Note: some validations are applied implictly 
        """
        if self.functionInput.text()=='':
            self.showError('Enter a function')
            self.errorcode = 1
            return False
        if self.minXInput.text() == '':
            self.showError('Enter minimum value of x')
            self.errorcode = 2
            return False
        if self.maxXInput.text()=='':
            self.showError('Enter maximum value of x')
            self.errorcode = 3
            return False

        if float(self.minXInput.text()) >= float(self.maxXInput.text()):
            self.showError('Maximum value of x must be greater than minimum value of x')
            self.errorcode = 4
            return False
        
        return True

    def plot(self,function,minX,maxX):
        """
        function to plot the function on the canvas given that inputs are validated  
        Args:
            function (string): function that user entered 
            minX(int): minimum value of x that user entered
            maxX(int): maximum value of x that user enterd 
        
        """
        x = np.linspace(minX, maxX)
        try:
            y = eval(function)
        except:
            self.showError("Please enter a valid function")
            self.errorcode = 5
            return
        self.fig.clear()
        self.canvas.axes = self.fig.add_subplot(111)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('function f(x)')
        self.canvas.axes.plot(x,y)
        self.canvas.draw()
        
        
    def onClickListner(self):
        """
        function to execute when clicking plot button. it validates the inputs and then plot the function 
        """
        if not self.validateInput() : 
            return
        self.plot(
            self.functionInput.text().lower().replace('^', '**'),
            float(self.minXInput.text()),
            float(self.maxXInput.text()),
        )


app = QApplication(sys.argv)
plotter = Function_Plotter()
plotter.show()
sys.exit(app.exec_())

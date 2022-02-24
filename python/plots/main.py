import sys
import matplotlib
matplotlib.use("Qt5Agg")

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

     # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        # First array is X and the second - Y
        with open("input.txt", "r") as inputData:
            data = inputData.read()        
            x, y = data.split("\n")
            x = list(map(float, x.split(",")))
            y = list(map(float, y.split(","))) 
            # 0.01,0.02,0.03,0.04,0.05,   22.45,37.64,61.35,79.50,101.20,
        # x = [79.25,79.35,79.45,79.55,79.65,79.80,79.85,79.95,80.05,80.15,80.25,80.35,80.45,80.55,80.65,80.75]
        # y = [0.03,0.03,0.04,0.05,0.06,0.07,0.09,0.09,0.10,0.10,0.09,0.07,0.06,0.04,0.04,0.04]
        
            sc.axes.plot(x, y)
            self.setCentralWidget(sc)

            # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
            toolbar = NavigationToolbar(sc, self)

            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(toolbar)
            layout.addWidget(sc)

            # Create a placeholder widget to hold our toolbar and canvas.
            widget = QtWidgets.QWidget()
            widget.setLayout(layout)
            self.setCentralWidget(widget)

            self.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec_()


if __name__ == '__main__':
    main()

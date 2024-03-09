import sys
#from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFont
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
def window():
   app = QApplication(sys.argv)
   widget = QWidget()

   textLabel = QLabel(widget)
   textLabel.setText("Hello World!")
   textLabel.move(210,185)
   textLabel.setFont(QFont('Arial', 40))

   textLabel = QLabel(widget)
   textLabel.setText("Hello Heaven!")
   textLabel.move(210,5)
   textLabel.setFont(QFont('Verdana', 20))

   widget.setGeometry(50,50,920,600)
   widget.setWindowTitle("PyQt5 Example")
   widget.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()
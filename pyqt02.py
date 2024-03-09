import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class AddNumbersApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Add Numbers')
        self.setGeometry(100, 100, 300, 150)

        # Create a vertical layout
        layout = QVBoxLayout()

        # Create input fields for numbers
        self.num1_label = QLabel('Enter the First Number:')
        self.num1_input = QLineEdit()
        self.num2_label = QLabel('Enter the Second Number:')
        self.num2_input = QLineEdit()

        # Create a label to display the result
        self.result_label = QLabel('Result:')

        # Create a button to perform addition
        self.add_button = QPushButton('Add')

        # Connect the button click event to the addition function
        self.add_button.clicked.connect(self.performAddition)

        # Add widgets to the layout
        layout.addWidget(self.num1_label)
        layout.addWidget(self.num1_input)
        layout.addWidget(self.num2_label)
        layout.addWidget(self.num2_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.result_label)

        # Set the layout for the main window
        self.setLayout(layout)

    def performAddition(self):
        try:
            # Get the numbers from the input fields
            num1 = float(self.num1_input.text())
            num2 = float(self.num2_input.text())

            # Perform the addition
            result = num1 + num2

            # Display the result
            self.result_label.setText(f'Result: {result}')
        except ValueError:
            # Handle invalid input (e.g., non-numeric input)
            self.result_label.setText('Invalid input')

def main():
    app = QApplication(sys.argv)
    window = AddNumbersApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
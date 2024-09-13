# This application is built with PyQt5 and is using
# CurrencyLayer API to access current rate of a currency
# that the user inputs.
 

import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class ForexApp(QWidget):
    def __init__(self):
        super().__init__()
        self.main_currency_label = QLabel("Enter main currency: ", self)
        self.main_currency_input = QLineEdit(self)
        self.quote_currency_label = QLabel("Enter quote currency: ", self)
        self.quote_currency_input = QLineEdit(self)
        self.get_rate_button = QPushButton("Get Rate", self)
        self.rate_label = QLabel(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Forex App")
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.main_currency_label)
        vbox.addWidget(self.main_currency_input)
        vbox.addWidget(self.quote_currency_label)
        vbox.addWidget(self.quote_currency_input)
        vbox.addWidget(self.get_rate_button)
        vbox.addWidget(self.rate_label)
        
        self.setLayout(vbox)
        
        self.main_currency_label.setAlignment(Qt.AlignCenter)
        self.main_currency_input.setAlignment(Qt.AlignCenter)
        self.quote_currency_label.setAlignment(Qt.AlignCenter)
        self.quote_currency_input.setAlignment(Qt.AlignCenter)
        self.rate_label.setAlignment(Qt.AlignCenter)
        
        self.main_currency_label.setObjectName("main_currency_label")
        self.main_currency_input.setObjectName("main_currency_input")
        self.quote_currency_label.setObjectName("quote_currency_label")
        self.quote_currency_input.setObjectName("quote_currency_input")
        self.get_rate_button.setObjectName("get_rate_button")
        self.rate_label.setObjectName("rate_label")
        
        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#main_currency_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#main_currency_input{
                font-size: 40px;
            }
            QLabel#quote_currency_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#quote_currency_input{
                font-size: 40px;
            }
            QPushButton#get_rate_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#rate_label{
                font-size: 75px;
            }
        """)
        
        self.get_rate_button.clicked.connect(self.get_rate)
    
    def get_rate(self):
        
        api_key = "a48b0156130354768f751a31a8f0c7bd"
        main_currency = self.main_currency_input.text()
        quote_currency = self.quote_currency_input.text()
        url = f"https://api.currencylayer.com/convert?access_key={api_key}&from={main_currency}&to={quote_currency}&amount=1"
        
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # The following line is showing the inside structure
        # of data, which is used to access the data :)
        print(data)
        
        self.display_rate(data, main_currency, quote_currency)
        
    
    def display_rate(self, data, main_currency,quote_currency):
        self.rate_label.setStyleSheet("font-size: 75px;")
        currency = main_currency + quote_currency
        print("\n",currency, "\n")
        rate = data["result"]
        
        self.rate_label.setText(f"{rate}")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    rate_app = ForexApp()
    rate_app.show()
    sys.exit(app.exec_())
    
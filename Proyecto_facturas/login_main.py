import sys
from PyQt6.QtWidgets import (QApplication,QMainWindow,QMessageBox)
from views.login_view import Ui_MainWindow
from windows.main_main import main

from db.conexionDB import cursor1
from db.conexionDB import psycopg2
from db.conexionDB import bcrypt

class login(QMainWindow):
    def __init__(self):
        super(login, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.is_logged = False
    
        self.ui.loginButton.clicked.connect(self.logins)

      
    def logins(self):
        try:
            password = self.ui.passwordInput.text().encode()
            sql = "select * from users where usuario = %s"
            user = self.ui.userImput.text()
            cursor1.execute(sql, (user,))
            resultado = cursor1.fetchone()

            if resultado is None:
                QMessageBox.warning(self, "Error", 
                                "El usuario no existe",
                                QMessageBox.StandardButton.Close, 
                                QMessageBox.StandardButton.Close)
            else:
                resultado_encoded = resultado[2].encode() 
                if bcrypt.checkpw(password, resultado_encoded):
                    QMessageBox.information(self, "Login", 
                                        "Login Correcto", 
                                        QMessageBox.StandardButton.Ok, 
                                        QMessageBox.StandardButton.Ok)
                    self.is_logged = True
                    self.close()
                    self.openMainWindow()
                else:
                    QMessageBox.warning(self, "Error", 
                                    "Credenciales incorrectas",
                                    QMessageBox.StandardButton.Close, 
                                    QMessageBox.StandardButton.Close)
        except psycopg2.Error:
            QMessageBox.critical(self, "Error", 
                             "Error en la conexión con la base de datos",
                             QMessageBox.StandardButton.Close, 
                             QMessageBox.StandardButton.Close)
            

    def openMainWindow(self):
        self.main = main()
        self.main.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = login()
    ventana.show()
    sys.exit(app.exec())
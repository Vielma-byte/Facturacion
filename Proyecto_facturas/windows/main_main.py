import sys
from PyQt6.QtWidgets import (QApplication,QMainWindow,QMessageBox)
from views.main_view import Ui_MainWindow


class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.is_logged = False
    
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = main()
    ventana.show()
    sys.exit(app.exec())
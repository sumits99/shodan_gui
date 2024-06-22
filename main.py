import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt6.QtCore import pyqtSlot, QFile, QTextStream, QIODevice
from core.sidebar_ui import Ui_MainWindow
from core.creds import CredStore, pathlib
import json

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)
        self.c = CredStore()
        self.cache_file_path = pathlib.Path.home().joinpath("pyqt_encrypted_data").__str__()
        self.load_settings()
    
    ## Function for search
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_9.setText(search_text)
    
    ## Function for changing page to user page
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)
                  
    ## Change QPushButton Checkable status when stackWidget index changed
    def on_stackWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton)\
            + self.ui.full_menu_widget.findChildren(QPushButton)
        
        for btn in btn_list:
            if index in [5,6]:
                btn.setAutoExclusive(False)
                btn.setCheckable(False)
            else:
                btn.setAutoExclusive(True)
    
    ## Functions for changing menu page
    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_dashboard_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    
    def on_dashboard_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    
    def on_orders_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    
    def on_orders_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    
    def on_products_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_products_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_customers_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_customers_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_kb_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    def on_settings_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(8)

    def on_btn_save_token_clicked(self):
        token=self.ui.edit_token.text()
        self.ui.btn_save_token
        temp = {
            "token": token
        }
        temp = json.dumps(temp)
        edata = self.c.encrypt_data(temp)
        self.c.save_encrypted_data(self.cache_file_path, edata)
        self.load_settings()
    
    def load_settings(self):
        edata =self.c.load_encrypted_data(self.cache_file_path)
        if not edata:
            return
        temp = self.c.decrypt_data(edata)
        temp = json.loads(temp)
        token=temp["token"]
        self.ui.edit_token.setText(token)
            
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
                      
                      /*= Style for mainwondow START
    ========================================= */
    #MainWindow {
        background-color: #fff;
    }
/*= END
    ========================================= */


/*= Style for button to change menu START
    ========================================= */
    #change_btn {
        padding: 5px;
        border: none;
        width: 30px;
        height: 30px;
    }
/*= END
    ========================================= */


/*= Style for header widget START
    ========================================= */
    #header_widget {
        background-color: #f9fafd;
    }
/*= END
    ========================================= */


/*= Style for menu with icon only START
    ========================================= */
  	/* style for widget */
    #icon_only_widget {
		background-color: #313a46;
		width:50px;
	}

    /* style for QPushButton and QLabel */
	#icon_only_widget QPushButton, QLabel {
		height:50px;
		border:none;
		/* border-bottom: 1px solid #b0b0b0; */
	}

	#icon_only_widget QPushButton:hover {
		background-color: rgba( 86, 101, 115, 0.5);
	}

	/* style for logo image */
	#logo_label_1 {
		padding: 5px
	}
/*= END
    ========================================= */


/*= Style for menu with icon and text START
    ========================================= */
	/* style for widget */
	#full_menu_widget {
		background-color: #313a46;
	}

	/* style for QPushButton */
	#full_menu_widget QPushButton {
		border:none;
		border-radius: 3px;
		text-align: left;
		padding: 8px 0 8px 15px;
		color: #788596;
	}

	#full_menu_widget QPushButton:hover {
		background-color: rgba( 86, 101, 115, 0.5);
	}

	#full_menu_widget QPushButton:checked {
		color: #fff;
	}

	/* style for logo image */
	#logo_label_2 {
		padding: 5px;
		color: #fff;
	}

	/* style for APP title */
	#logo_label_3 {
		padding-right: 10px;
		color: #fff;
	}
/*= END
    ========================================= */


/*= Style for search button START
    ========================================= */
	#search_btn {
		border: none;
	}
/*= END
    ========================================= */


/*= Style for search input START
    ========================================= */
	#search_input {
		border: none;
		padding: 5px 10px;
	}

	#search_input:focus {
		background-color: #70B9FE;
	}
/*= END
    ========================================= */


/*= Style for user information button START
    ========================================= */
	#user_btn {
		border: none;
	}
/*= END
    ========================================= */
                      """)

    ## loading style file, Example 2
    # style_file = QFile("style.qss")
    # style_file.open(QFile.ReadOnly | QFile.Text)
    # style_stream = QTextStream(style_file)
    # app.setStyleSheet(style_stream.readAll())

    window = MainWindow()
    window.show()

    ## loading style file (Example 2)
    
    sys.exit(app.exec())
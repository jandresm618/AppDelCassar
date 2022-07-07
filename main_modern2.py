from GUI.ui_main_interface import *

########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
########################################################################

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

		self.ui = Ui_MainWindow()
		self.setupUi(self)

		
		loadJsonStyle(self, self.ui)
        
	
if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.show()
	app.exec_() 
	
	   

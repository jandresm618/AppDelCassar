from tkinter import ttk 
from tkinter import *
from tkinter import messagebox
from manejo_datos import *

class MainWindow(object):
	"""docstring for MainWindow"""
	def __init__(self):
		super(MainWindow, self).__init__()
		
		self.loadData()
		self.windowInit()
		self.loadButtonOptions()

		self.window.mainloop()

	def loadData(self):
		self.info_Container = InfoContainer()	
		self.frameWidgets = []
		self.dictRunning = {'ventas':False,'compras':False,'cuadre':False,'notificaciones':False,'balance':False}
		

	def windowInit(self):
		self.window = Tk()
		self.window.attributes('-fullscreen', True)		
		self.window.config(bg = "red")
		self.window.title('DelCassarApp')
		#self.window.state('zoomed')
		#self.window.pack()

	def loadButtonOptions(self):
		"""ATRIBUTOS DE HEADER"""
		self.headerFrame = LabelFrame(self.window)
		self.headerFrame['text']='Menú'		
		#self.headerFrame.grid(row = 0, column= 0, columnspan=20,sticky=W + E)
		self.headerFrame.place(x=500,y=150)
		self.headerFrame.config(bg="white")
		
		"""ATRIBUTOS DE LOGO"""
		self.logoDelCassar = PhotoImage(file = "Archivos/Logo.png")
		self.logoLabel = Label(self.headerFrame,image = self.logoDelCassar)				
		self.logoLabel.grid(row=0,column=0,sticky= W + E, columnspan=3)
			
		"""ATRIBUTOS DE BOTON OPCION VENTAS Y BUSQUEDA"""
		self.saleButton = ttk.Button(self.headerFrame,command=self.saleButtonSlot)
		#self.saleButton = ttk.Button(self.headerFrame)
		self.saleButton['text']='BUSQUEDA Y VENTAS'
		self.saleButton.grid(row=1,column=0,sticky=W,padx=2,pady=10)
		
		"""ATRIBUTOS DE BOTON OPCION COMPRAS Y BUSQUEDA"""
		self.buyButton = ttk.Button(self.headerFrame,command=self.buyButtonSlot)
		#self.buyButton = ttk.Button(self.headerFrame)
		self.buyButton['text']='COMPRAS Y PLANEACION'
		self.buyButton.grid(row=2,column=0,sticky=W,padx=2,pady=10)

		"""ATRIBUTOS DE BOTON OPCION CUADRE DIARIO"""
		self.cashRegisterButton=ttk.Button(self.headerFrame,command=self.cashRegisterButtonSlot)
		self.cashRegisterButton['text']='CUADRE DIARIO'
		self.cashRegisterButton.grid(row=3,column=0,sticky=W,padx=2,pady=10)

		"""ATRIBUTOS DE BOTON OPCION NOTIFICACIONES"""
		#self.notifyButton=ttk.Button(self.headerFrame,command=self.notifySlot)
		#self.notifyButton['text']='NOTIFICACIONES, PEDIDOS Y RECORDATORIOS'
		#self.notifyButton.grid(row=4,column=0,sticky=W,padx=2,pady=10)

		"""ATRIBUTOS DE BOTON OPCION BALANCE Y ESTADISTICAS"""
		#if self.owner:
		#	self.stadisticsButton=ttk.Button(self.headerFrame,command=self.balanceSlot)
		#	self.stadisticsButton['text']='BALANCE MONETARIO'
		#	self.stadisticsButton.grid(row=5,column=0,sticky=W,padx=2,pady=10)

		"""ATRIBUTOS DE BOTON OPCION CAMBIO DE USUARIO"""
		#self.switchButton = ttk.Button(self.headerFrame,command=self.switchSlot)
		#self.switchButton['text']='CAMBIAR DE USUARIO'
		#self.switchButton.grid(row=6,column=0,sticky=W,padx=2,pady=10)

		"""ATRIBUTOS DE BOTON OPCION SALIR"""
		self.exitButton=ttk.Button(self.headerFrame,command=self.exitSlot)
		self.exitButton['text']='SALIR'
		self.exitButton.grid(row=7,column=0,sticky=W,padx=2,pady=10)		

		"""FRAME """
		self.frame = LabelFrame(self.window)
		self.frame['text'] = 'Bienvenidos a DelCassarApp'
		self.frame.grid(row = 1, column= 0, columnspan=3, pady=5,padx=10)	

	def headerDesing(self):
		self.headerFrame.grid(row = 0, column= 0, columnspan=20,sticky=W + E, pady=20)
		self.saleButton.grid(row=1,column=0,sticky=W,padx=2)
		self.buyButton.grid(row=1,column=1,sticky=W,padx=2)
		self.cashRegisterButton.grid(row=1,column=2,sticky=W,padx=2)

		#self.notifyButton.grid(row=1,column=3,sticky=W,padx=2)

		#if self.owner:			
		#	self.stadisticsButton.grid(row=1,column=4,sticky=W,padx=2)
		
		#self.switchButton.grid(row=1,column=5,sticky=W,padx=2)	

		self.exitButton.grid(row=1,column=7,sticky=W,padx=2)	
			
	def loadSearchFrame(self):
		##################  Frame de busqueda de productos  #######################
		self.searchFrame = LabelFrame(self.frame)
		self.searchFrame['text'] = 'Busqueda de Productos'
		self.searchFrame.grid(row = 0, column= 0, columnspan=1, pady=1,padx=10)			

		self.searchLabel=Label(self.searchFrame)		
		self.searchLabel['text']='Nombre: '
		self.searchLabel.grid(row=1,column=0,padx=3)
		self.frameWidgets.append(self.searchLabel)


		self.searchName=Entry(self.searchFrame,bg='white')
		self.searchName.focus()
		self.searchName.grid(row=1,column=1)
		self.frameWidgets.append(self.searchName)

		self.message = Label(self.searchFrame,text="",fg = 'red')
		self.message.grid(row=2,column=0,columnspan=2,sticky=W + E)
		self.frameWidgets.append(self.message)

		#self.searchButton=ttk.Button(self.searchFrame,command=self.searchProduct)
		self.searchButton=ttk.Button(self.searchFrame)
		self.searchButton['text']='Buscar'
		self.searchButton.grid(row=1,column=2,sticky=W + E,columnspan=2,pady=1)
		self.frameWidgets.append(self.searchButton)

				
		self.searchTable=ttk.Treeview(self.searchFrame,height=10,columns=4)
		self.searchTable.grid(row=4,column=0,columnspan=10,padx=1)
		self.searchTable['columns']=['Column 2','Column 3','Column 4']
		self.searchTable.column('#0',width=70,anchor=CENTER)
		self.searchTable.heading('#0',text='Codigo')
		self.searchTable.column('#1',width=400,anchor=CENTER)
		self.searchTable.heading('#1',text='Nombre')
		self.searchTable.column('#2',width=100,anchor=CENTER)
		self.searchTable.heading('#2',text='Precio')
		self.searchTable.column('#3',width=100,anchor=CENTER)
		self.searchTable.heading('#3',text='Cantidad')
		self.frameWidgets.append(self.searchTable)

		for elem in self.info_Container.getProducts():
			self.searchTable.insert("",10,text = elem.Codigo(),values=(elem.Nombre(),elem.Precio(),elem.Cantidad()))

		#self.addProductButton=ttk.Button(self.searchFrame,command=self.addSellProduct)
		self.addProductButton=ttk.Button(self.searchFrame)
		self.addProductButton['text']='Añadir al Carrito'
		self.addProductButton.grid(row=5,column=0,sticky=W + E,columnspan=2,pady=10)
		self.frameWidgets.append(self.addProductButton)		
			
	def	saleButtonSlot(self):
		self.headerDesing()
		self.loadSearchFrame()
	def	buyButtonSlot(self):
		pass
	def	cashRegisterButtonSlot(self):
		pass

	def exitSlot(self):		
		#print(messagebox.askyesno(message="¿Desea continuar?", title="Título"))
		if messagebox.askokcancel(message="¿Desea continuar?", title="AVISO"):
			#self.stopRunning()
			self.headerFrame.destroy()
			self.window.destroy()		

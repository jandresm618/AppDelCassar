from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk 
from matplotlib.figure import Figure
from tkinter import ttk 
from tkinter import *
from manejo_datos import *
from tkinter import messagebox
#from ventanas import *


			#~~~~~~~~~~~~~~~~~~~~~~!!!!!FRAME MENU DE OPCIONES!!!!!!~~~~~~~~~~~~~~~~~~~~~~#
			#~~~~~~~~~~~~~~~~~~~~~~!!!!!DISPONIBLE PARA USUARIOS!!!!!!~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~
#Clase encargada de administrar cada funcion del programa
class Menu(object):
	"""CONSTRUCTOR DE CLASE MENU"""
	def __init__(self):
		super(Menu, self).__init__()
		"""INICIALIZACION DE ATRIBUTOS TKINTER"""
		self.window = Tk()
		self.window.attributes('-fullscreen', True)		
		self.window.config(bg = "red")
		self.window.title('DelCassarApp')
		#self.window.state('zoomed')

		"""DICT DE OPCION DE VENTANA """
		self.dictRunning = {'ventas':False,'compras':False,'cuadre':False,'notificaciones':False,'balance':False}

		"""INICIALIZACION DE CLASE CONTENEDOR DE INFORMACION EXTERIOR"""
		self.info_Container = InfoContainer()

		"""DUEÑO POR DEFECTO"""		
		self.owner = True
		
		"""VENTANA INICIAL""" #--> SE DESEA CONTROL DE USUARIO
		self.frameInit()			
		self.window.mainloop()

#---------- ------ METODOS DE DISEÑO ------------------------#
	"""DISEÑO DE VENTANA INICIAL"""
	def frameInit(self):
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
		self.saleButton = ttk.Button(self.headerFrame,command=self.saleSlot)
		self.saleButton['text']='BUSQUEDA Y VENTAS'
		self.saleButton.grid(row=1,column=0,sticky=W,padx=2,pady=10)
		
		"""ATRIBUTOS DE BOTON OPCION COMPRAS Y BUSQUEDA"""
		self.buyButton = ttk.Button(self.headerFrame,command=self.buySlot)
		self.buyButton['text']='COMPRAS Y PLANEACION'
		self.buyButton.grid(row=2,column=0,sticky=W,padx=2,pady=10)

		"""ATRIBUTOS DE BOTON OPCION CUADRE DIARIO"""
		self.cashRegisterButton=ttk.Button(self.headerFrame,command=self.cashRegisterSlot)
		self.cashRegisterButton['text']='CUADRE DIARIO'
		self.cashRegisterButton.grid(row=3,column=0,sticky=W,padx=2,pady=10)

		"""ATRIBUTOS DE BOTON OPCION NOTIFICACIONES"""
		self.notifyButton=ttk.Button(self.headerFrame,command=self.notifySlot)
		self.notifyButton['text']='NOTIFICACIONES, PEDIDOS Y RECORDATORIOS'
		self.notifyButton.grid(row=4,column=0,sticky=W,padx=2,pady=10)

		"""ATRIBUTOS DE BOTON OPCION BALANCE Y ESTADISTICAS"""
		if self.owner:
			self.stadisticsButton=ttk.Button(self.headerFrame,command=self.balanceSlot)
			self.stadisticsButton['text']='BALANCE MONETARIO'
			self.stadisticsButton.grid(row=5,column=0,sticky=W,padx=2,pady=10)

		"""ATRIBUTOS DE BOTON OPCION CAMBIO DE USUARIO"""
		self.switchButton = ttk.Button(self.headerFrame,command=self.switchSlot)
		self.switchButton['text']='CAMBIAR DE USUARIO'
		self.switchButton.grid(row=6,column=0,sticky=W,padx=2,pady=10)

		"""ATRIBUTOS DE BOTON OPCION SALIR"""
		self.exitButton=ttk.Button(self.headerFrame,command=self.exitSlot)
		self.exitButton['text']='SALIR'
		self.exitButton.grid(row=7,column=0,sticky=W,padx=2,pady=10)		

		"""FRAME """
		self.frame=LabelFrame(self.window)
		self.frame['text']='Bienvenidos a DelCassarApp'
		self.frame.grid(row = 1, column= 0, columnspan=3, pady=5,padx=10)							

	def headerDesing(self):
		self.headerFrame.grid(row = 0, column= 0, columnspan=20,sticky=W + E, pady=20)

		self.saleButton.grid(row=1,column=0,sticky=W,padx=2)

		self.buyButton.grid(row=1,column=1,sticky=W,padx=2)
		
		self.cashRegisterButton.grid(row=1,column=2,sticky=W,padx=2)

		self.notifyButton.grid(row=1,column=3,sticky=W,padx=2)

		if self.owner:			
			self.stadisticsButton.grid(row=1,column=4,sticky=W,padx=2)
		
		self.switchButton.grid(row=1,column=5,sticky=W,padx=2)	

		self.exitButton.grid(row=1,column=7,sticky=W,padx=2)

#------------------- SLOTS DE BOTONES ------------------------------------		
	def saleSlot(self):
		messagebox.showinfo(message="Mensaje", title="Título")
		self.headerDesing()	
		self.stopRunning()
		self.dictRunning['ventas'] = True
		self.ventas = OutFrame(self.frame,self.info_Container)		

	def buySlot(self):
		self.headerDesing()	
		self.stopRunning()
		self.dictRunning['compras'] = True
		self.compras = InFrame(self.frame,self.info_Container)

	def cashRegisterSlot(self):
		self.headerDesing()	
		self.stopRunning()
		self.dictRunning['cuadre']=True
		self.cash_Register=	cashRegister(self.frame,self.info_Container)

	def notifySlot(self):
		self.headerDesing()	
		self.stopRunning()
		self.dictRunning['notificaciones'] = True
		self.notify = Notify(self.frame,self.info_Container)

	def balanceSlot(self):
		self.headerDesing()	
		self.stopRunning()
		self.dictRunning['balance']=True
		self.dataStudy = dataStudy(self.frame,self.info_Container)	
		
	def switchSlot(self):
		print(messagebox.askretrycancel(message="¿Desea reintentar?", title="Título"))		

	def exitSlot(self):		
		#print(messagebox.askyesno(message="¿Desea continuar?", title="Título"))
		if messagebox.askokcancel(message="¿Desea continuar?", title="AVISO"):
			self.stopRunning()
			self.headerFrame.destroy()
			self.window.destroy()							
		#print(messagebox.askretrycancel(message="¿Desea reintentar?", title="Título"))	
				
	
	#AGREGAR LOS BOTONES FALTANTES	

	#!!!!!!!!!!!!!!IMCOPLETO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	def stopRunning(self):
		for i in self.dictRunning:
			if self.dictRunning[i]:
				if i == 'ventas':
					self.ventas.desaparecer()
					self.dictRunning['ventas']=False
				elif i == 'compras':
					self.compras.desaparecer()
					self.dictRunning['compras']=False
				elif i == 'cuadre':
					self.cash_Register.desaparecer()
					self.dictRunning['compras']=False
				elif i == 'notificaciones':
					self.notify.desaparecer()
					self.dictRunning['notificaciones']=False
				elif i == 'balance':
					self.dataStudy.desaparecer()
					self.dictRunning['balance']=False


			#~~~~~~~~~~~~~~~~~~~~~~!!!!!FRAME SALIDA DE CAPITAL!!!!!!~~~~~~~~~~~~~~~~~~~~~~#
		   #~~~~~~~~~~~~~~~~~~~~~~!!!!!DISPONIBLE PARA USUARIOS!!!!!!~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~
#Clase encargada de mostrar la funcion de ventas
	#Esta clase controla toda salida de productos
class OutFrame(Frame):
	def __init__(self,frame,info_Container):
		super(OutFrame, self).__init__()
		self.mainframe=frame
		Frame.__init__(self, self.mainframe)
		self.pack(fill='both', expand=True)

		self.typo = 1 #Tipo de Salida (1-> Venta, 2-> Fiado, 3-> Injustificado)
		#Bandera de permisos
		self.owner = True # True-> es propietario
		self.username = 'administrador'


		#Inicializando los datos	
		self.info_Container = info_Container
		self.productos = self.info_Container.getProducts()
	
		#self.mainframe=frame

		self.frameWidgets = []
		self.sellList = []

		self.saleWindowDesing()

	def getInfoContainer(self):
		return self.info_Container
	
	def saleWindowDesing(self):
		self.searchFrame()		
		self.saleFrame()
		self.saleInfoFrame()

#---------- ------ METODOS DE DISEÑO ------------------------#
	def searchFrame(self):
		##################  Frame de busqueda de productos  #######################
		self.frame=LabelFrame(self)
		self.frame['text'] = 'Busqueda de Productos'
		self.frame.grid(row = 0, column= 0, columnspan=1, pady=1,padx=10)			

		self.searchLabel=Label(self.frame)		
		self.searchLabel['text']='Nombre: '
		self.searchLabel.grid(row=1,column=0,padx=3)
		self.frameWidgets.append(self.searchLabel)


		self.searchName=Entry(self.frame,bg='white')
		self.searchName.focus()
		self.searchName.grid(row=1,column=1)
		self.frameWidgets.append(self.searchName)

		self.message = Label(self.frame,text="",fg = 'red')
		self.message.grid(row=2,column=0,columnspan=2,sticky=W + E)
		self.frameWidgets.append(self.message)

		self.searchButton=ttk.Button(self.frame,command=self.searchProduct)
		self.searchButton['text']='Buscar'
		self.searchButton.grid(row=1,column=2,sticky=W + E,columnspan=2,pady=1)
		self.frameWidgets.append(self.searchButton)

				
		self.searchTable=ttk.Treeview(self.frame,height=10,columns=4)
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

		for elem in self.productos:
			self.searchTable.insert("",10,text = elem.Codigo(),values=(elem.Nombre(),elem.Precio(),elem.Cantidad()))

		self.addProductButton=ttk.Button(self.frame,command=self.addSellProduct)
		self.addProductButton['text']='Añadir al Carrito'
		self.addProductButton.grid(row=5,column=0,sticky=W + E,columnspan=2,pady=10)
		self.frameWidgets.append(self.addProductButton)

	def saleFrame(self):	
		##################  Frame Carrito de Ventas  #############################
		self.frame2=LabelFrame(self)
		self.frame2['text']='Venta de Productos'
		self.frame2.grid(row = 0, column= 3,padx=4)

		#self.var=False
		#self.granel=ttk.Checkbutton(self.aux_window,variable=self.var,command=self.granel)
		#self.granel['text']='¿Se Vende al granel?'
		#self.granel.grid(row=3,column=0,pady=25)
		self.check_var1=IntVar()
		self.check_var1.set(1)
		self.check_var2=IntVar()
		self.check_var3=IntVar()
		self.sellConfigButton=ttk.Checkbutton(self.frame2,variable=self.check_var1,command=self.sellConfig)
		self.sellConfigButton['text']='VENTAS'
		self.sellConfigButton.grid(row=0,column=7,pady=1,padx=50)
		self.frameWidgets.append(self.sellConfigButton)

		self.orderConfigButton = ttk.Checkbutton(self.frame2,variable=self.check_var2,command=self.trustConfig)
		self.orderConfigButton['text']='FIADO'
		self.orderConfigButton.grid(row=1,column=7,pady=1,padx=55)
		self.frameWidgets.append(self.orderConfigButton)

		self.trustConfigButton=ttk.Checkbutton(self.frame2,variable=self.check_var3,command=self.noConfig)
		self.trustConfigButton['text'] = 'INJUSTIFICADO'
		self.trustConfigButton.grid(row=2,column=7,pady=1,padx=50)
		self.frameWidgets.append(self.trustConfigButton)

		self.sellLabel = Label(self.frame2)
		self.sellLabel['text']='Nombre del Cliente: '
		self.sellLabel.grid(row=1,column=0,pady=1)
		self.frameWidgets.append(self.sellLabel)

		self.sellName = Entry(self.frame2)
		self.sellName.grid(row=1,column=1,pady=1)
		self.frameWidgets.append(self.sellName)

		self.message2 = Label(self.frame2,text='',fg = 'red')
		self.message2.grid(row=2,column=0,columnspan=2,sticky=W + E)
		self.frameWidgets.append(self.message2)

		self.sellTable = ttk.Treeview(self.frame2,height=9,columns=3)
		self.sellTable.grid(row=3,column=0,columnspan=100,padx=1)
		self.sellTable['columns'] = ['Column 2','Column 3']
		self.sellTable.heading('#0',text='Codigo',anchor=CENTER)
		self.sellTable.heading('#1',text='Nombre',anchor=CENTER)
		self.sellTable.heading('#2',text='Precio',anchor=CENTER)

		self.frameWidgets.append(self.sellTable)

		self.deleteButton=ttk.Button(self.frame2, command=self.deleteSellProduct)
		self.deleteButton['text']='Eliminar del Carrito'
		self.deleteButton.grid(row=4,column=0,sticky=W + E,columnspan=2,pady=10)
		self.frameWidgets.append(self.deleteButton)

	def saleInfoFrame(self):	
		##################  Frame Datos de Venta  #############################
		self.frame3=LabelFrame(self)
		self.frame3['text']='DATOS DE VENTA'
		self.frame3.grid(row = 3, column= 0, columnspan=20,sticky=W + E,padx=10)

		self.sellButton=ttk.Button(self.frame3,command=self.saleComplete)
		self.sellButton.grid(row=2,column=2,padx=30)#,columnspan=100,sticky=W + E)
		self.sellButton['text']='VENDIDO'
		self.frameWidgets.append(self.sellButton)


		if self.owner:			

			self.vhistoryButton=ttk.Button(self.frame3,command=self.historySlot)
			self.vhistoryButton.grid(row=2,column=4,padx=10)
			self.vhistoryButton['text']='HISTORIAL DE VENTAS'
			self.frameWidgets.append(self.vhistoryButton)


		self.totalSoldLabel=Label(self.frame3)
		self.totalSoldLabel.grid(row=0,column=0,pady=10,padx=10)
		self.frameWidgets.append(self.totalSoldLabel)

		self.modeLabel=Label(self.frame3)
		self.modeLabel.grid(row=2,column=0,pady=10,padx=10)
		self.modeLabel['text']='Seleccione la forma de pago: '
		self.frameWidgets.append(self.modeLabel)

		listPay=['EFECTIVO','QR']
		self.menuPay = ttk.Combobox(self.frame3,values=listPay)
		self.menuPay.set('EFECTIVO')
		self.menuPay.config(width=20)
		self.menuPay.grid(row=2,column=1,pady=10)
		self.frameWidgets.append(self.menuPay)

#--------------- SLOTS DE BOTONES ------------------------------------

	#Slot del boton buscar productos
	def searchProduct(self):
		self.results=self.info_Container.searchData(self.searchName.get())	
		if len(self.results) == 0:
			self.message['text']='No se ha encontrado ningun producto.'	
		else:
			self.message['text']=''	
		records=self.searchTable.get_children()
		for i in records:
			self.searchTable.delete(i)
		for elem in self.results:
			self.searchTable.insert("",0,text = elem.Codigo(),values=(elem.Nombre(),elem.Precio()))
	
	#Slot del boton añadir productos al carrito
	def addSellProduct(self):
		chosen=self.searchTable.item(self.searchTable.selection())
		if chosen['text']  ==  '' :
			self.message['text'] = 'Por favor, seleccione un producto.'
		else:
			self.message['text'] = ''
			self.sellList.append(chosen)
			try:
				self.updateSellTable()
			except Exception as e:
				self.message['text']='Por favor, seleccione un producto.'

	#Slot del boton eliminar del carrito		
	def deleteSellProduct(self):
		chosen = self.sellTable.item(self.sellTable.selection())		
		self.sellList.remove(chosen)		
		try:
			self.updateSellTable()
		except Exception as e:
			self.message2['text']='Por favor, seleccione un producto.'

	#Slot del boton Vendido
	def saleComplete(self):
		#Se presiona el boton "VENDIDO"
		if self.sellList:			
			shape = self.menuPay.get()
			if not shape == '':
				saleValue = self.info_Container.addOut(self.sellList,self.typo,shape,self.username,self.username)  #Funcion Simplificada de Venta
				
				self.sellList.clear()
				self.updateSellTable()
				self.updateSearchTable()
			else:
				print("Datos No validos")		


	#INCOMPLETO# AGREGAR VENTAS POR DIA	
	def historySlot(self):
		self.historyState='v'		
		df_ventas=self.info_Container.getDfVentas()
		df_columns=self.info_Container.ventas_columns
		self.aux_window=Tk()
		#self.aux_window.protocol("WM_DELETE_WINDOW",self.closedWindow)
		
		self.auxWindowWidgets=[]

		self.textLabel=Label(self.aux_window)
		self.textLabel['text']='Seleccione una Fecha: '
		self.textLabel.grid(row=0,column=0,padx=5,pady=5)
		self.auxWindowWidgets.append(self.textLabel)

		listDate = self.info_Container.getWeekDays(6)
		#listDate.append("2020-08-01")
		self.dateOptions=ttk.Combobox(self.aux_window,values=listDate)
		self.dateOptions.grid(row=0,column=1,pady=5)
		self.dateOptions.config(width=20)
		self.auxWindowWidgets.append(self.dateOptions)

		self.vhistoryButton=ttk.Button(self.aux_window,command=self.vhistorySlot)
		self.vhistoryButton.grid(row=1,column=0,padx=10)
		self.vhistoryButton['text']='HISTORIAL DE VENTAS'
		self.auxWindowWidgets.append(self.vhistoryButton)

		self.dhistoryButton=ttk.Button(self.aux_window,command=self.dhistorySlot)
		self.dhistoryButton.grid(row=1,column=1,padx=10)
		self.dhistoryButton['text']='HISTORIAL DE DOMICILIOS'
		self.auxWindowWidgets.append(self.dhistoryButton)

		self.fhistoryButton=ttk.Button(self.aux_window,command=self.fhistorySlot)
		self.fhistoryButton.grid(row=1,column=2,padx=10)
		self.fhistoryButton['text']='HISTORIAL DE FIADOS'
		self.auxWindowWidgets.append(self.fhistoryButton)

		self.vhistoryTable=ttk.Treeview(self.aux_window,height=20,columns=6)
		self.vhistoryTable.grid(row=2,column=0,columnspan=10,padx=1)
		self.vhistoryTable['columns']=['Column 2','Column 3','Column 4','Column 5','Column 6']
		self.vhistoryTable.column('#0',width=300,anchor=CENTER)
		self.vhistoryTable.heading('#0',text='ID VENTA')
		self.vhistoryTable.column('#1',width=80,anchor=CENTER)
		self.vhistoryTable.heading('#1',text='CODIGO')
		self.vhistoryTable.column('#2',width=200,anchor=CENTER)
		self.vhistoryTable.heading('#2',text='DESCRIPCION')
		self.vhistoryTable.column('#3',width=200,anchor=CENTER)
		self.vhistoryTable.heading('#3',text='PRECIO')
		self.vhistoryTable.column('#4',width=200,anchor=CENTER)
		self.vhistoryTable.heading('#4',text='NOMBRE VENDEDOR')
		self.vhistoryTable.column('#5',width=200,anchor=CENTER)
		self.vhistoryTable.heading('#5',text='NOMBRE COMPRADOR')

		listValues=[]
		for row in df_ventas.iterrows():
			for elem in row:
				if type(elem) != int:
					listValues.clear()		
					for column in df_columns:
						if column == 'ID VENTA':
							first_elem=elem[column]
						else:
							listValues.append(elem[column])	
					self.vhistoryTable.insert("",0,text = first_elem,values=(listValues))	

		self.updateButton=ttk.Button(self.aux_window,command=self.updateTable)
		self.updateButton['text']='ACTUALIZAR'
		self.updateButton.grid(row=3,column=0,pady=10,columnspan=400)
		self.auxWindowWidgets.append(self.updateButton)

		self.returnButton=ttk.Button(self.aux_window,command=self.returnProduct)
		self.returnButton.grid(row=3,column=1,pady=10,columnspan=400)
		self.returnButton['text']='DEVOLUCIONES'
		self.auxWindowWidgets.append(self.returnButton)

		self.doneButton=ttk.Button(self.aux_window,command=self.doneSlot)
		self.doneButton['text']='SALIR'
		self.doneButton.grid(row=4,column=0,pady=10,padx=10,columnspan=100,sticky=W + E)
		self.auxWindowWidgets.append(self.doneButton)
		
	def vhistorySlot(self):
		self.historyState='v'
		self.deleteItemsTable(self.vhistoryTable)
		self.vhistoryTable.config(columns=6)
		self.vhistoryTable['columns']=['Column 2','Column 3','Column 4','Column 5','Column 6']
		self.vhistoryTable.column('#0',width=300,anchor=CENTER)
		self.vhistoryTable.heading('#0',text='ID VENTA')
		self.vhistoryTable.column('#1',width=80,anchor=CENTER)
		self.vhistoryTable.heading('#1',text='CODIGO')
		self.vhistoryTable.column('#2',width=200,anchor=CENTER)
		self.vhistoryTable.heading('#2',text='DESCRIPCION')
		self.vhistoryTable.column('#3',width=200,anchor=CENTER)
		self.vhistoryTable.heading('#3',text='PRECIO')
		self.vhistoryTable.column('#4',width=200,anchor=CENTER)
		self.vhistoryTable.heading('#4',text='NOMBRE VENDEDOR')
		self.vhistoryTable.column('#5',width=200,anchor=CENTER)
		self.vhistoryTable.heading('#5',text='NOMBRE COMPRADOR')	

	def dhistorySlot(self):
		self.historyState='d'
		self.deleteItemsTable(self.vhistoryTable)
		df_columns=self.info_Container.delivery_columns

		listColumns=[]
		for i in range(len(df_columns)+1):
			if i>1:
				listColumns.append('Columnn '+str(i))

		self.vhistoryTable.config(columns=len(df_columns)+1)
		self.vhistoryTable['columns']=listColumns
		self.vhistoryTable.column('#0',width=100,anchor=CENTER)
		self.vhistoryTable.heading('#0',text=df_columns[0])
		self.vhistoryTable.column('#1',width=80,anchor=CENTER)
		self.vhistoryTable.heading('#1',text=df_columns[1])
		self.vhistoryTable.column('#2',width=100,anchor=CENTER)
		self.vhistoryTable.heading('#2',text=df_columns[2])
		self.vhistoryTable.column('#3',width=100,anchor=CENTER)
		self.vhistoryTable.heading('#3',text=df_columns[3])
		self.vhistoryTable.column('#4',width=100,anchor=CENTER)
		self.vhistoryTable.heading('#4',text=df_columns[4])
		self.vhistoryTable.column('#5',width=100,anchor=CENTER)
		self.vhistoryTable.heading('#5',text=df_columns[5])
		self.vhistoryTable.column('#6',width=100,anchor=CENTER)
		self.vhistoryTable.heading('#6',text=df_columns[6])

	

	def fhistorySlot(self):
		self.historyState='t'
		self.deleteItemsTable(self.vhistoryTable)
		df_columns=self.info_Container.trust_columns

		listColumns=[]
		for i in range(len(df_columns)+1):
			if i>1:
				listColumns.append('Columnn '+str(i))

		self.vhistoryTable.config(columns=len(df_columns)+1)
		self.vhistoryTable['columns']=listColumns
		self.vhistoryTable.column('#0',width=300,anchor=CENTER)
		self.vhistoryTable.heading('#0',text=df_columns[0])
		self.vhistoryTable.column('#1',width=80,anchor=CENTER)
		self.vhistoryTable.heading('#1',text=df_columns[1])
		self.vhistoryTable.column('#2',width=200,anchor=CENTER)
		self.vhistoryTable.heading('#2',text=df_columns[2])
		self.vhistoryTable.column('#3',width=200,anchor=CENTER)
		self.vhistoryTable.heading('#3',text=df_columns[3])
		self.vhistoryTable.column('#4',width=200,anchor=CENTER)
		self.vhistoryTable.heading('#4',text=df_columns[4])		


	#SLOTS#VENTANTAS$EMERGENTES
	def updateTable(self):
		self.deleteItemsTable(self.vhistoryTable)
		#Obtener Datos por Fecha
		date=self.dateOptions.get()
		#######
		if self.historyState == 'v':
			dfList=self.info_Container.searchSaleByDate(date)
			for vector in dfList:
				self.vhistoryTable.insert("",0,text = vector[0],values=vector[1:])

	def updateHistoryTable(self,dataframe):			
		self.deleteItemsTable(self.vhistoryTable)
		listDF=self.info_Container.df2List(dataframe)		
		for vector in listDF:
			self.vhistoryTable.insert("",0,text = vector[0],values=vector[1:])

	def returnProduct(self):
		chosen=self.vhistoryTable.item(self.vhistoryTable.selection())
		if self.info_Container.validarDatos(chosen):				
			try:
				df=self.info_Container.returnItemSold(chosen)
				self.updateHistoryTable(df)
			except Exception as e:
				print("No se pudo actualizar la tabla")

		else:
			print("Elemento Vacio")
			print("No se pudo hacer la Devolucion")	

	def doneSlot(self):		
		for i in self.auxWindowWidgets:
			i.destroy()
		self.aux_window.destroy()


	#SLOTS#CHECKBOX#	
		
	def sellConfig(self):
		self.typo = 1
		self.check_var2.set(0)
		self.check_var3.set(0)
		print('venta: ',self.check_var1.get())
		self.setConfig()

	def	trustConfig(self):
		self.typo = 2
		self.check_var1.set(0)
		self.check_var3.set(0)
		print('Fiado: ',self.check_var2.get())
		self.setConfig()

	def	noConfig(self):
		self.typo = 3
		self.check_var1.set(0)
		self.check_var2.set(0)
		print('Injustificado: ',self.check_var3.get())
		self.setConfig()	

#---------------------- FUNCIONES ASISTENTES--------------------------
	def setConfig(self):
		if self.check_var1.get() == 1:
			self.frame2['text']='Venta de Productos'
			self.sellButton['text']='VENDIDO'	
		elif self.check_var2.get() == 1:
			self.frame2['text']='Agregar Domicilio'
			self.sellButton['text']='AGREGAR DOMICILIO'
		elif self.check_var3.get() == 1:
			self.frame2['text']='Fiado de Productos'
			self.sellButton['text']='AGREGAR FIADO'
	
	


	def itemTable2itemProduct(self):
		listSoldProduct=[]	#Para guardar en el archivo de ventas	
		for item in self.sellList:
			for product in self.info_Container.getProducts():
				if int(item['text']) == product.Codigo():
					listSoldProduct.append(product)
					print("Producto Vendido: {}".format(item['values'][0]))
		return listSoldProduct


	def updateSellTable(self):
		saleValue=self.info_Container.addingSale(self.sellList)		
		self.totalSoldLabel['text']='Valor nuevo Venta: {}'.format(saleValue)						
		records=self.sellTable.get_children()
		for i in records:
				self.sellTable.delete(i)
		for elem in self.sellList:
			self.sellTable.insert("",0,text = elem['text'],values=elem['values'])

	def updateSearchTable(self):
		records=self.searchTable.get_children()
		for i in records:
				self.searchTable.delete(i)
		for elem in self.info_Container.getProducts():
			self.searchTable.insert("",10,text = elem.Codigo(),values=(elem.Nombre(),elem.Precio(),elem.Cantidad()))		
	
	def deleteItemsTable(self,tableWidget):
		records=tableWidget.get_children()
		for i in records:
				tableWidget.delete(i)	

	def deleteFrameWidgets(self):	
		for widget in self.frameWidgets:
			widget.grid_remove()
			widget.destroy()
		self.frameWidgets.clear()
		self.frame.destroy()					
		self.frame2.destroy()
		self.frame3.destroy()

	def desaparecer(self):
		self.deleteFrameWidgets()
		del self.frameWidgets
		del self.info_Container
		self.destroy()	

#~~~~~~~~~~~~~~~~~~~~~~----------------FIN DE LA CLASE VENTANA_VENTAS ---------------------------------·~#		




				#~~~~~~~~~~~~~~~~~~~~~~!!!!!FRAME DE ENTRADA DE CAPITAL!!!!!!~~~~~~~~~~~~~~~~~~~~~~#
			      #~~~~~~~~~~~~~~~~~~~~~~!!!!!DISPONIBLE PARA USUARIOS!!!!!!~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~				
#Clase encargada de mostrar la funcion de compras
	#Esta clase controla toda entrada de productos
class InFrame(Frame):
	def __init__(self, frame,info_Container):
		super(InFrame, self).__init__()		
		self.mainframe=frame
		Frame.__init__(self, self.mainframe)
		self.pack(fill='both', expand=True)

		#Bandera de permisos
		self.owner = True # True-> es propietario
		self.username = 'administrador'

		self.info_Container = info_Container

		self.frameWidgets=[]
		self.buyList= []
		self.buyData = []
		self.buyCont = 0
		self.list_new_products=[]
		self.username='administrador'

		self.searchFrame()
		self.buyTableFrame()
		self.boughtDataFrame()
	def searchFrame(self):
		##################  Frame de busqueda de productos  #######################
		self.frame=LabelFrame(self)
		self.frame['text']='Busqueda de Productos'
		self.frame.grid(row = 0, column= 0, columnspan=1, padx=10)

		self.searchLabel=Label(self.frame)		
		self.searchLabel['text']='Nombre: '
		self.searchLabel.grid(row=1,column=0,padx=3)
		self.frameWidgets.append(self.searchLabel)


		self.searchName=Entry(self.frame,bg='white')
		self.searchName.focus()
		self.searchName.grid(row=1,column=1)
		self.frameWidgets.append(self.searchName)

		self.message=Label(self.frame,text="",fg = 'red')
		self.message.grid(row=2,column=0,columnspan=2,sticky=W + E)
		self.frameWidgets.append(self.message)

		self.searchButton=ttk.Button(self.frame,command=self.searchProduct)
		self.searchButton['text']='Buscar'
		self.searchButton.grid(row=1,column=3,sticky=W + E,columnspan=2,pady=1)
		self.frameWidgets.append(self.searchButton)
				
		self.searchTable=ttk.Treeview(self.frame,height=10,columns=4)
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

		self.updateSearchTable()		

		self.addProductButton=ttk.Button(self.frame,command=self.addBuyProduct)
		self.addProductButton['text']='Añadir al Carrito de Compras'
		self.addProductButton.grid(row=7,column=0 ,pady=5,padx=5)
		self.frameWidgets.append(self.addProductButton)

		self.addNewButton=ttk.Button(self.frame,command=self.addNewProductSlot)
		self.addNewButton['text']='Añadir Producto Nuevo'
		self.addNewButton.grid(row=7,column=3,pady=5,padx=5)
		self.frameWidgets.append(self.addNewButton)
	def buyTableFrame(self):	
		##################  Frame Carrito de Compras  #############################
		self.frame2=LabelFrame(self)
		self.frame2['text']='Compra de Productos'
		self.frame2.grid(row = 0, column= 3, columnspan=10,padx=4)

		self.buyLabel=Label(self.frame2)
		self.buyLabel['text']='Nombre del Proveedor: '
		self.buyLabel.grid(row=1,column=0,pady=10)
		self.frameWidgets.append(self.buyLabel)

		lisProveedores = self.info_Container.getProvidersNames()
		self.menuProveedores = ttk.Combobox(self.frame2,values=lisProveedores)
		self.menuProveedores.config(width=20)
		self.menuProveedores.grid(row=1,column=1,pady=10)
		self.frameWidgets.append(self.menuProveedores)

		if self.owner:
			self.addProviderButton=ttk.Button(self.frame2,command=self.addNewProvider)
			self.addProviderButton.grid(row=1,column=2,padx=100)
			self.addProviderButton['text']='Añadir Proveedor Nuevo'
			self.frameWidgets.append(self.addProviderButton)	

		self.message2=Label(self.frame2,text='',fg = 'red')
		self.message2.grid(row=2,column=0,columnspan=2,sticky=W + E)
		self.frameWidgets.append(self.message2)

		self.buyTable=ttk.Treeview(self.frame2,height=9,columns=3)
		self.buyTable.grid(row=3,column=0,columnspan=100,padx=10)
		self.buyTable['columns']=['Column 2','Column 3','Column 4']
		self.buyTable.column('#0',width=70,anchor=CENTER)
		self.buyTable.heading('#0',text='Codigo')
		self.buyTable.column('#1',width=350,anchor=CENTER)
		self.buyTable.heading('#1',text='Nombre')
		self.buyTable.column('#2',width=100,anchor=CENTER)
		self.buyTable.heading('#2',text='Precio')
		self.buyTable.column('#3',width=100,anchor=CENTER)
		self.buyTable.heading('#3',text='Cantidad')
		self.frameWidgets.append(self.buyTable)

		self.deleteButton=ttk.Button(self.frame2, command=self.deleteBuyProduct)
		self.deleteButton['text']='Eliminar del Carrito'
		self.deleteButton.grid(row=4,column=0,sticky=W + E,columnspan=2,pady=10)
		self.frameWidgets.append(self.deleteButton)	

	def boughtDataFrame(self):
		##################  Frame Datos de Venta  #############################
		self.frame3 = LabelFrame(self)
		self.frame3['text'] = 'DATOS DE COMPRA'
		self.frame3.grid(row = 3, column= 0, columnspan=20,sticky=W + E,padx=10)

		self.sellButton = ttk.Button(self.frame3,command=self.buyComplete)
		self.sellButton.grid(row=0,column=0,columnspan=100,padx=10)
		self.sellButton['text']='AGREGAR PEDIDO'
		self.frameWidgets.append(self.sellButton)
		
		self.planButton = ttk.Button(self.frame3,command = self.planearProveedor)
		self.planButton.grid(row=1,column=1,columnspan=100,padx=10)
		self.planButton['text'] = 'PLANEAR PROVEEDOR'
		self.frameWidgets.append(self.planButton)

		if self.owner:
			self.bHistory = ttk.Button(self.frame3,command=self.bHistorySlot)
			self.bHistory.grid(row=2,column=2,padx=110,pady=10)
			self.bHistory['text'] = 'HISTORIAL DE COMPRAS'
			self.frameWidgets.append(self.bHistory)			


		self.totalSoldLabel = Label(self.frame3)
		self.totalSoldLabel.grid(row=0,column=0,pady=10,padx=10)
		self.frameWidgets.append(self.totalSoldLabel)	

#SLOTS DE BOTONES DEL FRAME PRINCIPAL
	def searchProduct(self):
		self.results=self.info_Container.searchData(self.searchName.get())	
		if len(self.results) == 0:
			self.message['text']='No se ha encontrado ningun producto.'	
		else:
			self.message['text']=''	
		records=self.searchTable.get_children()
		for i in records:
			self.searchTable.delete(i)
		for elem in self.results:
			self.searchTable.insert("",0,text = elem.Codigo(),values=(elem.Nombre(),elem.Precio(),elem.Cantidad()))

	def addBuyProduct(self):
		chosen = self.searchTable.selection()
		if chosen:
			print("Datos Validos ",chosen,type(chosen))
			self.aux_window = Tk()
			self.aux_window.protocol("WM_DELETE_WINDOW",self.closedWindow)
			
			self.newFlag=False
			self.auxWindowWidgets=[]

			self.messageLabel = Label(self.aux_window)
			self.messageLabel['text']=''
			self.messageLabel.grid(row=1,column=0,pady=25)
			self.auxWindowWidgets.append(self.messageLabel)

			###
			self.priceLabel=Label(self.aux_window)
			self.priceLabel['text']='PRECIO: '
			self.priceLabel.grid(row=2,column=0,pady=25)
			self.auxWindowWidgets.append(self.priceLabel)
			
			self.priceEntry=Entry(self.aux_window)
			self.priceEntry.grid(row=2,column=1,pady=25)
			self.auxWindowWidgets.append(self.priceEntry)
			
			self.var1 = BooleanVar()
			self.iva = ttk.Checkbutton(self.aux_window,variable=self.var1,command=self.iva)
			self.iva['text']='IVA INCLUIDO: '
			self.iva.grid(row=3,column=0,pady=15)
			self.auxWindowWidgets.append(self.iva)

			
			###
			self.quantityLabel=Label(self.aux_window)
			self.quantityLabel['text']='CANTIDAD: '
			self.quantityLabel.grid(row=4,column=0,pady=25)
			self.auxWindowWidgets.append(self.quantityLabel)

			self.quantityEntry=Entry(self.aux_window)
			self.quantityEntry.grid(row=4,column=1,pady=25)
			self.auxWindowWidgets.append(self.quantityEntry)
			###
			
			self.var = BooleanVar()
			self.granel = ttk.Checkbutton(self.aux_window,variable=self.var,command=self.granel)
			self.granel['text']='GRANELADO: '
			self.granel.grid(row=5,column=0,pady=25)
			self.auxWindowWidgets.append(self.granel)
			
			self.var2 = BooleanVar()
			self.cambio = ttk.Checkbutton(self.aux_window,variable=self.var2,command=self.cambio)
			self.cambio['text']='CAMBIO: '
			self.cambio.grid(row=6,column=0,pady=25)
			self.auxWindowWidgets.append(self.cambio)		

			self.addExisting=ttk.Button(self.aux_window,command=self.addExistingProduct)
			self.addExisting['text']="AGREGAR"
			self.addExisting.grid(row=7,column=0)
			self.auxWindowWidgets.append(self.addExisting)

			self.aux_window.mainloop()
		else:
			pass

	def addNewProvider(self):
		self.aux_window=Tk()
		#self.aux_window.protocol("WM_DELETE_WINDOW",self.closedWindow)
		
		self.auxWindowWidgets=[]

		self.messageNP=Label(self.aux_window,text="",fg = 'red')
		self.messageNP.grid(row=0,column=0,columnspan=2,sticky=W + E)
		self.auxWindowWidgets.append(self.messageNP)

		self.textLabel=Label(self.aux_window)
		self.textLabel['text']='INGRESE EL NOMBRE: '
		self.textLabel.grid(row=1,column=0,padx=5,pady=5)
		self.auxWindowWidgets.append(self.textLabel)

		self.entryName=ttk.Entry(self.aux_window)
		self.entryName.grid(row=1,column=1)
		self.auxWindowWidgets.append(self.entryName)

		self.textLabel=Label(self.aux_window)
		self.textLabel['text']='INGRESE EL NIT: '
		self.textLabel.grid(row=2,column=0,padx=5,pady=5)
		self.auxWindowWidgets.append(self.textLabel)

		self.entryNit=ttk.Entry(self.aux_window)
		self.entryNit.grid(row=2,column=1)
		self.auxWindowWidgets.append(self.entryNit)

		self.textLabel=Label(self.aux_window)
		self.textLabel['text']='INGRESE EL HORARIO(L-M-W-J-V-S-D): '
		self.textLabel.grid(row=3,column=0,padx=5,pady=5)
		self.auxWindowWidgets.append(self.textLabel)

		self.entrySchedule=ttk.Entry(self.aux_window)
		self.entrySchedule.grid(row=3,column=1)
		self.auxWindowWidgets.append(self.entrySchedule)

		self.textLabel=Label(self.aux_window)
		self.textLabel['text']='INGRESE EL TELEFONO: '
		self.textLabel.grid(row=4,column=0,padx=5,pady=5)
		self.auxWindowWidgets.append(self.textLabel)

		self.entryTel=ttk.Entry(self.aux_window)
		self.entryTel.grid(row=4,column=1)
		self.auxWindowWidgets.append(self.entryTel)

		self.addNewProviderButton=ttk.Button(self.aux_window,command=self.addNewProvider2Info)
		self.addNewProviderButton['text']='Agregar Nuevo Proveedor'
		self.addNewProviderButton.grid(row=5,column=0,sticky=W + E,columnspan=100)
		self.auxWindowWidgets.append(self.addNewProviderButton)

	def bHistorySlot(self):
		df_columns=self.info_Container.compras_columns
		self.aux_window=Tk()
		#self.aux_window.protocol("WM_DELETE_WINDOW",self.closedWindow)
		
		self.auxWindowWidgets=[]

		self.textLabel=Label(self.aux_window)
		self.textLabel['text']='Seleccione una Fecha: '
		self.textLabel.grid(row=0,column=0,padx=5,pady=5)
		self.auxWindowWidgets.append(self.textLabel)

		listDate = self.info_Container.getWeekDays(6)
		self.dateOptions=ttk.Combobox(self.aux_window,values=listDate)
		self.dateOptions.grid(row=0,column=1,pady=5)
		self.dateOptions.config(width=20)
		self.auxWindowWidgets.append(self.dateOptions)

		listColumns=[]
		for i in range(len(df_columns)+1):
			if i>1:
				listColumns.append('Columnn '+str(i))

		self.dhistoryTable=ttk.Treeview(self.aux_window,height=20,columns=len(df_columns)+1)
		self.dhistoryTable.grid(row=1,column=0,columnspan=10,padx=1)
		self.dhistoryTable['columns']=listColumns
		self.dhistoryTable.column('#0',width=300,anchor=CENTER)
		self.dhistoryTable.heading('#0',text=df_columns[0])
		self.dhistoryTable.column('#1',width=80,anchor=CENTER)
		self.dhistoryTable.heading('#1',text=df_columns[1])
		self.dhistoryTable.column('#2',width=200,anchor=CENTER)
		self.dhistoryTable.heading('#2',text=df_columns[2])
		self.dhistoryTable.column('#3',width=200,anchor=CENTER)
		self.dhistoryTable.heading('#3',text=df_columns[3])
		self.dhistoryTable.column('#4',width=200,anchor=CENTER)
		self.dhistoryTable.heading('#4',text=df_columns[4])
		self.dhistoryTable.column('#5',width=200,anchor=CENTER)
		self.dhistoryTable.heading('#5',text=df_columns[5])
		self.dhistoryTable.column('#6',width=200,anchor=CENTER)
		self.dhistoryTable.heading('#6',text=df_columns[6])
		self.auxWindowWidgets.append(self.dhistoryTable)


		self.doneButton=ttk.Button(self.aux_window,command=self.doneSlot)
		self.doneButton['text']='HECHO'
		self.doneButton.grid(row=2,column=0,sticky=W + E,columnspan=100)
		self.auxWindowWidgets.append(self.doneButton)		

	#Slot de boton agregar producto nuevo que genera una nueva ventana	
	def addNewProductSlot(self):

		self.newFlag=True
		self.aux_window=Tk()
		self.aux_window.title('Agregar Producto Nuevo')	

		self.auxWindowWidgets=[]

		self.messageLabel = Label(self.aux_window)
		self.messageLabel['text']='Por favor, llene cada item'
		self.messageLabel.grid(row=0,column=0)
		self.auxWindowWidgets.append(self.messageLabel)

		self.codeLabel = Label(self.aux_window)
		self.codeLabel['text']='Escriba el Codigo del producto'
		self.codeLabel.grid(row=1,column=0)
		self.auxWindowWidgets.append(self.codeLabel)

		self.codeEntry = Entry(self.aux_window)
		self.codeEntry.grid(row=1,column=1,pady=25)
		self.auxWindowWidgets.append(self.codeEntry)

		self.nameLabel = Label(self.aux_window)
		self.nameLabel['text']='Escriba la Descripcion del producto'
		self.nameLabel.grid(row=2,column=0,pady=25)
		self.auxWindowWidgets.append(self.nameLabel)

		self.nameEntry = Entry(self.aux_window)
		self.nameEntry.grid(row=2,column=1,pady=25)		
		self.auxWindowWidgets.append(self.nameEntry)

		self.priceLabel = Label(self.aux_window)
		self.priceLabel['text']='Escriba el precio con Iva del producto'
		self.priceLabel.grid(row=3,column=0,pady=25)
		self.auxWindowWidgets.append(self.priceLabel)
		
		self.var1 = BooleanVar()
		self.iva = ttk.Checkbutton(self.aux_window,variable=self.var1,command=self.iva)
		self.iva['text']='IVA INCLUIDO: '
		self.iva.grid(row=4,column=0,pady=10)
		self.auxWindowWidgets.append(self.iva)

		self.priceEntry=Entry(self.aux_window)
		self.priceEntry.grid(row=3,column=1,pady=25)
		self.auxWindowWidgets.append(self.priceEntry)

		self.quantityLabel=Label(self.aux_window)
		self.quantityLabel['text']='Escriba la cantidad del producto'
		self.quantityLabel.grid(row=5,column=0,pady=25)
		self.auxWindowWidgets.append(self.quantityLabel)

		self.quantityEntry=Entry(self.aux_window)
		self.quantityEntry.grid(row=5,column=1,pady=25)
		self.auxWindowWidgets.append(self.quantityEntry)

		self.var = BooleanVar()
		self.granel = ttk.Checkbutton(self.aux_window,variable=self.var,command=self.granel)
		self.granel['text']='¿Se Vende al granel?'
		self.granel.grid(row=6,column=0,pady=25)
		self.auxWindowWidgets.append(self.granel)
		
		self.valid = ttk.Button(self.aux_window,command=self.addNewProduct)
		self.valid['text']='Agregar Producto'
		self.valid.config(width=30)
		self.valid.grid(row=7,column=0,pady=25)		
		self.auxWindowWidgets.append(self.granel)

		self.aux_window.mainloop()

	def deleteBuyProduct(self):
		chosen=self.buyTable.item(self.buyTable.selection())
		print("ELemento a eliminar ",chosen)
		#chosen=self.buyTable.selection()		
		self.buyList.remove(chosen)		
		try:
			self.updateBuyTable()
		except Exception as e:
			self.message2['text']='Por favor, seleccione un producto.'


	#Slot del boton Agregar pedido o comprado
	def buyComplete(self):
		#Se presiona el boton "Comprado"
		if self.buyData:		
			provider = self.menuProveedores.get()

			if self.validarDatos([provider]):
				self.message2['text'] = ''
				if self.newFlag:
					self.info_Container.newProducts(self.list_new_products)
				

				#INCOMPLETO:
				     #FALTA GENERAR LA SUMA DE LOS NUEVOS PRODUCTOS
				purchaseValue = self.info_Container.addBuy(self.buyList,self.list_new_products,provider,self.username)
				self.info_Container.addIn(self.buyData,provider,self.username)
				self.totalSoldLabel['text']='Valor nuevo Compra: {}'.format(purchaseValue)
				self.buyList.clear()
				self.buyData.clear()
				self.buyCont = 0

				self.updateBuyTable(self.buyData)
				self.updateSearchTable()
			else:
				self.message2['text']='SELECCIONE PROVEEDOR O CREE UNO NUEVO.'
			
	def planearProveedor(self):
		self.info_Container.addIn(self.buyData,"Cualquiera",self.username)


#SLOTS DE BOTONES DEL VENTANAS SECUNDARIAS
	def addNewProduct(self):
		listData = []
		listData.append(self.codeEntry.get())#[0] Codigo
		listData.append(self.nameEntry.get())#[1] Descripcion
		listData.append(False) #[2] Cambio/Compra - True/False
		listData.append(self.var.get())#[3]	Granel
		listData.append(float(self.quantityEntry.get()))#[4] Cantidad

		if self.var1.get():			
			listData.append(int(self.priceEntry.get()))#[5] Precio
		else:
			listData.append(int(self.priceEntry.get())*self.info_Container.getIva())#[5] Precio	

		if self.validarDatos(listData):
			self.message2['text']= ''
			self.setNewProduct(listData)			
			#self.deleteWidgets(self.auxWindowWidgets)
			self.aux_window.destroy()
		else:
			self.messageLabel['text']='Datos Incompletos.'		


	def addExistingProduct(self):
		auxList = []
		dataList = []
		newQuantity = 0
		newPrice = 0
		newQuantity = self.quantityEntry.get()
		if self.var1.get():
			newPrice = int(self.priceEntry.get())#[5] Precio
		else:
			newPrice = int(self.priceEntry.get())*self.info_Container.getIva()#[5] Precio
		
		chosen = self.searchTable.selection()
		print("NUEVA CANTIDAD {}\nNUEVO PRECIO {}\n".format(newQuantity,newPrice))
		if self.validarDatos([newQuantity,newPrice]):
			
			self.deleteWidgets(self.auxWindowWidgets)
			self.aux_window.destroy()

			chosen = self.searchTable.item(chosen)	
			
			dataList.append(chosen['text']) #Codigo
			dataList.append(chosen['values'][0])#Decripcion
			dataList.append(self.var2.get())#Cambio/Compra
			dataList.append(self.var.get())#Granel			
			dataList.append(float(newQuantity))#Cantidad
			dataList.append(int(newPrice)) #Precio
			
			chosen['values'][1] = int(newPrice)
			chosen['values'][2] = float(newQuantity)

			self.buyList.append(chosen)
			self.buyData.append(dataList)
			self.buyCont += 1
				
			try:				
				self.updateBuyTable(self.buyData)
				self.message['text'] = ''
			except Exception as e:
				print("ERROR al actualizar la tabla del carrito de compras \n",e)
		else:
			self.messageLabel['text']='Por favor, seleccione un producto.'

	def addNewProvider2Info(self):
		listData=[]
		listData.append(self.entryName.get())
		listData.append(self.entryNit.get())
		listData.append(self.entrySchedule.get())
		listData.append(self.entryTel.get())
		if self.info_Container.validarDatos(listData):
			self.messageNP['text']=''
			self.doneSlot()
		else:
			self.messageNP['text']='Datos NO Validos.'						

	#INCOMPLETO			
	def closedWindow(self):
		#Preguntar al usuario si esta de acuerdo con cerrar
		self.aux_window.destroy()		
		print('ventana cerrdada')

	#SLOTS#VENTANTAS$EMERGENTES
	def doneSlot(self):
		for i in self.auxWindowWidgets:
			i.destroy()
		self.aux_window.destroy()		

#---------------------- FUNCIONES ASISTENTES--------------------------
	
	#!!!!!!!!!!!!!!IMCOPLETO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	def itemTable2itemProduct(self):
		listSoldProduct=[]	#Para guardar en el archivo de ventas	
		for item in self.buyList:
			for product in self.info_Container.getProducts():
				if int(item['text']) == product.Codigo():
					listSoldProduct.append(product)
					print("Producto Vendido: {}".format(item['values'][0]))
		return listSoldProduct

	def granel(self):
		self.var.set(not self.var.get())		
		if self.var.get():
			print("Se vende al granel")
		else:
			print("NO se vende al granel")	
			
	def iva(self):
		self.var1.set(not self.var1.get())		
		if self.var1.get():
			print("Precio con IVA")
		else:
			print("Precio sin IVA")	
			
	def cambio(self):
		self.var2.set(not self.var2.get())		
		if self.var2.get():
			print("CAMBIO")				
		else:
			print("COMPRA")	

	def updateSearchTable(self):
		records = self.searchTable.get_children()
		for i in records:
				self.searchTable.delete(i)
		for elem in self.info_Container.getProducts():
			self.searchTable.insert("",10,text = elem.Codigo(),values=(elem.Nombre(),elem.Precio(),elem.Cantidad()))		

	#!!!!!!!!!!!!!!IMCOPLETO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!	
	def updateBuyTable(self):
		#saleValue=self.info_Container.addingBuy(self.buyList)
		#self.totalBoughtLabel['text']='Valor nuevo Venta: {}'.format(saleValue)						
		records = self.buyTable.get_children()
		for i in records:
				self.buyTable.delete(i)
		for elem in self.buyList:
			self.buyTable.insert("",0,text = elem['text'],values=elem['values'])

	def updateBuyTable(self,buyList):
		records = self.buyTable.get_children()
		for i in records:
				self.buyTable.delete(i)
		for elem in buyList:
			self.buyTable.insert("",0,text = elem[0],values= [elem[1],elem[5],elem[4]])		

	#!!!!!!!!!!!!!!IMCOPLETO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	def setNewProduct(self,listData):
		#Agregar nuevos productos a la lista de productos
		self.list_new_products.append(listData)
		self.buyData.append(listData)
		self.buyTable.insert("",10,text = listData[0],values=(listData[1],listData[5],listData[4]))		


	def validarDatos(self,listData):
		valid=True
		cont=0
		for i in listData:
			cont+=1
			if i == '':
				valid=False
			elif i == ():
				valid=False		
					
		return valid

#FUNCIONES DE ELIMINACION Y DESTRUCCION DE OBJETOS		
	def deleteFrameWidgets(self):	
		for widget in self.frameWidgets:
			widget.grid_remove()
			widget.destroy()
		self.frameWidgets.clear()
		self.frame.destroy()					
		self.frame2.destroy()
		self.frame3.destroy()

	def deleteWidgets(self,frameWidgets):
		for widget in frameWidgets:
			widget.grid_remove()
			widget.destroy()	
		return frameWidgets.clear()

	def desaparecer(self):
		self.deleteFrameWidgets()
		del self.info_Container
		self.destroy()


#~~~~~~~~~~~~~~~~~~~~~~----------------FIN DE LA CLASE VENTANA_COMPRAS ---------------------------------·~#	


				#~~~~~~~~~~~~~~~~~~~~~~!!!!!FRAME CUADRE DIARIO!!!!!!~~~~~~~~~~~~~~~~~~~~~~#
			 #~~~~~~~~~~~~~~~~~~~~~~!!!!!DISPONIBLE PARA USUARIOS!!!!!!~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~				
#Clase encargada de registrar el cuadre diario
class cashRegister(Frame):
	def __init__(self, frame,info_Container):
		super(cashRegister, self).__init__()
		self.mainframe=frame
		Frame.__init__(self, self.mainframe)
		self.pack(fill='both', expand=True)

		self.info_Container=info_Container
		self.date=self.info_Container.getToday()

		self.frameWidgets=[]

		self.infoFrame()
		self.moneyFrame()
		self.graphicsFrame()
		self.registerFrame()

	def infoFrame(self):
		##################  FRAME CUADRE DIARIO  #######################

		#PENDIENTE:
		self.infoList=[30,46,76,23,33]

		self.frame=LabelFrame(self)
		self.frame['text']='CUADRE DIARIO'
		self.frame.grid(row = 0, column= 0, columnspan=1, padx=10)
		self.frame.config(bg='white')

		self.dateLabel=Label(self.frame)		
		self.dateLabel['text']='Fecha: '
		self.dateLabel.grid(row=1,column=0,padx=3)
		self.frameWidgets.append(self.dateLabel)

		self.dateLabel=Label(self.frame)		
		self.dateLabel['text']='{} '.format(self.info_Container.getYesterday())
		self.dateLabel.grid(row=1,column=1,padx=3)
		self.frameWidgets.append(self.dateLabel)

		self.totalLabel=Label(self.frame)		
		self.totalLabel['text']='TOTAL EN EFECTIVO:    {}'.format(self.infoList[0])
		self.totalLabel.grid(row=2,column=0,pady=3)
		self.frameWidgets.append(self.totalLabel)

		self.utilityLabel=Label(self.frame)		
		self.utilityLabel['text']='UTILIDAD:    {}'.format(self.infoList[1])
		self.utilityLabel.grid(row=3,column=0,pady=3)
		self.frameWidgets.append(self.utilityLabel)

		self.yBaseLabel=Label(self.frame)		
		self.yBaseLabel['text']='BASE:\t{}\t{}'.format(self.infoList[2],self.info_Container.getToday())
		self.yBaseLabel.grid(row=4,column=0,pady=3)
		self.frameWidgets.append(self.yBaseLabel)

		self.vNetaLabel=Label(self.frame)		
		self.vNetaLabel['text']='VENTA NETA:    {}'.format(self.infoList[3])
		self.vNetaLabel.grid(row=5,column=0,pady=3)
		self.frameWidgets.append(self.vNetaLabel)

		self.tBaseLabel=Label(self.frame)		
		self.tBaseLabel['text']='BASE: \t{}\t{}'.format(self.infoList[4],self.info_Container.getTomorrow())
		self.tBaseLabel.grid(row=6,column=0,pady=3)
		self.frameWidgets.append(self.tBaseLabel)

	def moneyFrame(self):
		##################  Frame de busqueda de productos  #######################

		#PENDIENTE:
		#self.infoList=[30,46,76,23,33]

		self.frame2=LabelFrame(self)
		self.frame2['text']='CANTIDAD DE DINERO {}'.format(self.info_Container.getToday())
		self.frame2.grid(row = 0, column= 1, columnspan=1, padx=10)
		self.frame2.config(bg='white')

		self.bill100Label=Label(self.frame2)		
		self.bill100Label['text']='BILLETES DE 100.000: '
		self.bill100Label.grid(row=0,column=0,padx=3)
		self.frameWidgets.append(self.bill100Label)

		self.bill50Label=Label(self.frame2)		
		self.bill50Label['text']='BILLETES DE 50.000:'
		self.bill50Label.grid(row=1,column=0,padx=3)
		self.frameWidgets.append(self.bill50Label)

		self.bill20Label=Label(self.frame2)		
		self.bill20Label['text']='BILLETES DE 20.000:'
		self.bill20Label.grid(row=2,column=0,pady=3)
		self.frameWidgets.append(self.bill20Label)

		self.bill10Label=Label(self.frame2)		
		self.bill10Label['text']='BILLETES DE 10.000:'
		self.bill10Label.grid(row=3,column=0,pady=3)
		self.frameWidgets.append(self.bill10Label)

		self.bill5Label=Label(self.frame2)		
		self.bill5Label['text']='BILLETES DE 5.000'
		self.bill5Label.grid(row=4,column=0,pady=3)
		self.frameWidgets.append(self.bill5Label)

		self.bill2Label=Label(self.frame2)		
		self.bill2Label['text']='BILLETES DE 2.000'
		self.bill2Label.grid(row=5,column=0,pady=3)
		self.frameWidgets.append(self.bill2Label)

		self.bill1Label=Label(self.frame2)		
		self.bill1Label['text']='BILLETES Y MONEDAS DE 1.000'
		self.bill1Label.grid(row=6,column=0,pady=3)
		self.frameWidgets.append(self.bill1Label)

		self.mon5Label=Label(self.frame2)		
		self.mon5Label['text']='MONEDAS DE 500'
		self.mon5Label.grid(row=7,column=0,pady=3)
		self.frameWidgets.append(self.mon5Label)

		self.mon2Label=Label(self.frame2)		
		self.mon2Label['text']='MONEDAS DE 200'
		self.mon2Label.grid(row=8,column=0,pady=3)
		self.frameWidgets.append(self.mon2Label)

		self.mon1Label=Label(self.frame2)		
		self.mon1Label['text']='MONEDAS DE 100'
		self.mon1Label.grid(row=9,column=0,pady=3)
		self.frameWidgets.append(self.mon1Label)

		self.mon50Label=Label(self.frame2)		
		self.mon50Label['text']='MONEDAS DE 50:'
		self.mon50Label.grid(row=10,column=0,pady=3)
		self.frameWidgets.append(self.mon50Label)

		self.bill100Entry=Entry(self.frame2)		
		self.bill100Entry.grid(row=0,column=1,padx=3)
		self.frameWidgets.append(self.bill100Entry)

		self.bill50Entry=Entry(self.frame2)		
		self.bill50Entry.grid(row=1,column=1,padx=3)
		self.frameWidgets.append(self.bill50Entry)

		self.bill20Entry=Entry(self.frame2)		
		self.bill20Entry.grid(row=2,column=1,pady=3)
		self.frameWidgets.append(self.bill20Entry)

		self.bill10Entry=Entry(self.frame2)		
		self.bill10Entry.grid(row=3,column=1,pady=3)
		self.frameWidgets.append(self.bill10Entry)

		self.bill5Entry=Entry(self.frame2)		
		self.bill5Entry.grid(row=4,column=1,pady=3)
		self.frameWidgets.append(self.bill5Entry)

		self.bill2Entry=Entry(self.frame2)		
		self.bill2Entry.grid(row=5,column=1,pady=3)
		self.frameWidgets.append(self.bill2Entry)

		self.bill1Entry=Entry(self.frame2)				
		self.bill1Entry.grid(row=6,column=1,pady=3)
		self.frameWidgets.append(self.bill1Entry)

		self.mon5Entry=Entry(self.frame2)				
		self.mon5Entry.grid(row=7,column=1,pady=3)
		self.frameWidgets.append(self.mon5Entry)

		self.mon2Entry=Entry(self.frame2)				
		self.mon2Entry.grid(row=8,column=1,pady=3)
		self.frameWidgets.append(self.mon2Entry)

		self.mon1Entry=Entry(self.frame2)				
		self.mon1Entry.grid(row=9,column=1,pady=3)
		self.frameWidgets.append(self.mon1Entry)

		self.mon50Entry=Entry(self.frame2)				
		self.mon50Entry.grid(row=10,column=1,pady=3)
		self.frameWidgets.append(self.mon50Entry)

	def graphicsFrame(self):
		self.var='LO QUE SEA'
		self.frame3=LabelFrame(self)
		self.frame3['text']='GRAFICAS DE {}'.format(self.var)
		self.frame3.grid(row = 0, column= 2, columnspan=1, padx=10)
		self.frame3.config(bg='white')

		self.table=ttk.Treeview(self.frame3)
		self.table.grid(row = 0, column= 0, columnspan=1, padx=10)				
		self.frameWidgets.append(self.table)

	def registerFrame(self):
		self.frame4=LabelFrame(self)
		self.frame4['text']='ACCIONES DE REGISTRO'
		self.frame4.grid(row=1,column=0,columnspan=1, padx=10, pady=10)

		self.registerVariable=''
		self.registerLabel=Label(self.frame4)
		self.registerLabel['text']='Mensaje: {}'.format(self.registerVariable)
		self.registerLabel.grid(row=0,column=1,padx=10,pady=5)

		self.doneButton=ttk.Button(self.frame4,command=self.doneSlot)
		self.doneButton['text']='TERMINAR'
		self.doneButton.grid(row=1,column=0,columnspan=1,padx=10,pady=2,sticky=W + E)


	#SLOTS#
	#SLOTS#Slot de button 'HECHO'
	def doneSlot(self):
		if self.info_Container.getToday()==self.date:
			try:
				if not self.info_Container.getCashState():																
					data=[]				
					data.append(int(self.bill100Entry.get())*100000)
					data.append(int(self.bill50Entry.get())*50000)
					data.append(int(self.bill20Entry.get())*20000)
					data.append(int(self.bill10Entry.get())*10000)
					data.append(int(self.bill5Entry.get())*5000)
					data.append(int(self.bill2Entry.get())*2000)
					data.append(int(self.bill1Entry.get())*1000)
					data.append(int(self.mon5Entry.get())*500)
					data.append(int(self.mon2Entry.get())*200)
					data.append(int(self.mon1Entry.get())*100)
					data.append(int(self.mon50Entry.get())*50)
					self.registerLabel['text']='Datos VALIDOS'
					self.info_Container.closeCash()
				else:					
					self.registerLabel['text']='LA CAJA YA HA SIDO CERRADA'
			except Exception as e:
				self.registerLabel['text']='Datos NO VALIDOS'

			self.info_Container.cashDayRegister(data)

		else:
			self.registerLabel['text']='EL CUADRE YA ESTA HECHO'			


	def deleteFrameWidgets(self):	
		for widget in self.frameWidgets:
			widget.grid_remove()
			widget.destroy()
		self.frameWidgets.clear()
		self.frame.destroy()					
		self.frame2.destroy()
		self.frame3.destroy()
	

	def desaparecer(self):
		self.deleteFrameWidgets()
		self.destroy()


#~~~~~~~~~~~~~~~~~~~~~~----------------FIN DE LA CLASE VENTANA_COMPRAS ---------------------------------·~#	


				#~~~~~~~~~~~~~~~~~~~~~~!!!!!FRAME DE RECORDATORIOS!!!!!!~~~~~~~~~~~~~~~~~~~~~~#
			   #~~~~~~~~~~~~~~~~~~~~~~!!!!!DISPONIBLE PARA USUARIOS!!!!!!~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~				
#Clase encargada de mostrar la funcion de notificaciones

class Notify(Frame):
	def __init__(self, frame,info_Container):
		super(Notify, self).__init__()
		self.mainframe=frame
		Frame.__init__(self, self.mainframe)
		self.pack(fill='both', expand=True)

		self.info_Container=info_Container

		self.frameWidgets=[]
		self.frameWidgets2=[]

		self.menuFrame()
		self.providersOrderFrame()
		#self.graphicsFrame()

	def menuFrame(self):
		##################  Frame de busqueda de productos  #######################

		#PENDIENTE:
		self.infoList=[30,46,76,23,33]

		self.frame=LabelFrame(self)
		self.frame['text']='MENU OPCIONES DE NOTIFICACIONES'
		self.frame.grid(row = 0, column= 0, columnspan=1, padx=10)
		self.frame.config(bg='white')

		self.opcLabel=Label(self.frame)		
		self.opcLabel['text']='OPCIONES: '
		self.opcLabel.grid(row=0,column=0,padx=3)
		self.frameWidgets.append(self.opcLabel)

		self.orderButton=ttk.Button(self.frame,command=self.providerOrderSlot)		
		self.orderButton['text']='PEDIDOS PENDIENTES: '
		self.orderButton.grid(row=1,column=0,padx=3,pady=3)
		self.frameWidgets.append(self.orderButton)

		self.order2Button=ttk.Button(self.frame,command=self.deliveryOrderSlot)		
		self.order2Button['text']='DOMICILIOS PENDIENTES: '
		self.order2Button.grid(row=2,column=0,padx=3,pady=3)
		self.frameWidgets.append(self.order2Button)

		self.order3Button=ttk.Button(self.frame,command=self.clientOrderSlot)		
		self.order3Button['text']='ENCARGOS PENDIENTES: '
		self.order3Button.grid(row=3,column=0,padx=3,pady=3)
		self.frameWidgets.append(self.order3Button)

		self.order4Button=ttk.Button(self.frame,command=self.rememberingSlot)		
		self.order4Button['text']='RECORDATORIOS PENDIENTES: '
		self.order4Button.grid(row=4,column=0,padx=3,pady=3)
		self.frameWidgets.append(self.order4Button)

		self.order5Button=ttk.Button(self.frame,command=self.debtsSlot)		
		self.order5Button['text']='DEUDAS PENDIENTES: '
		self.order5Button.grid(row=5,column=0,padx=3,pady=3)
		self.frameWidgets.append(self.order5Button)

		
	def providersOrderFrame(self):
		##################  Frame de busqueda de productos  #######################

		#PENDIENTE:
		#self.infoList=[30,46,76,23,33]
		self.frame2=LabelFrame(self)
		self.frame2['text']='-----------------------------------------------------PEDIDOS-----------------------------------------'
		self.frame2.grid(row = 0, column= 1, columnspan=1, padx=10)
		self.frame.config(bg='white')

		self.dateLabel=Label(self.frame2)
		self.dateLabel['text']='Fecha de Pedidos'
		self.dateLabel.grid(row=0,column=0,pady=10,padx=3)
		self.frameWidgets2.append(self.dateLabel)

		listDate=['15-AGOSTO','16-AGOSTO']
		self.date=ttk.Combobox(self.frame2,values=listDate)
		self.date.config(width=20)
		self.date.grid(row=0,column=1,pady=10,padx=3)
		self.frameWidgets2.append(self.date)

		self.orderProviderTable=ttk.Treeview(self.frame2,height=11,columns=2)
		self.orderProviderTable.grid(row=1,column=0,pady=3,padx=3,columnspan=100)
		self.orderProviderTable.column('#0',width=350,anchor=CENTER)
		self.orderProviderTable.heading('#0',text='PROVEEDOR')
		self.orderProviderTable.column('#1',width=350,anchor=CENTER)
		self.orderProviderTable.heading('#1',text='VALOR')
		self.frameWidgets2.append(self.orderProviderTable)

		self.deleteButton=ttk.Button(self.frame2,command=self.deleteOrder)
		self.deleteButton['text']='Llegó'
		self.deleteButton.grid(row=2,column=0,padx=5,pady=5)
		self.frameWidgets2.append(self.deleteButton)
	


	def deliveryOrderFrame(self):
		##################  Frame de busqueda de productos  #######################

		#PENDIENTE:
		#self.infoList=[30,46,76,23,33]
		self.frame2=LabelFrame(self)
		self.frame2['text']='-----------------------------------------------------DOMICILIOS-----------------------------------------'
		self.frame2.grid(row = 0, column= 1, columnspan=1, padx=10)
		self.frame.config(bg='white')

		self.dateLabel=Label(self.frame2)
		self.dateLabel['text']='DOMICILIOS POR ENTREGAR:'
		self.dateLabel.grid(row=0,column=0,pady=10,padx=3)
		self.frameWidgets2.append(self.dateLabel)

		#listDate=['15-AGOSTO','16-AGOSTO']
		#self.date=ttk.Combobox(self.frame2,values=listDate)
		#self.date.config(width=20)
		#self.date.grid(row=0,column=1,pady=10,padx=3)
		#self.frameWidgets2.append(self.date)

		self.orderProviderTable=ttk.Treeview(self.frame2,height=11,columns=3)
		self.orderProviderTable.grid(row=1,column=0,pady=3,padx=3,columnspan=100)
		self.orderProviderTable['columns']=['Column 2','Column 3']
		self.orderProviderTable.column('#0',width=250,anchor=CENTER)
		self.orderProviderTable.heading('#0',text='DIRECCION')
		self.orderProviderTable.column('#1',width=350,anchor=CENTER)
		self.orderProviderTable.heading('#1',text='PRODUCTOS')
		self.orderProviderTable.column('#2',width=150,anchor=CENTER)
		self.orderProviderTable.heading('#2',text='VALOR TOTAL')
		self.frameWidgets2.append(self.orderProviderTable)

		self.deleteButton=ttk.Button(self.frame2,command=self.deliveryDone)
		self.deleteButton['text']='HECHO'
		self.deleteButton.grid(row=2,column=0,padx=5,pady=5)
		self.frameWidgets2.append(self.deleteButton)	

	def clientOrderFrame(self):
		##################  Frame de busqueda de productos  #######################

		#PENDIENTE:
		#self.infoList=[30,46,76,23,33]
		self.frame2=LabelFrame(self)
		self.frame2['text']='-----------------------------------------------------ENCARGOS-----------------------------------------'
		self.frame2.grid(row = 0, column= 1, columnspan=1, padx=10)
		self.frame.config(bg='white')

		self.dateLabel=Label(self.frame2)
		self.dateLabel['text']='Fecha de Encargos'
		self.dateLabel.grid(row=0,column=0,pady=10,padx=3)
		self.frameWidgets2.append(self.dateLabel)

		listDate=['15-AGOSTO','16-AGOSTO']
		self.date=ttk.Combobox(self.frame2,values=listDate)
		self.date.config(width=20)
		self.date.grid(row=0,column=1,pady=10,padx=3)
		self.frameWidgets2.append(self.date)

		self.orderProviderTable=ttk.Treeview(self.frame2,height=11,columns=3)
		self.orderProviderTable.grid(row=1,column=0,pady=3,padx=3,columnspan=100)
		self.orderProviderTable['columns']=['Column 2','Column 3']
		self.orderProviderTable.column('#0',width=350,anchor=CENTER)
		self.orderProviderTable.heading('#0',text='CLIENTE')
		self.orderProviderTable.column('#1',width=350,anchor=CENTER)
		self.orderProviderTable.heading('#1',text='PRODUCTOS')
		self.orderProviderTable.column('#2',width=150,anchor=CENTER)
		self.orderProviderTable.heading('#2',text='CANTIDAD')
		self.frameWidgets2.append(self.orderProviderTable)

		self.deleteButton=ttk.Button(self.frame2,command=self.clientOrderDone)
		self.deleteButton['text']='REALIZADO'
		self.deleteButton.grid(row=2,column=0,padx=5,pady=5)
		self.frameWidgets2.append(self.deleteButton)	


	def rememberingFrame(self):
		##################  Frame de busqueda de productos  #######################

		#PENDIENTE:
		#self.infoList=[30,46,76,23,33]
		self.frame2=LabelFrame(self)
		self.frame2['text']='-----------------------------------------------------RECORDATORIOS-----------------------------------------'
		self.frame2.grid(row = 0, column= 1, columnspan=1, padx=10)
		self.frame.config(bg='white')

		self.dateLabel=Label(self.frame2)
		self.dateLabel['text']='RECUERDA RESPIRAR'
		self.dateLabel.grid(row=0,column=0,pady=10,padx=3)
		self.frameWidgets2.append(self.dateLabel)

		#listDate=['15-AGOSTO','16-AGOSTO']
		#self.date=ttk.Combobox(self.frame2,values=listDate)
		#self.date.config(width=20)
		#self.date.grid(row=0,column=1,pady=10,padx=3)
		#self.frameWidgets2.append(self.date)

		self.orderProviderTable=ttk.Treeview(self.frame2,height=11,columns=2)
		self.orderProviderTable.grid(row=1,column=0,pady=3,padx=3,columnspan=100)
		self.orderProviderTable.column('#0',width=350,anchor=CENTER)
		self.orderProviderTable.heading('#0',text='DESCRIPCION')
		self.orderProviderTable.column('#1',width=350,anchor=CENTER)
		self.orderProviderTable.heading('#1',text='FECHA LIMITE')
		self.frameWidgets2.append(self.orderProviderTable)

		self.deleteButton=ttk.Button(self.frame2,command=self.forgeting)
		self.deleteButton['text']='ELIMINAR RECORDATORIO'
		self.deleteButton.grid(row=2,column=0,padx=5,pady=5)
		self.frameWidgets2.append(self.deleteButton)
		
	def debtsFrame(self):
		##################  Frame de busqueda de productos  #######################

		#PENDIENTE:
		#self.infoList=[30,46,76,23,33]
		self.frame2=LabelFrame(self)
		self.frame2['text']='-----------------------------------------------------DEUDAS-----------------------------------------'
		self.frame2.grid(row = 0, column= 1, columnspan=1, padx=10)
		self.frame.config(bg='white')

		self.dateLabel=Label(self.frame2)
		self.dateLabel['text']='RECUERDA RESPIRAR'
		self.dateLabel.grid(row=0,column=0,pady=10,padx=3)
		self.frameWidgets2.append(self.dateLabel)

		#listDate=['15-AGOSTO','16-AGOSTO']
		#self.date=ttk.Combobox(self.frame2,values=listDate)
		#self.date.config(width=20)
		#self.date.grid(row=0,column=1,pady=10,padx=3)
		#self.frameWidgets2.append(self.date)

		self.orderProviderTable=ttk.Treeview(self.frame2,height=11,columns=3)
		self.orderProviderTable.grid(row=1,column=0,pady=3,padx=3,columnspan=100)
		self.orderProviderTable['columns']=['Column 2','Column 3']
		self.orderProviderTable.column('#0',width=350,anchor=CENTER)
		self.orderProviderTable.heading('#0',text='DESCRIPCION')
		self.orderProviderTable.column('#1',width=150,anchor=CENTER)
		self.orderProviderTable.heading('#1',text='FECHA LIMITE')
		self.orderProviderTable.column('#2',width=150,anchor=CENTER)
		self.orderProviderTable.heading('#2',text='VALOR')
		self.frameWidgets2.append(self.orderProviderTable)

		self.deleteButton=ttk.Button(self.frame2,command=self.debtPaid)
		self.deleteButton['text']='DEUDA PAGADA :D'
		self.deleteButton.grid(row=2,column=0,padx=5,pady=5)
		self.frameWidgets2.append(self.deleteButton)	

	def graphicsFrame(self):
		self.var='LO QUE SEA'
		self.frame3=LabelFrame(self)
		self.frame3['text']='GRAFICAS DE {}'.format(self.var)
		self.frame3.grid(row = 0, column= 2, columnspan=1, padx=10)
		self.frame3.config(bg='white')

		self.table=ttk.Treeview(self.frame3)
		self.table.grid(row = 0, column= 0, columnspan=1, padx=10)				
		self.frameWidgets.append(self.table)

	#SLOTS DE ELECCION
	
	def providerOrderSlot(self):
		self.deleteFrame2Widgets()
		self.providersOrderFrame()

	def	deliveryOrderSlot(self):
		self.deleteFrame2Widgets()
		self.deliveryOrderFrame()

	def clientOrderSlot(self):
		self.deleteFrame2Widgets()
		self.clientOrderFrame()

	def rememberingSlot(self):
		self.deleteFrame2Widgets()
		self.rememberingFrame()

	def debtsSlot(self):
		self.deleteFrame2Widgets()
		self.debtsFrame()



	#SLOTS DE FRAME SECUNDARIOS	

	def deleteOrder(self):
		print('eliminando: ',self.orderProviderTable.selection())

	def deliveryDone(self):
		print('eliminando: ',self.orderProviderTable.selection())

	def clientOrderDone(self):
		print('eliminando: ',self.orderProviderTable.selection())
		
	def forgeting(self):
		print('eliminando: ',self.orderProviderTable.selection())
		
	def debtPaid(self):
		print('eliminando: ',self.orderProviderTable.selection())					



	def deleteFrameWidgets(self):	
		for widget in self.frameWidgets:
			widget.grid_remove()
			widget.destroy()
		self.frameWidgets.clear()
		self.frame.destroy()					
		#self.frame3.destroy()

	def deleteFrame2Widgets(self):	
		for widget in self.frameWidgets2:
			widget.grid_remove()
			widget.destroy()
		self.frameWidgets2.clear()					
		self.frame2.destroy()
		#self.frame3.destroy()

	def desaparecer(self):
		self.deleteFrameWidgets()
		self.deleteFrame2Widgets()
		self.destroy()	

#~~~~~~~~~~~~~~~~~~~~~~----------------FIN DE LA CLASE VENTANA_COMPRAS ---------------------------------·~#	


				#~~~~~~~~~~~~~~~~~~~~~~!!!!!FRAME DE MUESTRA DE DATOS!!!!!!~~~~~~~~~~~~~~~~~~~~~~#
			#~~~~~~~~~~~~~~~~~~~~~~!!!!!DISPONIBLE SOLO PARA ADMINISTRADORES!!!!!!~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~				
#Clase encargada de mostrar la funcion de balance de datos

class dataStudy(Frame):
	def __init__(self, frame,info_Container):
		super(dataStudy, self).__init__()
		self.mainframe=frame
		Frame.__init__(self, self.mainframe)
		self.pack(fill='both', expand=True)


		self.info_Container=info_Container

		self.frameWidgets=[]

		self.infoFrame()
		self.moneyFrame()
		self.graphicsFrame()

	def infoFrame(self):
		##################  Frame de busqueda de productos  #######################

		#PENDIENTE:
		self.infoList=[30,46,76,23,33]

		self.frame=LabelFrame(self)
		self.frame['text']='GRAFICAS DE COMPORTAMIENTOS'
		self.frame.grid(row = 0, column= 0, columnspan=1, padx=10)
		self.frame.config(bg='white')

		self.opcLabel=Label(self.frame)		
		self.opcLabel['text']='OPCIONES: '
		self.opcLabel.grid(row=0,column=0,padx=3)
		self.frameWidgets.append(self.opcLabel)

		self.orderButton=ttk.Button(self.frame,command=self.grafica1Slot)		
		self.orderButton['text']='GRAFICA 1: '
		self.orderButton.grid(row=1,column=0,padx=3,pady=3)
		self.frameWidgets.append(self.orderButton)

		self.order2Button=ttk.Button(self.frame,command=self.grafica2Slot)		
		self.order2Button['text']='GRAFICA 2 '
		self.order2Button.grid(row=2,column=0,padx=3,pady=3)
		self.frameWidgets.append(self.order2Button)

		self.order3Button=ttk.Button(self.frame,command=self.grafica3Slot)		
		self.order3Button['text']='GRAFICA 3: '
		self.order3Button.grid(row=3,column=0,padx=3,pady=3)
		self.frameWidgets.append(self.order3Button)

		self.order4Button=ttk.Button(self.frame,command=self.grafica4Slot)		
		self.order4Button['text']='GRAFICA 4 '
		self.order4Button.grid(row=4,column=0,padx=3,pady=3)
		self.frameWidgets.append(self.order4Button)

		self.order5Button=ttk.Button(self.frame,command=self.grafica5Slot)		
		self.order5Button['text']='GRAFICA 5 '
		self.order5Button.grid(row=5,column=0,padx=3,pady=3)
		self.frameWidgets.append(self.order5Button)

	def moneyFrame(self):
		##################  Frame de busqueda de productos  #######################

		#PENDIENTE:
		#self.infoList=[30,46,76,23,33]
		self.variable='POR LO TANTO'
		self.frame2=LabelFrame(self)
		self.frame2['text']='-------------------------GRAFICA DE  {} VS TIEMPO --------------------------'.format(self.variable)
		self.frame2.grid(row = 0, column= 1, columnspan=1, padx=10)
		self.frame2.config(bg='white')

		

	def graphicsFrame(self):
		self.var='LO QUE SEA'
		self.frame3=LabelFrame(self)
		self.frame3['text']='GRAFICAS DE {}'.format(self.var)
		self.frame3.grid(row = 0, column= 2, columnspan=1, padx=10)
		self.frame3.config(bg='white')

		self.table=ttk.Treeview(self.frame3)
		self.table.grid(row = 0, column= 0, columnspan=1, padx=10)				
		self.frameWidgets.append(self.table)

	#SLOTS DE GRAFICAS
	
	def grafica1Slot(self):
		self.info_Container.graficaBreve(1)

	def grafica2Slot(self):
		print("Grafica 2")
		
	def grafica3Slot(self):
		print("Grafica 3")
		
	def grafica4Slot(self):
		print("Grafica 4")

	def grafica5Slot(self):
		print("Grafica 5")					

	def deleteFrameWidgets(self):	
		for widget in self.frameWidgets:
			widget.grid_remove()
			widget.destroy()
		self.frameWidgets.clear()
		self.frame.destroy()					
		self.frame2.destroy()
		self.frame3.destroy()
	

	def desaparecer(self):
		self.deleteFrameWidgets()
		self.destroy()	

#~~~~~~~~~~~~~~~~~~~~~~----------------FIN DE LA CLASE VENTANA_COMPRAS ---------------------------------·~#	


				#~~~~~~~~~~~~~~~~~~~~~~!!!!!CCCLLLAAASSSEEE!!!!!!~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~				
#Clase encargada de mostrar la funcion de compras

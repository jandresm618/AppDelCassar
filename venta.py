from tkinter import ttk 
from tkinter import *





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

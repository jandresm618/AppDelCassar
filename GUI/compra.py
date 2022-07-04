from tkinter import ttk 
from tkinter import *


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
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk 
from matplotlib.figure import Figure
from tkinter import ttk 
from tkinter import *
from manejo_datos import *
from tkinter import messagebox
from venta import *
from compra import *
from cierre_caja import *
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

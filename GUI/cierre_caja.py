from tkinter import ttk 
from tkinter import *

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

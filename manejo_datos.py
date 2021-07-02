import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
from datetime import datetime, timedelta

def diffStrings(string1,string2):
	strF = ""
	cont1 = 0
	cont2 = 0
	for i in string1:
		for j in string2:			
			if cont1 == cont2 or cont2 > len(string1) or cont1 > len(string2):
				print("Valida los numeros")
				print(i," - ",j)
				if not (i == j):
					print("Valida las letras")
					strF += i
					break
			cont2 += 1
		cont2 = 0	
		cont1 += 1
	print("STring FINAL ",strF)	
	return strF
def overShape(string1,string2):
	strF = ""
	if len(string1) > len(string2):
		strF = string1[len(string2)+1:len(string1)+1]
	elif len(string1) < len(string2):
		strF = string2[len(string1)+1:len(string2)+1]
	return strF					


#CLASE InfoContainer: Esta clase se encarga de modelar el manejo de Informacion del negocio
class InfoContainer(object):

	def __init__(self):
		self.cash_closed = False
		self.total_soldOut = 0
		self.total_cashIn = 0
		self.total_QR = 0
		self.total_bought = 0
		self.total_cashOut = 0

		self.iva = 1.19
		
		self.data_list=[]
		self.search_list=[]
		self.provider_list=[]
		self.excel_name = "Archivos/Codigos.xlsx"
		self.out_path = "Archivos/salida_productos.csv"
		self.in_path = "Archivos/entrada_productos.csv"
		self.devoluciones_path = "Archivos/devoluciones.csv"
		self.pedidos_path = "Archivos/pedidos.csv"
		self.productos_columns=('Codigo', 'DESCRIPCION', 'PRECIO', 'Cantidad Inicial',  'Cantidad Actual', 'Rotacion','Granel','PROVEEDOR')
		self.ventas_columns=('ID VENTA','CODIGO','DESCRIPCION','PRECIO','NOMBRE VENDEDOR','NOMBRE COMPRADOR')
		
		self.delivery_columns=('ID PEDIDO','ESTADO','DESCRIPCION','NOMBRE CLIENTE','TELEFONO CLIENTE','DIRECCION CLIENTE','NOMBRE VENDEDOR')
		self.trust_columns=('ID FIADO','ESTADO','DESCRIPCION','NOMBRE CLIENTE','NOMBRE VENDEDOR')
		self.proveedores_columns=('NOMBRE','NIT','DIAS','TELEFONO','CORREO')
		self.compras_columns=('ID COMPRA','CODIGO','DESCRIPCION','PRECIO','CANTIDAD','NOMBRE PROVEEDOR','NOMBRE TRABAJADOR')
		
		"""ARCHIVOS SIMPLIFICADOS"""
		self.out_columns = ('FECHA','HORA','CODIGO','DESCRIPCION','TIPO','PRECIO','FORMA DE PAGO','NOMBRE VENDEDOR','NOMBRE COMPRADOR')
		self.in_columns = ('FECHA','HORA','CODIGO','DESCRIPCION','COMPRA/CAMBIO','GRANEL','CANTIDAD','PRECIO','PROVEEDOR','NOMBRE VENDEDOR')
		self.pedidos_columns = ('FECHA 1','FECHA 2','DECRIPCION','GRANEL','CANTIDAD','PRECIO','PROVEEDOR','NOMBRE VENDEDOR')
		self.return_columns = ('ID DEV','CODIGO','DESCRIPCION','PRECIO','FORMA DE DEVOLUCION','NOMBRE VENDEDOR','NOMBRE COMPRADOR')
		
		self.page='Hoja 1'
		self.dataUpload()
		
	def closeCash(self):
		self.cash_closed = True

	#METODOS GET#
	def getIva(self):
		return self.iva
	def getCashState(self):
		return self.cash_closed	
	def getDfInventario(self):
		return self.dfInventario
	def getDfVentas(self):
		return self.dfVentas
	def getDfProveedores(self):
		return self.dfProveedores		
	def getProducts(self):
		return self.data_list
	def getProviders(self):
		return self.provider_list
	def getProvidersNames(self):
		providersNames = []
		for i in self.provider_list:
			providersNames.append(i.getNombre())
		return providersNames	

	#METODOS DE MANEJO DEL TIEMPO	
	def getToday(self):
		return date.today()
	def getTomorrow(self):
		return date.today()	+ timedelta(days=1)
	def getYesterday(self):
		return date.today()	+ timedelta(days=-1)	
	def getNow(self):
		return	datetime.now()
	def getWeekDays(self,limit):		
		days=[]
		for i in range(limit):
			days.append(date.today()	+ timedelta(days=-i))
		return days					

	#METODOS DE MANIPULACION DE DATAFRAMES
	def df2List(self,dataframe):
		listReturn=[]
		listAux=[]
		listColumns = list(dataframe)
		cont=0
		for serie in dataframe[listColumns[0]]:			
			listAux=[]	
			for column in listColumns:
				listAux.append(dataframe.iloc[cont][column])	
			listReturn.append(listAux)
			cont+=1				
		return listReturn
		"""CARGA PRODUCTOS DEL DATAFRAME"""
	def uploadProducts(self):
		cont = 0
		list_value = []			
		for elem in self.dfInventario[self.productos_columns[0]]:
			for column in self.productos_columns:
				elem=self.dfInventario[column].loc[cont]
				list_value.append(elem)
			product=Producto(list_value)
			self.data_list.append(product)
			list_value.clear()
			cont=cont+1
		cont=0
	def uploadProviders(self):
		try:
			cont = 0
			list_value = []
			for row in self.dfProveedores[self.proveedores_columns[0]]:				
				for column in self.proveedores_columns:
					elem=self.dfProveedores[column].loc[cont]
					list_value.append(elem)	
				pro=Proveedor(list_value)
				self.provider_list.append(pro)
				list_value.clear()
				cont+=1
			print("Proveedores Cargados Correctamente ",len(self.provider_list))		
		except Exception as e:
			print(e)
			print("!!!!!!!!!!!!!!!!!!No se pudo cargar los proveedores!!!!!!!!!!")
	def list_to_df(self):
		cont = 0
		self.dfInventario = pd.DataFrame(columns=self.productos_columns)
		for i in self.data_list:
			self.dfInventario.loc[cont] = i.atributes()
			cont=cont+1
		cont=0
		self.dfProveedores=pd.DataFrame(columns=self.proveedores_columns)
		for i in self.provider_list:
			self.dfProveedores.loc[cont] = i.atributes()
			cont=cont+1			

	#METODOS DE CARGA#
	def dataUpload(self):
		#Carga los Datos del Archivo CODIGOS.xlsx HOJA 1
		col_types = {"Codigo":str, "DESCRIPCION":str}
		self.dfInventario = pd.read_excel(self.excel_name,sheet_name='Hoja 1',dtype=col_types)
		#self.dfInventario=self.dfInventario.replace(np.nan,0).ffill()
		print("Productos cargados correctamente. ", len(self.data_list))

		#Carga los Datos del Archivo CODIGOS.xlsx HOJA 2
		self.dfVentas = pd.read_excel(self.excel_name,sheet_name='Hoja 2',index_col=[0])
		self.dfVentas = self.dfVentas.replace(0,np.nan).ffill()

		#Carga los Datos del Archivo CODIGOS.xlsx HOJA 3
		col_types = {"NOMBRE":str, "NIT":str,"DIAS":str,"TELEFONO":str}
		self.dfProveedores = pd.read_excel(self.excel_name,sheet_name='Hoja 3',dtype=col_types)
		self.dfProveedores = self.dfProveedores.replace(0,np.nan).ffill()
		
		#Carga los Datos de los Archivos CSV
		self.dfOut = pd.read_csv(self.out_path)
		self.dfIn = pd.read_csv(self.in_path)
		self.dfPedidos = pd.read_csv(self.pedidos_path)
		self.dfDevoluciones = pd.read_csv(self.devoluciones_path)
				

		#Carga de lista de Productos y Proveedores
		self.uploadProducts()
		self.uploadProviders()

	#METODOS DE GUARDADO#	
	def save(self):
		print("Guardandooo....")
		print(self.dfVentas)

		df_to_save = self.list_to_df()
		grabar = pd.ExcelWriter(self.excel_name)
		df_to_save.to_excel(grabar,'Hoja 1')

		self.dfVentas.to_excel(grabar,'Hoja 2')
		grabar.save()
	#Metodo Generalizado para Guardar
	def guardarExcel(self,name,dataFrame,sheet):
		guardar = pd.ExcelWriter(name)
		dataFrame.to_excel(sheet)
		guardar.save()
		
	def guardarCsv(self,name,dataFrame):
		try:
			dataFrame.to_csv(name)
			return True
		except Exception as e:
			print("NO SE HA GUARDADO EL ARCHIVO CSV.\n",e)
			return False

	#METODOS DE DINAMICOS DE INFORMACION
		#"""SE MODIFICAN LOS DATOS DE LOS DATAFRAME VENTAS"""
			#		"""AÑADIR COLUMNA AL DATAFRAME"""
	def addRow(self,dataFrame,listData):
		try:
			print(len(listData))
			index = len(dataFrame.index)
			dataFrame.loc[index] = listData
		except Exception as e:
			print(e)
			print("Error al Agregar Fila al DataFrame")
	def tabOutData(self,productData,typo,shape,buyername,username):
		aux = []
		aux.append(str(date.today())) #Fecha
		aux.append(overShape(str(date.today()),str(datetime.now()))) #Hora
		aux.append(productData['text']) #Codigo
		aux.append(productData['values'][0]) #Descripcion
		aux.append(typo) #Tipo de Salida
		aux.append(productData['values'][1]) # Precio
		aux.append(shape) # Forma de Pago
		aux.append(username) # Nombre del Vendedor
		aux.append(buyername) # Nombre del Comprador
		return aux

	def addOut(self,products,typo,shape,buyername,username):
		aux = []
		auxVenta = 0
		try:
			for product in products:
				if self.validarDatos(product):
					#index=self.selectProducto([product['text'],product['values'][0]])
					#if self.data_list[index].setOut(1):
					#Tabulacion de Datos
					aux = self.tabOutData(product,typo,shape,buyername,username)
					price = int(product['values'][1])
					#Agregar Datos Economicos
					auxVenta += price
					#Añadir datos al DataFrame
					self.addRow(self.dfOut,aux)
					#Modificar Datos del producto
					
					aux.clear()
			#Guardar Datos
			print(self.dfOut)
			print("Venta Total: ",auxVenta)
			return auxVenta
			
		except Exception as e:
			print("!!!!!!!!!!!!!!!!!!No se pudo completar!!!!!!!!!!\n",e)
			return 0
	
	def addSale(self,sold_Product,buyername,username):	
		cont=0		
		new_df2=pd.DataFrame(columns=self.ventas_columns)
		try:
			for product in sold_Product:
				#print("HORA: ",overShape(str(date.today()),str(datetime.now())))
				#print("Dia de la semana ", date.today().weekday())							
				new_df2.loc[cont]=[str(datetime.now()),int(product['text']),product['values'][0],int(product['values'][1]),buyername,username]
				cont+=1
				index=self.selectProducto([product['text'],product['values'][0]])			
				self.data_list[index].minusCantidad(1)
			self.dfVentas = pd.concat((self.dfVentas,new_df2))
			#print(self.dfVentas)			
			return self.addingSale(sold_Product)

		except Exception as e:
			print("ERROR: No se pudo completar la venta.\n",e)
			return 0

	#			"""ELIMINAR COLUMNA AL DATAFRAME"""
	def deleteSale(self,item):
		try:
			self.dfVentas=self.deleteItemDataFrame(self.dfVentas,'ID VENTA',[item['text'],item['values']])
			print("Se elimino del dataframe")				
		except Exception as e:
			print("Error al eliminar del dataframe")
		print("Nuevo DataFrame")
		print(self.dfVentas)	
		return self.dfVentas								


		#INCOMPLETO
	#"""SE MODIFICAN LOS DATOS DE LOS DATAFRAME DOMICILIOS"""
	#			"""AÑADIR COLUMNA AL DATAFRAME"""		
	def addDelivery(self,sold_Product,clientDeliveryInfo,username):
		print("Para domicilio: ")
		print("Direccion: ",clientDeliveryInfo[0])
		print("Nombre: ",clientDeliveryInfo[1])
		print("Telefono: ",clientDeliveryInfo[2])
		for product in sold_Product:
			print(product['values'][0])
			#AGREGAR AL DATAFRAME DE DELIVERYS
			index=self.selectProducto([product['text'],product['values'][0]])			
			self.data_list[index].minusCantidad(1)

		return self.addingSale(sold_Product)	

	def addTrusted(self,sold_Product,clientTrust,username):
		print("Para fiado: ")
		print("Nombre: ",clientTrust)
		for product in sold_Product:
			#AGREGAR AL DATAFRAME DE TRUSTED
			print(product['values'][0])
			index = self.selectProducto([product['text'],product['values'][0]])			
			self.data_list[index].minusCantidad(1)				
		return self.addingSale(sold_Product)	

	def addIn(self,buyList,provider,username):
		cont = 0
		aux = []
		for product in buyList:
			aux.append(str(date.today()))
			aux.append(overShape(str(date.today()),str(datetime.now()))) #Hora
			aux += product
			aux.append(provider)
			aux.append(username)
			print(product[0],product[1],product[2],product[3],product[4],product[5])
			#Codigo#Decripcion#Cambio/Compra#Granel	#Cantidad#Con o sin Iva #Precio

			index = self.selectProducto([product[0:1]])
			self.data_list[index].setIn(product,provider)

			self.addRow(self.dfIn,aux)
			aux.clear()

			cont += 1
		print(self.dfIn)	

	def addBuy(self,bought_Product,listNewProducts,provider,username):	
		cont = 0
		new_df2 = pd.DataFrame(columns=self.compras_columns)
		try:
			for product in bought_Product:
				new_df2.loc[cont] = [str(datetime.now()),int(product['text']),product['values'][0],int(product['values'][1]),int(product['values'][2]),provider,username]
				cont+=1
				index = self.selectProducto([product['text'],product['values'][0]])
				self.data_list[index].plusCantidad(product['values'][2])
				#TENER EN CUENTA CUANDO NO ES CON IVA
				self.data_list[index].setPrecioVenta(product['values'][1])

			#self.dfVentas=pd.concat((self.dfVentas,new_df2))
			print(new_df2)			
			return self.addingBuy(bought_Product,listNewProducts)

		except Exception as e:
			print("!!!!!!!!!!!!!!!!!!No se pudo completar la compra!!!!!!!!!!")
			return 0
			
		#METODOS DE BUSQUEDA# SE BUSCA DATOS EN LOS DATAFRAMES
	def searchProductByCode(self,code):
		return self.searchDataFrame(self.dfInventario,'CODIGO',code)
	def searchProductByName(self,name):
		return self.searchDataFrame(self.dfInventario,'DESCRIPCION',name)
	def searchProductByPrice(self,price):
		return self.searchDataFrame(self.dfInventario,'PRECIO',price)
	def searchProductByProvider(self,provider):
		return self.searchDataFrame(self.dfInventario,'PROVEEDOR',provider)				
	def searchSaleByDate(self,date):
		return self.searchDataFrame(self.dfVentas,'ID VENTA',date)
	def searchDeliveryByDate(self,date):
		self.searchDataFrame(self.dfVentas,'ID VENTA',date)	
	def searchTrustByDate(self,date):
		self.searchDataFrame(self.dfVentas,'ID VENTA',date)
	def searchTrustByState(self,state):
		pass				
	def searchTrustByName(self,name):
		pass
	

	def deleteItemDataFrame(self,dataframe,column,data):
		try:
			df = dataframe.drop(dataframe[dataframe==data].index)
			return df			
		except Exception as e:
			print("No se puede ejecutar esta forma de eliminar")
		
				
	#METODO DE BUSQUEDA EN DATAFRAME
	def searchDataFrame(self,dataframe,column,data):
		listThings=[]
		cont=0
		columns=list(dataframe)
		newDf=pd.DataFrame(columns=columns)
		for i in dataframe[column]:
			if data in str(i):	
				listThings.clear()			
				for c in columns:
					listThings.append(dataframe.iloc[cont][c])
				newDf.loc[cont]=listThings
			cont+=1			
		return self.df2List(newDf)

	def returnItemSold(self,item):
		index=self.searchItemSold(item)
		print(self.dfVentas.index[index])
		self.dfVentas=self.dfVentas.drop(self.dfVentas.index[index])
		return self.dfVentas	

	def searchItemSold(self,item):
		index=self.searchItemDataFrame(self.dfVentas,item)
		return index	

	def searchItemDataFrame(self,dataframe,item):
		cont=0
		matchCont=0
		listColumns=list(dataframe)
		if type(item)==dict:
			for serie in dataframe[listColumns[0]]:
				if item['text']== str(dataframe.iloc[cont][listColumns[0]]):
					matchCont+=1
					iterColumnsCont=0
					for column in listColumns:
						iterValuesCont=0
						for value in item['values']:
							if (iterColumnsCont==iterValuesCont+1)&(str(dataframe.iloc[cont][column]) == str(value)):
								matchCont+=1
							if matchCont==len(item['values']):
								matchCont=0
								return cont	
							iterValuesCont+=1
						iterColumnsCont+=1				
				else:
					matchCont=0						
				cont+=1
				matchCont=0				
		#BUSQUEDA EN LISTA DE PRODUCTOS
		
	def searchData(self, item):
		cont_aux=0
		self.search_list.clear()
		#print("PRODUCTOSSS")
		for i in self.data_list:	
			if i.busquedaAvanzada(item):
				cont_aux=cont_aux+1
				self.search_list.append(i)
				print("Producto ",cont_aux,". ",i.nombre,"-----",i.codigo,"---->", i.precio)
		if(cont_aux==0):
			print("PRODUCTO NO ENCONTRADO!!!")
		return self.search_list	

	def selectProducto(self, listData):
		for product in self.data_list:
			if product.coincide(listData):
				print("Coincidio ",product.Nombre())
				return self.data_list.index(product)
				break
		return False



	#METODOS OPERACIONALES# AQUI SE EJECUTAN OPERACIONES
	def addingSale(self,sold_Product):
		saleValue=0
		for product in sold_Product:		
			saleValue+=int(product['values'][1])
		
		return saleValue

		#INCOMPLETO		
		#Modificar cantidad del producto
	def addingBuy(self,bought_Product,listNewProducts):
		saleValue=0		
		for product in bought_Product:
			saleValue+=(int(product['values'][1])*int(product['values'][2]))
			
			#DEBUG#print(int(product['values'][1]),' * ',int(product['values'][2]))


		for product in listNewProducts:
			saleValue+=(int(product[2])*int(product[3]))
			
			#DEBUG#print(int(product[2]),'--*--',int(product[3]))
			print("Valor de Compra: {}".format(saleValue))		
		
		return saleValue	

	def cashDayRegister(self,listData):
		total=0
		base=0
		base_ant=64000
		for data in listData:
			if listData.index(data)>5:
				base+=data
			total+=data
		print(total)
		print('venta neta: ',total-base_ant)
		print('base: ',base)
		print('Utilidad: ',total*0.2)	
		return self.validarDatos(listData)

		#INCOMPLETO:	
	def graficaBreve(self,inte):
		vectorinicial=np.random.normal(2000000,250000,5000)
		plt.hist(vectorinicial,50)
		plt.show()			
	
	#METODOS DE VALIDACION# SE VERIFICAN LOS DATOS	
	def validarDatos(self,listData):
		valid=True
		if type(listData) == list:
			for i in listData:
				if i == '':
					valid = False	
		elif type(listData) == dict:
			valid=False
			for i in listData:
				if (listData[i] != '') & (i != 'open'):
					valid=True	
		else:
			if i == ():
					valid=False
		return valid

	#METODOS DE INSTANCIACION# SE CREAN NUEVOS ELEMENTOS	
	def newProducts(self,list_new_products):
		#Declarar cada producto de la lista
		print("Creando nuevos productos: ")			
		for i in list_new_products:
			product = Producto(i)
			self.data_list.append(product)
			print("Agregado")


	#METODOS DE VISUALIZACION DE DATOS#
	def printVector(self,vector):
		strAux="["
		cont=0
		for i in vector:
			strAux+=str(i)
			if cont == len(vector)-1:
				strAux+=" ]"
			else:
				strAux+=" , "	
			cont+=1
		print(strAux)	
	def printMatriz(self,matriz):
		strAux=""
		for i in matriz:
			strAux=""
			for j in i:
				strAux+=str(j)
			print(strAux)		

	#METODOS INDEFINIDOS#
	def setParametro(self, indice ,parametro, valor):			
		for i in self.data_list:
			if i.Indice() == indice:
				if(parametro=='1'):
					#set de codigo
					i.setCodigo(valor)
				elif(parametro=='2'):
					#set de nombre
					i.setNombre(valor)					
				elif(parametro=='3'):
					#set de precio
					print("Cambiando el precio")
					i.setPrecio(valor)
					print("Precio cambiado a:")
					print(i.nombre,"-----",i.codigo,"---->", i.precio)
				elif(parametro=='4'):
					#set de cantidad_0
					i.setCantidad_O(valor)
				elif(parametro=='5'):
					#set de cantidad
					i.setCantidad(valor)

	def setParametroGranel(self, indice):
		for i in self.data_list:
			if i.Indice() == indice:
				if(i.Granel()):
					i.noGranelado()
				else:
					i.granelado()	

	def setTodosLosParametros(self):				
		for i in self.data_list:
			print("Ingrese el nuevo precio para ",i.Nombre(),":\n")
			_precio=input()
			if(_precio=='salir'):break
			i.setPrecio(_precio)

			print("Ingrese la nueva cantidad estimada para ",i.Nombre(),":\n")
			_cantidad_o=input()
			if(_cantidad_o=='salir'):break
			i.setCantidad_O(_cantidad_o)

			print("Ingrese la nueva cantidad actual para ",i.Nombre(),":\n")
			_cantidad=input()
			if(_cantidad=='salir'):break
			i.setCantidad(_cantidad)

			_granel=input("Responda 1 si el producto se vende al granel y 0 en caso contrario.")
			if(_granel=='salir'):break
			if _granel:
				i.granelado(_cantidad_o,_cantidad)
			else:
				i.noGranelado()	

			print(i.Codigo()," - ",i.Nombre()," - ",i.Precio()," - ",i.Cantidad_O()," - ",i.Cantidad()," Granel: ",i.Granel())

	def printListaProductos(self):
		for i in self.data_list:
			print(i.Codigo(),i.Nombre(),i.Precio(),i.Cantidad_O(),i.Indice())
	def printListaBusqueda(self):
		for i in self.search_list:
			print(i.Codigo(),i.Nombre(),i.Precio(),i.Cantidad_O(),i.Indice())		
	def printProducto(indice):
		for i in self.data_list:
			if i.Indice() == indice:
				print("El producto escogido es: ")
				print(i.Codigo()," - ",i.Nombre()," - ",i.Precio()," - ",i.Cantidad_O()," - ",i.Indice())			
	
#CLASE PROVEEDOR: Esta clase se encarga de modelar un proveedor en especifico
class Proveedor(object):
	"""docstring for Proveedores"""
	def __init__(self, value_list):
		super(Proveedor, self).__init__()		
		self.nombre = value_list[0]
		self.nit = value_list[1]
		self.dias = value_list[2]
		self.telefono = value_list[3]
		self.correo=value_list[4]
		self._atributes=value_list		
		
	def busquedaNombre(self, _nombre):
		exist=_nombre.lower() in self.nombre.lower()		
		return exist
	def busquedaNit(self, _nit):
		exist=_nit.lower() in self.nit.lower()		
		return exist		
	def busquedaDias(self, _dias):
		exist=_dias.lower() in self.dias.lower()		
		return exist
	def busquedaTelefono(self, _telefono):
		exist=_telefono.lower() in self.telefono.lower()		
		return exist

	def atributes(self):
		list_=[self.nombre,self.nit,self.dias,self.telefono]
		return list_

	def getNombre(self):
		return self.nombre

#CLASE PRODUCTO: Esta clase se encarga de modelar un producto en especifico
class Producto(object):
	##docstring for Producto
	def __init__(self, list_value ):
		super(Producto, self).__init__()				
		self.codigo=list_value[0] 
		self.nombre=list_value[1]
		self.precio=list_value[2]
		self.cantidad_o=float(list_value[3])
		self.cantidad=float(list_value[4])
		self.rotacion=float(list_value[5])
		self.granel=list_value[6]
		self.proveedor=list_value[7]
		self.porcentaje=20
		self.precio_compra=list_value[2]

	def __init__(self, list_value ):						
		self.porcentaje=20
		self.codigo=list_value[0] 
		self.nombre=list_value[1]
		self.precio_compra=list_value[2]
		self.setPrecioVenta(list_value[2])
		self.cantidad_o=list_value[3]
		self.cantidad=list_value[3]
		self.rotacion=float(0)
		self.granel=list_value[4]

	def atributes(self):
		list_=[self.codigo,self.nombre,self.precio,self.cantidad_o,self.cantidad,self.rotacion,self.granel]
		return list_	

	def busquedaAvanzada(self, _item):
		exist=_item.lower() in self.nombre.lower()		
		return exist

	def coincide(self,listData):
		if listData[0]== self.Codigo():
			if listData[1]==self.Nombre():
				return True	
			else:
				return False		
		else:
			return False			

	def granelado(self,_cantidad):
		self.cantidad +=_cantidad
		self.granel=True

	def noGranelado(self):
		self.granel=False	
								

	##METODOS SET
	def setCodigo(self, codigo):
			self.codigo=codigo
			return self.codigo		
	def setNombre(self, nombre):
		self.nombre=nombre
		return self.nombre	
	def setPrecio(self, item_precio):
			self.precio=item_precio
			return self.precio
	def setCantidad_O(self, cantidad_o):
		self.cantidad_o=cantidad_o
		return self.cantidad_o	
	def setCantidad(self, cantidad):
		self.cantidad=cantidad
	def setProveedor(self,provider):
		self.proveedor = provider	
	
	def plusCantidad(self,cantidad):
		self.setCantidad(self.cantidad+cantidad)
	def minusCantidad(self,cantidad):
		if self.cantidad - float(cantidad) <= 0:
			return False
		else:				
			self.setCantidad(self.cantidad-cantidad)		
			return True

	def calcularRotacion(self,time):
			self.rotacion=(self.cantidad_o-self.cantidad)/time	
			return self.rotacion
	def setPorcentaje(self,porcentaje):
		self.porcentaje=int(porcentaje)		
	def setPrecioVenta(self,precio_compra):
		self.precio_compra=int(precio_compra)
		self.precio=int(self.precio_compra*((self.porcentaje+100)/100))

	def setIn(self,listData,provider):
		if listData[3]:
			self.granelado(float(listData[3]))
		else:
			self.noGranelado()
			self.plusCantidad(float(listData[3]))
		self.setPrecioVenta(int(listData[5]))
		self.setProveedor(provider)
	def setOut(self,cantidad):
		return self.minusCantidad(cantidad)	
				
			

	##METODOS GET		
	def Nombre(self):		
		return self.nombre
	def Codigo(self):		
		return self.codigo
	def Precio(self):		
		return self.precio
	def Cantidad_O(self):		
		return self.cantidad_o
	def Cantidad(self):		
		return self.cantidad	
	def Indice(self):		
		return self.indice
	def Rotacion(self):		
		return self.rotacion
	def Granel(self):		
		return self.granel
	def Porcentaje(self):
		return self.porcentaje
	def PrecioCompra(self):
		return self.precio_compra										

from clases import *


if __name__ == '__main__':
		
	aplication = Menu()

"""

print(aplication.getInfoContainer())
while True:
	

	print("**********************************MENU********************************* ")
	print("1. BUSQUEDA DE PRODUCTOS")
	print("2. MODIFCAR VALORES DE PRODUCTOS")
	print("3. MODIFCAR TODOS LOS VALORES DE LOS PRODUCTOS")
	print("4. SALIR")
	opcion_escogida=input("\n")

	if opcion_escogida=='1':
		item=input("INGRESE EL NOMBRE DEL PRODUCTO QUE DESEA BUSCAR \n")
		aplication.aplication.getInfoContainer().searchProducto(item)
		if(item.lower()=='salir'):
			break	

	elif opcion_escogida=='2':	
		item=input("INGRESE EL NOMBRE DEL PRODUCTO 	QUE DESEA MODIFICAR \n")
		aplication.getInfoContainer().searchProducto(item)
		if(item.lower()=='salir'):
			break
		n_selected=input("ECOJA UNO DE LOS PRODUCTOS ENUMERADOS: \n\n")
		if(n_selected=='salir'):
			break
		else:

			indice_escogido=aplication.getInfoContainer().selectProducto(n_selected)

			print("Que Desea Hacer?: ")
			print("1. Cambiar el codigo")
			print("2.Cambiar el nombre?")
			print("3.Cambiar el precio?")
			print("4.Cambiar la Cantidad Estimada?")
			print("5.Cambiar el Cantidad Actual")
			print("6.Cambiar el modo de compra y venta del producto")
			opc=input("\n¡¡Ingrese Salir para salir del programa o Continuar para cancelar la operacion!!\n")

			if(opc=='1'):
				##FUNCION ENCARGADA DE CAMBIAR UN PARAMETRO DEL DATAFRAME 
				##FUNCION ENCARGADA DE save EL NUEVO DATAFRAME
				_codigo=input("Ingrese el nuevo Codigo\n")
				aplication.getInfoContainer().setParametro(indice_escogido,opc,_codigo)
			elif(opc=='2'):					
				##FUNCION ENCARGADA DE CAMBIAR UN PARAMETRO DEL DATAFRAME 
				##FUNCION ENCARGADA DE save EL NUEVO DATAFRAME
				_nombre=input("Ingrese el nuevo Nombre\n")
				aplication.getInfoContainer().setParametro(indice_escogido,opc,_nombre)
			elif(opc=='3'):	
				##FUNCION ENCARGADA DE CAMBIAR UN PARAMETRO DEL DATAFRAME 
				##FUNCION ENCARGADA DE save EL NUEVO DATAFRAME				
				_precio=input("Ingrese el nuevo Precio\n")
				aplication.getInfoContainer().setParametro(indice_escogido,opc,_precio)
			elif(opc=='4'):	
				##FUNCION ENCARGADA DE CAMBIAR UN PARAMETRO DEL DATAFRAME 
				##FUNCION ENCARGADA DE save EL NUEVO DATAFRAME				
				_cantidad_o=input("Ingrese la nueva Cantidad Estimada")
				aplication.getInfoContainer().setParametro(indice_escogido,opc,_cantidad_o)
			elif(opc=='5'):	
				##FUNCION ENCARGADA DE CAMBIAR UN PARAMETRO DEL DATAFRAME 
				##FUNCION ENCARGADA DE save EL NUEVO DATAFRAME				
				_cantidad=input("Ingrese la nueva Cantidad Actual\n")
				aplication.getInfoContainer().setParametro(indice_escogido,opc,_cantidad)
			elif(opc=='6'):	
				##FUNCION ENCARGADA DE CAMBIAR UN PARAMETRO DEL DATAFRAME 
				##FUNCION ENCARGADA DE save EL NUEVO DATAFRAME				
				aplication.getInfoContainer().setParametroGranel(indice_escogido)			
			elif(opc=='salir'):
				break
			elif(opc=='continuar'):
				continue	

			else:
				print("Opcion no disponible")	
	
	elif opcion_escogida=='3':
		aplication.getInfoContainer().setTodosLosParametros()

	elif opcion_escogida=='4':
	    break				
	else:
		print("Opcion no Valida")    
""" 
#aplication.getInfoContainer().save()
#aplication.getInfoContainer().saveVenta()
print("SALIENDOOOO.......")


	
		
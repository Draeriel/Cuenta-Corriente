import time

def validacion():
	nombre = str(input("Introduzca su nombre: "))
	apellidos = str(input("Introduzca sus apellidos: "))
	cliente = (nombre + " " + apellidos).replace(" ", "_")
	rutaAccesoFichero = "./" + str(cliente) + ".txt"
	datos = [nombre, apellidos]
	return accesoDatos(rutaAccesoFichero, nombre, apellidos, datos)


def accesoDatos(rutaAccesoFichero, nombre, apellidos, datos):
	try:
		assert isinstance(rutaAccesoFichero, str)
		fichero = open(rutaAccesoFichero, 'r')
		fichero.close()    
	except FileNotFoundError:
		error = 0
		seguir = True
		while seguir:
			if error == 0:
				blank = str(input("No se han encontrado sus datos. ¿Desea volver a intentarlo? S/N: "))
			elif error == 1:
				blank = str(input("Lo sentimos, pero no hemos entendido su petición. Por favor, introduzca solo S o N: "))	
			if blank == "S":
				return validacion()
			elif blank == "N":
				error = 0
				while seguir:
					if error == 0:
						nuevoCliente = str(input("¿Desea crear una nueva cuenta con nosotros? S/N: "))
					elif error == 1:
						nuevoCliente = str(input("Lo sentimos, pero no hemos entendido su petición. Por favor, introduzca solo S o N: "))
					if nuevoCliente == "S" :
						abrirCuenta(rutaAccesoFichero, nombre, apellidos, datos)
						seguir = False
					elif nuevoCliente == "N":
						print("Entendemos que es una decisión difícil. Si cambia de opinión, estaremos encantados de volver a atenderle.")
						seguir = False
					else:
						error = 1			
			else:
				error = 1
	
	
	return ultimaSesion(rutaAccesoFichero)	

					
def abrirCuenta(rutaAccesoFichero, nombre, apellidos, datos):	
	print("Para la creacion de la nueva cuenta serán necesarios sus datos personales.")
	time.sleep(2)
	dentro = True
	error = 0
	while dentro:		
		try:
			if error == 0:
				direccion = str(input("Por favor, introduzca su dirección (no utilice comas): "))
			else:
				direccion = str(input("La dirección introducida no es válida. Por favor, introduzca una dirección válida (no utilice comas): "))	
			assert isinstance(direccion, str)
			assert ("," not in direccion)
		except AssertionError:
			error = 1
		else:
			datos.append(direccion)
			dentro = False
	error = 0			
	while not dentro:
		try:
			if error == 0:
				telefono = str(input("Introduzca su número de teléfono: "))
			else:
				telefono = str(input("El número introducido no coincide con ningún teléfono. Indroduzca un número válido: "))	
			assert isinstance(telefono, str)
			assert (len(telefono) == 9)
		except AssertionError:
			error = 1
		else:
			datos.append(telefono)
			dentro = True
	error = 0			
	while dentro:
		try:
			if error == 0:			
				nif = str(input("Introduzca su número de DNI: "))
			else:
				nif = str(input("El número introducido no es válido. Por favor, inténtelo de nuevo: "))	
			assert isinstance(nif, str)
			assert (len(nif) == 9)
			assert (nif.isalnum())
			numeros = [numero for numero in nif]
			letra = numeros.pop()
			assert (letra.isalpha())
			numeros = "".join(numeros)
			assert (numeros.isdigit())

		except AssertionError:
			error = 1
		else:
			datos.append(nif)
			dentro = False
	datos.append("0")
	nuevaCuenta = open(rutaAccesoFichero, 'w')
	nuevaCuenta.write("Nombre, Apellidos, Dirección, Teléfono, NIF, Saldo" )
	fichero.write("\n" + time.strftime("%d/%m/%Y") + "     " + time.strftime("%H:%M:%S") + "     Creación de una nueva cuenta")
	nuevaCuenta.write("\n" + ", ".join(datos))	
	nuevaCuenta.close()
	ultimaSesion(rutaAccesoFichero)


def ultimaSesion(rutaAccesoFichero):
	fichero = open(rutaAccesoFichero, 'r')
	historial = [linea for linea in fichero]
	fichero.close()
	lista = []
	colector = ""
	actual = historial[-1]
	for dato in range(len(actual)):
		if actual[dato] == " " and actual[dato -1] == ",":
			pass
		elif actual[dato] != ",":
			colector += actual[dato]
		elif actual[dato] == "," and actual[dato +1] == " ":
			lista.append(colector)
			colector = ""
	colector = float(colector)				
	lista.append(colector)
	return lista


def transacciones(actual):
	cliente = (actual.nombre + " " + actual.apellidos).replace(" ", "_")
	rutaAccesoFichero = "./" + str(cliente) + ".txt"
	fichero = open(rutaAccesoFichero, "a")
	tramites = True
	while tramites:
		accion = input("¿Qué desea hacer? 1.Retirar dinero, 2.Ingresar dinero, 3.Consultar cuenta, 4.Nada más: ")
		if accion == "1":
			abheben = True
			while abheben:
				try:
					retirar = float(input("¿Cuánto dinero quieres retirar?: "))
					actual.retirarDinero(retirar)
					fichero.write("\n" + time.strftime("%d/%m/%Y") + "   " + time.strftime("%H:%M:%S") + f"     Se han extraído {retirar}€.")
				except TypeError:
					print("Por favor, introduzca solo números.")
					time.sleep(1)
				else:
					print(f"Usted ha retirado {retirar}€.")
					abheben = False
					tramites = False

		elif accion == "2":
			ueberweisen = True
			while ueberweisen:
				try:
					ingresar = float(input("¿Cuánto dinero quieres ingresar?: "))
					actual.ingresarDinero(ingresar)
					fichero.write("\n" + time.strftime("%d/%m/%Y") + "   " + time.strftime("%H:%M:%S") + f"     Se han ingresado {ingresar}€.")
				except TypeError:
					print("Por favor, introduzca solo números.")
					time.sleep(1)
				else:
					print(f"Usted ha ingresado {ingresar}€.")
					ueberweisen = False
					tramites = False
						
		elif accion == "3":
			print(f"Su saldo actual es de {actual.consultarCuenta()}€")
			fichero.write("\n" + time.strftime("%d/%m/%Y") + "   " + time.strftime("%H:%M:%S") + f"     Se ha consultado la cuenta.")
			tramites = False

		elif accion == "4":
			print("Gracias por confiar en nosotros, hasta la próxima.")
			break	

		else:
			print("Por favor, introduzca solo un número.")
			print("Para retirar diner, pulse 1.")
			print("Para ingresar dinero, pulse 2.")
			print("Para consultar el estado de su cuenta, pulse 3.")
			print("Si no desea hacer ningún trámite, pulse 4.")	
				
		fichero.write("\n" + str(actual.getDatosCompletos()))
		fichero.close()

class CuentaCorriente:

	def __init__(self, nombre, apellidos, direccion, telefono, nif, saldo):
		self.nombre = nombre
		self.apellidos = apellidos
		self. direccion = direccion
		self.telefono = telefono
		self.nif = nif
		self.saldo = saldo

	def __repr__(self):
		return "%s, %s, %s, %s, %s, %s" % (self.nombre, self.apellidos, self.direccion, self.telefono, self.nif, self.saldo)


class Interfaz():

	def consultarCuenta():
		pass


class DatosPersonales(CuentaCorriente, Interfaz):

	def __init__(self, nombre, apellidos, direccion, telefono, nif, saldo):
		CuentaCorriente.__init__(self, nombre, apellidos, direccion, telefono, nif, saldo)

	def setNombre(self, nombre): 
		assert isinstance(self.nombre, str)
	
	def setApellidos(self, apellidos):
		assert isinstance(self.apellidos, str)

	def getNombreCompleto(self):
		self.setNombre(self.nombre)
		self.setApellidos(self.apellidos)
		return self.nombre + " " + self.apellidos

	def setDireccion(self, direccion):
		assert isinstance(self.direccion, str)
		
	def getDireccion(self):
		self.setDireccion(self.direccion)	
		return self.direccion

	def setTelefono(self, telefono):
		assert isinstance(self.telefono, str)
		try:
			telefono = int(telefono)
		except ValueError:
			raise "Se han encontrado carácteres no numéricos."

	def getTelefono(self):
		self.setTelefono(self.telefono)
		return self.telefono

	def setNif(self, nif):
		assert isinstance(self.nif, str)
		assert (len(self.nif) == 9)
		assert (self.nif.isalnum())
		numeros = [numero for numero in self.nif]
		letra = numeros.pop()
		assert (letra.isalpha())
		numeros = "".join(numeros)
		assert (numeros.isdigit())
		
	def getNif(self):
		self.setNif(self.nif)
		return self.nif	

	def setSaldo(self, saldo):
		assert isinstance(self.saldo, float)

	def getSaldo(self, valor):
		self.setSaldo(self.saldo)
		self.saldo += valor
		return self.saldo	

	def getDatosCompletos(self):
		return self	



class Transacciones(DatosPersonales):
	def __init__(self, nombre, apellidos, direccion, telefono, nif, saldo):
		CuentaCorriente.__init__(self, nombre, apellidos, direccion, telefono, nif, saldo)

	def retirarDinero(self, retirar):
		self.getSaldo(-retirar)
		return self.saldo

	def ingresarDinero(self, ingresar):
		self.getSaldo(ingresar)
		return self.saldo

	def consultarCuenta(self):
		return self.getSaldo(0)

	def saldoNegativo(self):
		if self.saldo > 0:
			return  "Tu saldo es positivo."
		elif self.saldo == 0:
			return "No tienes saldo."	
		else:
			return "Tu saldo es negativo."	
from cuentaCorriente import *
from accesoDatos import *

if __name__ == "__main__":
	try:
		actual = Transacciones(*validacion())
	except TypeError:
		pass
	else:	
		print(f"Su saldo actual es de {actual.consultarCuenta()}€")
		transacciones(actual)	
	
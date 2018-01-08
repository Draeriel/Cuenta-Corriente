from cuentaCorriente import *
from accesoDatos import *

if __name__ == "__main__":
	actual = Transacciones(*validacion())
	print(f"Su saldo actual es de {actual.consultarCuenta()}€")
	transacciones(actual)	
	
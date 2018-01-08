from cuentaCorriente import *
if __name__ == "__main__":
	cliente = DatosPersonales("Harry", "Potter", "4 Privet Drive", "911234534", "98666124B", 1265625.83)
	print("Nombre completo: " + cliente.getNombreCompleto())
	print("Dirección: " + cliente.getDireccion())
	print("Número de teléfono: " + cliente.getTelefono())
	print("NIF: " + cliente.getNif())
	print(f"Saldo actual: {cliente.getSaldo(0)}")

	cuenta = Transacciones("Harry", "Potter", "4 Privet Drive", "911234534", "98666124B", 1265625.83)
	print(cuenta.retirarDinero(10))
	print(cuenta.ingresarDinero(1))
	print(cuenta.consultarCuenta())
	print(cuenta.saldoNegativo())
	
	
class Cuenta:
    def __init__(self, numero_cuenta, cliente, saldo_inicial=0):
        self.__numero_cuenta = numero_cuenta
        self.__cliente = cliente
        self.__saldo = saldo_inicial



    # ======= Getters y Setters =======
    def get_numero_cuenta(self):
        return self.__numero_cuenta

    def get_saldo(self):
        return self.__saldo

    def get_cliente(self):
        return self.__cliente

    def set_saldo(self, nuevo_saldo):
        self.__saldo = nuevo_saldo

    # ======= Métodos principales =======
    def depositar(self, monto):
        """Agrega dinero a la cuenta"""
        try:
            if monto <= 0:
                raise ValueError("El monto debe ser positivo.")
            self.__saldo += monto
            print(f"💰 Depósito exitoso. Nuevo saldo: ${self.__saldo}")
        except ValueError as e:
            print(f"Error: {e}")

    def retirar(self, monto):
        """Extrae dinero de la cuenta"""
        try:
            if monto <= 0:
                raise ValueError("El monto debe ser positivo.")
            if monto > self.__saldo:
                raise ValueError("Fondos insuficientes.")
            self.__saldo -= monto
            print(f"🏧 Retiro exitoso. Saldo actual: ${self.__saldo}")
        except ValueError as e:
            print(f"Error: {e}")


              # Mostrar datos
    def mostrar_datos(self):
        print("\n=== DATOS DEL CLIENTE ===")
        print(f"Nombre: {self.__nombre}")
        print(f"Apellido: {self.__apellido}")
        print(f"DNI: {self.__dni}")
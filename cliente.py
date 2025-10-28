class Cliente:
    def _init_(self, nombre, apellido, dni):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni

    # Getters y setters ----------------------------------------------------------
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        else:
            self.__nombre = nuevo_nombre

    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, nuevo_apellido):
        if not nuevo_apellido.strip():
            raise ValueError("El apellido no puede estar vacío.")
        else:
            self.__apellido = nuevo_apellido

    def get_dni(self):
        return self.__dni
        if not nuevo_dni.strip():
            raise ValueError("El DNI no puede estar vacío.")
        else:
            self.__dni = nuevo_dni

    def set_dni(self, nuevo_dni):
        if len(str(nuevo_dni)) < 7:
            print("El DNI debe tener al menos 7 caracteres.")
        else:
            self.__dni = nuevo_dni

    # Mostrar datos del cliente ------------------------------------------------
    def mostrar_datos(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Apellido: {self.__apellido}")
        print(f"DNI: {self.__dni}")

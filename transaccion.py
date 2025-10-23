from datetime import datetime
from typing import List, Tuple


class Transaccion:
    def __init__(self, tipo: str, monto: float):
        self.__tipo = tipo
        self.__monto = float(monto)
        self.__fecha = datetime.now()

    def get_tipo(self) -> str:
        return self.__tipo

    def set_tipo(self, tipo: str) -> None:
        self.__tipo = str(tipo)

    def get_monto(self) -> float:
        return self.__monto

    def set_monto(self, monto: float) -> None:
        self.__monto = float(monto)
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero.")
        self.__monto = float(monto)

    def get_fecha(self) -> datetime:
        return self.__fecha

    def set_fecha(self, fecha: datetime) -> None:
        self.__fecha = datetime(fecha)

    # Polimorfismo: cada subclase define cómo se aplica --------------------
    def aplicar(self, cuenta) -> None:
        raise NotImplementedError(
            "Este método debe ser implementado por las subclases."
        )

    def __str__(self) -> str:
        signo = "+" if self.__monto > 0 else "-"
        return f"{self.__fecha:%Y-%m-%d %H:%M:%S} | {self.__tipo}: {signo}${abs(self.__monto):.2f}"


class Deposito(Transaccion):

    def __init__(self, monto: float):
        super().__init__("Depósito", monto)

    def aplicar(self, cuenta) -> None:
        # Sube el saldo actual por el monto del depósito
        nuevo = cuenta.get_saldo() + self.get_monto()
        cuenta.set_saldo(nuevo)


class Retiro(Transaccion):
    # Disminuye el saldo actual por el monto del retiro
    def __init__(self, monto: float):
        super().__init__("Retiro", monto)

    def aplicar(self, cuenta) -> None:
        # Aca debe verificar los fondos antes de retirar
        if self.get_monto() > cuenta.get_saldo():
            raise ValueError("Fondos insuficientes.")

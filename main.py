from cliente import Cliente
from cuenta import Cuenta
from transaccion import Transaccion
from fpdf import FPDF

clientes = []
cuentas = []
transacciones = []
contador_cuentas = 1000


def crear_cliente():
    global contador_cuentas
    print("\n🆕 Crear nuevo cliente")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")

    cliente = Cliente(nombre, apellido, dni)
    clientes.append(cliente)

    contador_cuentas += 1
    cuenta = Cuenta(numero_cuenta=contador_cuentas, cliente=cliente, saldo_inicial=0)
    cuentas.append(cuenta)

    print(f"\n✅ Cliente y cuenta creados con éxito.")
    print(f"Cuenta Nº {cuenta.numero_cuenta} asociada a {cliente.nombre} {cliente.apellido}.\n")


def listar_clientes():
    if not clientes:
        print("\n⚠️ No hay clientes registrados.\n")
        return
    print("\n📋 Lista de clientes:")
    for i, c in enumerate(clientes, start=1):
        print(f"{i}. {c}")
    print("")


def listar_cuentas():
    if not

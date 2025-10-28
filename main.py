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
    if not cuentas:
        print("\n⚠️ No hay cuentas registradas.\n")
        return
    print("\n🏦 Lista de cuentas:")
    for c in cuentas:
        print(c)
    print("")


def exportar_pdf():
    if not clientes:
        print("\n⚠️ No hay clientes para exportar.\n")
        return

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="📋 Lista de Clientes del Banco", ln=True, align="C")

    pdf.set_font("Arial", size=12)
    for c in clientes:
        pdf.cell(200, 10, txt=f"{c.nombre} {c.apellido} - DNI: {c.dni}", ln=True)

    pdf.output("clientes_banco.pdf")
    print("\n📄 Archivo 'clientes_banco.pdf' generado con éxito.\n")


def buscar_cuenta_por_numero(numero):
    for c in cuentas:
        if c.numero_cuenta == numero:
            return c
    return None


def realizar_transaccion():
    print("""
============================
💸 TRANSACCIONES
============================
1️⃣ Depósito
2️⃣ Retiro
3️⃣ Transferencia
============================
""")
    opcion = input("Seleccioná una opción: ")

    if opcion == "1":
        numero = int(input("Número de cuenta destino: "))
        cuenta = buscar_cuenta_por_numero(numero)
        if not cuenta:
            print("❌ Cuenta no encontrada.")
            return
        monto = float(input("Monto a depositar: "))
        print(cuenta.depositar(monto))
        transacciones.append(Transaccion("depósito", monto, destino=cuenta))

    elif opcion == "2":
        numero = int(input("Número de cuenta origen: "))
        cuenta = buscar_cuenta_por_numero(numero)
        if not cuenta:
            print("❌ Cuenta no encontrada.")
            return
        monto = float(input("Monto a retirar: "))
        print(cuenta.retirar(monto))
        transacciones.append(Transaccion("retiro", monto, origen=cuenta))

    elif opcion == "3":
        origen_num = int(input("Cuenta origen: "))
        destino_num = int(input("Cuenta destino: "))
        monto = float(input("Monto a transferir: "))

        origen = buscar_cuenta_por_numero(origen_num)
        destino = buscar_cuenta_por_numero(destino_num)

        if not origen or not destino:
            print("❌ Alguna de las cuentas no existe.")
            return

        print(origen.transferir(destino, monto))
        transacciones.append(Transaccion("transferencia", monto, origen=origen, destino=destino))
    else:
        print("❌ Opción inválida.")


def mostrar_transacciones():
    if not transacciones:
        print("\n📭 No hay transacciones registradas.\n")
        return
    print("\n📜 HISTORIAL DE TRANSACCIONES:\n")
    for t in transacciones:
        print(t)
    print("")


def menu():
    while True:
        print("""
=============================
🏦 BANCO INTERACTIVO
=============================
1️⃣ Crear cliente
2️⃣ Listar clientes
3️⃣ Listar cuentas
4️⃣ Exportar clientes a PDF
5️⃣ Transacciones
6️⃣ Ver historial
7️⃣ Salir
""")

        opcion = input("Seleccioná una opción: ")

        if opcion == "1":
            crear_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            listar_cuentas()
        elif opcion == "4":
            exportar_pdf()
        elif opcion == "5":
            realizar_transaccion()
        elif opcion == "6":
            mostrar_transacciones()
        elif opcion == "7":
            print("\n👋 Saliendo del sistema bancario...\n")
            break
        else:
            print("\n❌ Opción inválida. Probá otra vez.\n")


if __name__ == '__main__':
    menu()


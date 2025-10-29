from cliente import Cliente
from cuenta import Cuenta
from transaccion import Deposito, Retiro  # usamos subclases concretas
from fpdf import FPDF

clientes = []
cuentas = []
transacciones = []
contador_cuentas = 1000


def crear_cliente():
    global contador_cuentas
    print("\n🆕 Crear nuevo cliente")
    try:
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        dni = input("DNI: ").strip()
        if not nombre or not apellido or not dni:
            raise ValueError("Todos los campos son obligatorios.")

        cliente = Cliente(nombre, apellido, dni)
        clientes.append(cliente)

        contador_cuentas += 1
        cuenta = Cuenta(
            numero_cuenta=contador_cuentas, cliente=cliente, saldo_inicial=0
        )
        cuentas.append(cuenta)

        print("\n✅ Cliente y cuenta creados con éxito.")
        print(
            f"Cuenta Nº {cuenta.get_numero_cuenta()} asociada a "
            f"{cliente.get_nombre()} {cliente.get_apellido()}.\n"
        )
    except ValueError as e:
        print(f"⚠️ Error: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


def listar_clientes():
    if not clientes:
        print("\n⚠️ No hay clientes registrados.\n")
        return
    print("\n📋 Lista de clientes:")
    for i, c in enumerate(clientes, start=1):
        print(f"{i}. {c.get_apellido()}, {c.get_nombre()} (DNI: {c.get_dni()})")
    print("")


def listar_cuentas():
    if not cuentas:
        print("\n⚠️ No hay cuentas registradas.\n")
        return
    print("\n🏦 Lista de cuentas:")
    for c in cuentas:
        cli = c.get_cliente()
        print(
            f"N° {c.get_numero_cuenta()} | Titular: {cli.get_apellido()}, {cli.get_nombre()} | Saldo: ${c.get_saldo():.2f}"
        )
    print("")


def exportar_pdf():
    if not cuentas:
        print("\n⚠️ No hay cuentas para exportar.\n")
        return

    try:
        pdf = FPDF()
        pdf.add_page()

        # Título
        pdf.set_font("Helvetica", style="B", size=14)
        pdf.cell(
            w=0,
            h=10,
            text="Lista de Cuentas del Banco",
            new_y="NEXT",
            new_x="LMARGIN",
            align="C",
        )

        # Cuerpo
        pdf.set_font("Helvetica", size=12)
        for cuenta in cuentas:  # <-- iteramos CUENTAS
            cli = cuenta.get_cliente()  # <-- obtenemos el Cliente de esa cuenta
            linea = (
                f"{cli.get_nombre()} {cli.get_apellido()} "
                f"- DNI: {cli.get_dni()} "
                f"- Cuenta N°: {cuenta.get_numero_cuenta()} "
                f"- Saldo: ${cuenta.get_saldo():.2f}"
            )
            pdf.cell(w=0, h=8, text=linea, new_y="NEXT", new_x="LMARGIN")

        pdf.output("cuentas_banco.pdf")
        print("\n📄 Archivo 'cuentas_banco.pdf' generado con éxito.\n")

    except Exception as e:
        print(f"❌ No se pudo generar el PDF: {e}")


def buscar_cuenta_por_numero(numero):
    for c in cuentas:
        if c.get_numero_cuenta() == numero:
            return c
    return None


def realizar_transaccion():
    print(
        """
============================
💸 TRANSACCIONES
============================
1️⃣ Depósito
2️⃣ Retiro
============================
"""
    )
    opcion = input("Seleccioná una opción: ").strip()

    try:
        if opcion == "1":
            numero = int(input("Número de cuenta destino: "))
            cuenta = buscar_cuenta_por_numero(numero)
            if not cuenta:
                print("❌ Cuenta no encontrada.")
                return
            monto = float(input("Monto a depositar: "))
            t = Deposito(monto)  # valida monto > 0
            t.aplicar(cuenta)  # usa get_saldo/set_saldo de Cuenta
            transacciones.append(t)  # arreglo en memoria (consigna)
            print(f"✅ Depósito exitoso. Saldo: ${cuenta.get_saldo():.2f}")

        elif opcion == "2":
            numero = int(input("Número de cuenta: "))
            cuenta = buscar_cuenta_por_numero(numero)
            if not cuenta:
                print("❌ Cuenta no encontrada.")
                return
            monto = float(input("Monto a retirar: "))
            t = Retiro(monto)  # valida monto > 0
            t.aplicar(cuenta)  # puede lanzar 'Fondos insuficientes'
            transacciones.append(t)
            print(f"✅ Retiro exitoso. Saldo: ${cuenta.get_saldo():.2f}")

        else:
            print("❌ Opción inválida.")
    except ValueError as e:
        print(f"⚠️ Error: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


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
        print(
            """
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
"""
        )

        opcion = input("Seleccioná una opción: ").strip()

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


if __name__ == "__main__":
    menu()
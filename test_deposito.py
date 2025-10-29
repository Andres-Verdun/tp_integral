# test_deposito.py
from cliente import Cliente
from cuenta import Cuenta
from main import cuentas, clientes, transacciones, depositar_en_cuenta_por_parametros


def setup_function():
    # limpiar arreglos para que cada test empiece limpio
    clientes.clear()
    cuentas.clear()
    transacciones.clear()


def test_deposito_ok():
    cli = Cliente("Ana", "Perez", "12345678")
    clientes.append(cli)
    cta = Cuenta(numero_cuenta=1001, cliente=cli, saldo_inicial=100.0)
    cuentas.append(cta)

    ok, msg = depositar_en_cuenta_por_parametros(1001, 50.0)

    assert ok is True
    assert cta.get_saldo() == 150.0
    assert len(transacciones) == 1


def test_deposito_cuenta_inexistente():
    ok, msg = depositar_en_cuenta_por_parametros(9999, 10)
    assert ok is False
    assert "Cuenta no encontrada" in msg


def test_deposito_monto_invalido():
    # monto <= 0 debe fallar
    cli = Cliente("Juan", "Gomez", "11111111")
    clientes.append(cli)
    cta = Cuenta(numero_cuenta=2002, cliente=cli, saldo_inicial=0)
    cuentas.append(cta)

    ok, msg = depositar_en_cuenta_por_parametros(2002, 0)
    assert ok is False
    assert "mayor que cero" in msg

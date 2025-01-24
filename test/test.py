from src.tablaAsignacion import TablaAsignacion

def test_initialization():
    tabla = TablaAsignacion()
    expected = [
        "T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z",
        "S", "Q", "V", "H", "L", "C", "K", "E"
    ]
    assert tabla.getTabla() == expected

def test_getTabla():
    tabla = TablaAsignacion()
    expected = [
        "T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z",
        "S", "Q", "V", "H", "L", "C", "K", "E"
    ]
    assert tabla.getTabla() == expected

def test_getLetra_valid_position():
    tabla = TablaAsignacion()
    assert tabla.getLetra(0) == "T"
    assert tabla.getLetra(22) == "E"

def test_getLetra_invalid_position():
    tabla = TablaAsignacion()
    assert tabla.getLetra(30) == "Posicion letra fuera de rango"

def test_getModulo():
    tabla = TablaAsignacion()
    assert tabla.getModulo() == 23

def test_isLetraPermitida():
    tabla = TablaAsignacion()
    assert tabla.isLetraPermitida("T") == True
    assert tabla.isLetraPermitida("I") == False

def test_calcularLetra():
    tabla = TablaAsignacion()
    assert tabla.calcularLetra("78484464") == "T"
    assert tabla.calcularLetra("72376173") == "A"
    assert tabla.calcularLetra("01817200") == "Q"
from src.dni import Dni

def test_initialization():
    dni = Dni("12345678Z")
    assert dni.getDni() == "12345678Z"
    assert not dni.getNumeroSano()
    assert not dni.getLetraSana()

def test_set_get_dni():
    dni = Dni()
    dni.setDni("87654321X")
    assert dni.getDni() == "87654321X"

def test_set_get_numero_sano():
    dni = Dni()
    dni.setNumeroSano(True)
    assert dni.getNumeroSano()

def test_set_get_letra_sana():
    dni = Dni()
    dni.setLetraSana(True)
    assert dni.getLetraSana()

def test_check_cif():
    dni = Dni("78484464T")
    assert dni.checkCIF()

def test_check_dni():
    dni = Dni("78484464T")
    assert dni.checkDni()

def test_check_letra():
    dni = Dni("78484464T")
    dni.checkDni()
    assert dni.checkLetra()

def test_obtener_letra():
    dni = Dni("78484464T")
    dni.checkDni()
    assert dni.obtenerLetra() == "T"

def test_check_longitud():
    dni = Dni("78484464T")
    assert dni.checkLongitud()

def test_check_numero():
    dni = Dni("78484464T")
    assert dni.checkNumero()

def test_check_letra_valida():
    dni = Dni("78484464T")
    dni.checkDni()
    assert dni.checkLetraValida()

def test_get_parte_alfabetica_dni():
    dni = Dni("78484464T")
    assert dni.getParteAlfabeticaDni() == "T"

def test_get_parte_numerica_dni():
    dni = Dni("78484464T")
    dni.checkDni()
    assert dni.getParteNumericaDni() == "78484464"
from src.dni import Dni

def test_validar_longitud():
    assert Dni('41569305').checkNumero() == True
    assert Dni('41567873829305').checkNumero() == False
    assert Dni('41567').checkNumero() == False


# def test_validar_formato():
#     assert Dni('41569305').validar_formato() == True
#     assert Dni('41567873829305').validar_formato() == False
#     assert Dni('41567').validar_formato() == False
#     assert Dni('41567fff').validar_formato() == False
#     assert Dni('abcdefgh').validar_formato() == False




# def test_calcular_letra():
#     assert Dni('41509405').calcular_letra() == 'V'
#     assert Dni('72376173').calcular_letra() == 'A'
#     assert Dni('01817200').calcular_letra() == 'Q'
#     assert Dni('95882054').calcular_letra() == 'E'
#     assert Dni('63587725').calcular_letra() == 'Q'
#     assert Dni('26861694').calcular_letra() == 'V'
#     assert Dni('66714505').calcular_letra() == 'S'
#     assert Dni('76857238').calcular_letra() == 'R'
#     assert Dni('80117501').calcular_letra() == 'Z'
#     assert Dni('40135330').calcular_letra() == 'P'
#     assert Dni('66499420').calcular_letra() == 'A'
#     assert Dni('26868974').calcular_letra() == 'Y'


# def test_añadir_letra():
#     assert Dni('41509405').añadir_letra() == '41509405V'
#     assert Dni('72376173').añadir_letra() == '72376173A'
#     assert Dni('01817200').añadir_letra() == '01817200Q'
#     assert Dni('95882054').añadir_letra() == '95882054E'
#     assert Dni('63587725').añadir_letra() == '63587725Q'
#     assert Dni('26861694').añadir_letra() == '26861694V'
#     assert Dni('66714505').añadir_letra() == '66714505S'
#     assert Dni('76857238').añadir_letra() == '76857238R'
#     assert Dni('80117501').añadir_letra() == '80117501Z'
#     assert Dni('40135330').añadir_letra() == '40135330P'
#     assert Dni('66499420').añadir_letra() == '66499420A'
#     assert Dni('26868974').añadir_letra() == '26868974Y'






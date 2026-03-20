import pytest 
from escola import verificador_media

def test_string_como_entrada():
    with pytest.raises(TypeError, match="Tipo inválido, a entrada deve ser numérica"):
        verificador_media("OITO")

def test_menor_que_0_como_entrada():
    with pytest.raises(ValueError, match="O valor deve ser maior ou igual a 10"):
        verificador_media("-5")

def test_maior_que_10_como_entrada():
    with pytest.raises(ValueError, match="O valor deve ser maior ou igual a 10"):
        verificador_media("43423")






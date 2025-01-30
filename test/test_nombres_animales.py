import allure

from src.animales import obtener_nombres_animales 

@allure.description("Test donde se devuelve una lista de nombresdeanimales")
@allure.feature("Animales")
@allure.epic("Lista de nombres")

def test_obtener_nombres ():
    nombres = obtener_nombres_animales()
    assert isinstance(nombres, list)

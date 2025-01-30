import allure

from src.operaciones import  sumar,restar

@allure.description("Test donde se calcula suma y resta")
@allure.feature("Sumar y Restar")
@allure.epic("Calculo de Suma y Resta")


def test_sumar (): 
    resultado = sumar(2,2)
    assert resultado == 4


def test_restar ():
    resultado = restar (2,2)
    assert resultado == 0
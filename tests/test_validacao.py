import pytest
from src.servico.validacao import validar_senha

def test_senha_com_menos_de_8_caracteres():
    senha = "Ab1$xy"  # 6 caracteres
    resultado = validar_senha(senha)
    assert not resultado

def test_senha_sem_maiuscula():
    senha = "abc123$%"  
    resultado = validar_senha(senha)
    assert not resultado, "Senhas sem letra maiúscula devem ser inválidas"


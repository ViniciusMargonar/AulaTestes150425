# tests/test_validacao.py

import pytest
from src.servico.validacao import validar_senha

def test_senha_com_menos_de_8_caracteres():
    senha = "Ab1$xy"  # 6 caracteres
    resultado = validar_senha(senha)
    assert not resultado

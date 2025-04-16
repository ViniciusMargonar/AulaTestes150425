def validar_senha(senha: str) -> bool:
    if not verificar_tamanho_minimo(senha):
        return False
    if not verificar_maiuscula(senha):
        return False
    return True


def verificar_tamanho_minimo(senha: str) -> bool:
    return len(senha) >= 8


def verificar_maiuscula(senha: str) -> bool:
    for caractere in senha:
        if caractere.isupper():
            return True
    return False

# Testes de Software

## Mínimo de 8 caracteres

### 🔴 RED
  
```python
def validar_senha(senha: str) -> bool:
    return True 

 def test_senha_com_menos_de_8_caracteres():
    senha = "Ab1$xy"  # 6 caracteres
    resultado = validar_senha(senha)
    assert not resultado # Espera um false
```
![image](https://github.com/user-attachments/assets/1a797bc8-21d0-4ce0-8fb9-7548017a68c7)

### 🟢 GREEN

```python
def validar_senha(senha: str) -> bool:
    if len(senha) < 8:
        return False
    return True

def validar_senha(senha: str) -> bool:
    if len(senha) < 8:
        return False
    return True
```
![image](https://github.com/user-attachments/assets/38821b7a-61a9-4c8c-a73b-b8a77e33241d)

### 🔵 REFACTOR

```python
def validar_senha(senha: str) -> bool:
    if not verificar_tamanho_minimo(senha):
        return False

    return True


def verificar_tamanho_minimo(senha: str) -> bool:
    return len(senha) >= 8
```
## Pelo menos uma letra maiúscula

### 🔴 RED

```python
def validar_senha(senha: str) -> bool:
    if not verificar_tamanho_minimo(senha):
        return False

    return True

def verificar_tamanho_minimo(senha: str) -> bool:
    return len(senha) >= 8
def test_senha_sem_maiuscula():
    senha = "abc123$%"  
    resultado = validar_senha(senha)
    assert not resultado, "Senhas sem letra maiúscula devem ser inválidas"
```

![image](https://github.com/user-attachments/assets/e5e8f599-7da1-4dc6-81e6-c21c647370d3)


### 🟢 GREEN

```python
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

def test_senha_sem_maiuscula():
    senha = "abc123$%"  
    resultado = validar_senha(senha)
    assert not resultado, "Senhas sem letra maiúscula devem ser inválidas"

```

### 🔵 REFACTOR

```python
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

```


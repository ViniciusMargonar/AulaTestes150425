# Testes de Software

## Mínimo de 8 caracteres.

### <span style="color:red">RED <span>
  
```
def validar_senha(senha: str) -> bool:
    return True 

 def test_senha_com_menos_de_8_caracteres():
    senha = "Ab1$xy"  # 6 caracteres
    resultado = validar_senha(senha)
    assert not resultado
```
![image](https://github.com/user-attachments/assets/1a797bc8-21d0-4ce0-8fb9-7548017a68c7)

### GREEN

```
def validar_senha(senha: str) -> bool:
    if len(senha) < 8:
        return False
    return True

def validar_senha(senha: str) -> bool:
    if len(senha) < 8:
        return False
    return True
```

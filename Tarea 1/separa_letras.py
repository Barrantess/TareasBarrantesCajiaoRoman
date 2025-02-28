def separa_letras(cadena):
    # Codigos de error/exito
    NoString = "ErrorCode = 1"
    NoAlpha = "ErrorCode = 2"
    EmptyString = "ErrorCode = 3"
    SuccesString = "SuccesCode = 0"
    
    # Verificar que el parámetro sea un string
    if not isinstance(cadena, str):
        return NoString
    
    # Verificar que el string no este vacio
    if cadena == "":
        return EmptyString
    
    # Verificar que solo contenga letras
    if not cadena.isalpha():
        return NoAlpha
    
    # Separar letras en mayúsculas y minúsculas
    mayusculas = "".join([char for char in cadena if char.isupper()])
    minusculas = "".join([char for char in cadena if char.islower()])
    
    return SuccesString, mayusculas, minusculas

# Ejemplo de uso
cadena = input("Ingrese una cadena de texto: ")
result = separa_letras(cadena)
print(result)  # ('SUCCESS', 'HM', 'olaundo')

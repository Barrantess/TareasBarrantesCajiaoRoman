def potencia_manual(base, potencia):
    # Codigos de error/exito
    EsString = "ErrorCode = 4"
    SuccesPot = "SuccesCode = 1"
    
    # Verificar que los parametros no sean strings
    if isinstance(base, str) or isinstance(potencia, str):
        return EsString
    
    # Manejar caso base de exponente 0
    if potencia == 0:
        return SuccesPot, 1
    
    # Manejar caso de exponente negativo
    if potencia < 0:
        return SuccesPot, 0  # No se permite division, se retorna 0 como indicacion
    
    resultado = 1
    for j in range(potencia):
        suma = 0
        for j in range(base):
            suma += resultado
        resultado = suma
    
    return SuccesPot, resultado

base = int(input("Ingrese la base: "))
potencia = int(input("Ingrese la potencia: "))
result_potencia = potencia_manual(base, potencia)
print(result_potencia)  

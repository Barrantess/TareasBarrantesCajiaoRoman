def separa_letras(cadena):
    # Codigos de error/exito
    EINTEGER = -100 #Número entero de entrada
    EOUTABC = -200 #String con valores fuera del abecedario
    EEMPTYSTRING = -300 #String vacía
    SUCCESS = 0 #Se realiza la operación de manera exitosa
    
    # Verificar si el parámetro es un integer
    try: 
        int(cadena)
        return EINTEGER, None, None
    except ValueError:
        cadena=cadena

    
    # Verificar que el string no este vacio
    if cadena == "":
        return EEMPTYSTRING, None, None
    

    # Verificar que solo contenga letras
    if not cadena.isalpha():
        return EOUTABC, None, None
    
    # Separar letras en mayúsculas y minúsculas
    mayusculas = "".join([char for char in cadena if char.isupper()])
    minusculas = "".join([char for char in cadena if char.islower()])
    
    return SUCCESS, mayusculas, minusculas

def potencia_manual(base, potencia):
    # Códigos de error/éxito
    ESTRING = -400 #Se untrodujo String
    SUCCESS = 0 #Operación exitosa
    resultado = 1 

    # Verificar que los parámetros no sean strings o valores inválidos
    if not isinstance(base, (int)) or not isinstance(potencia, int):
        return ESTRING, None
    
    if base==0 and potencia == 0:
        return SUCCESS, None
    if base == 0:#Potencia de base cero
        return SUCCESS, 0 
    if potencia == 0: #Número elevado a la 1
        return SUCCESS, 1

    
    # Potencia realizada manualmente
    for _ in range(potencia):
        suma = 0
        # Sumar "base" tantas veces como su valor
        for _ in range(base):
            suma += resultado  # Sumar resultado tantas veces como el valor de "base"
        resultado = suma  #
    return SUCCESS, resultado

if __name__ == "__main__":
    metodo=input("Digite 0 para método separar_letras, 1 para método potencia_manual: ")
    if metodo=="0":
        cadena = input("Ingrese una cadena de texto: ")
        result = separa_letras(cadena)
        print(result) 
        input()
    elif metodo=="1":
        base = input("Ingrese la base: ")
        potencia = input("Ingrese la potencia: ")

        # Convertir base y potencia a números, ya que input recibe únicamente strings
        try:
            base = int(base)
            potencia = int(potencia)
        except ValueError:
            base, potencia = None, None  # Fuerza el código de error

        codigoError, resultado = potencia_manual(base, potencia)
        print(f"Código: {codigoError}, Resultado: {resultado}")
        input()
    else:
         print("Opción no válida.")
         input()
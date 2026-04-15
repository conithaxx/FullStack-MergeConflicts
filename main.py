def procesar_nombres(lista_nombres):
    """
    Recibe una lista de nombres y debe devolver una lista 
    con los nombres limpios (sin espacios extra) y en formato correcto.
    """
    procesados = []

    for nombre in lista_nombres:
        # 1. Eliminar espacios en blanco al inicio y final
        limpio = nombre.strip()

        # 2. Poner la primera letra en mayúscula y el resto en minúscula
        if limpio:  # 3. Solo agregar si no está vacío
            procesados.append(limpio.capitalize())

    return procesados


if __name__ == "__main__":
    nombres_sucios = ["  juan", "ALICIA", " ", "  rOberto  ", "", "   ", "cRisToBal ", "AgustinA"]
    resultado = procesar_nombres(nombres_sucios)
    print(f"Resultado final: {resultado}")

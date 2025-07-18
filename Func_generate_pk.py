def generate_pk(*args):
    """
    Devuelve la concatenación de los argumentos recibidos, separados por '_'.
    """
    return "_".join(str(arg) for arg in args)

def nvl(valor, reemplazo):
    """
    Devuelve 'valor' si no es None, en caso contrario devuelve 'reemplazo'.
    Equivalente a la función NVL de Oracle.
    """
    return valor if valor is not None else reemplazo

# Ejemplo de uso:
#   resultado = concatenar_campos(1, 20, "ABC")
#   print(resultado)  # Salida: 1_20_ABC
#   print(nvl(None, 'sc'))  # Salida: sc
#   print(nvl(5, 'sc'))     # Salida: 5
import sys  # Libreria para leer argumentos desde la linea de comandos


def AFDClasificador(cadena):
    # Estado inicial del automata
    estado_actual = "q1"

    for simbolo in cadena:

        # Empezamos en el estado inicial "q1"
        if estado_actual == "q1":

            # δ(q1, 0) = q2 
            if simbolo == "0":
                estado_actual = "q2"

            # δ(q1, 1) = q3
            elif simbolo == "1":
                estado_actual = "q3"

            # Si no es 0 o 1, se rechaza de una
            else:
                return False

        # Estado de acceptacion
        elif estado_actual == "q2":

            # Desde q2, cualquier 0 o 1 nos mantiene en q2
            # δ(q2, 0) = q2
            # δ(q2, 1) = q2
            if simbolo == "0" or simbolo == "1":
                estado_actual = "q2"

            else:
                return False

        # Si esta en q3 es estado de rechazo
        elif estado_actual == "q3":

            # Una vez que se entra aquí, ya no se puede salir
            if simbolo == "0" or simbolo == "1":
                estado_actual = "q3"
            else:
                return False

    # Cuando termina de leerse toda la cadena, el AFD acepta SOLO si el estado final es q2
    # w es aceptada si δ*(q1, w) ∈ F
    return estado_actual == "q2"


def main():

    if len(sys.argv) != 2:
        print("Uso: python AFD.py entrada.txt")
        return

    archivo = sys.argv[1]

    try:
        # Se abre el archivo
        with open(archivo, "r") as f:
            lineas = f.readlines()

        # Se lee linea porf linea del archivo txt como una cadena 
        for linea in lineas:

            # strip() elimina saltos de línea y espacios extra
            cadena = linea.strip()

            # Simula el AFD con la cadena actual
            if AFDClasificador(cadena):
                print("ACEPTA")
            else:
                print("NO ACEPTA")

    # El archivo no existe
    except FileNotFoundError:
        print("Archivo no encontrado")

if __name__ == "__main__":
    main()

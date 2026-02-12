# Automatas-Finitos-Deterministas
# Simulación de un Autómata Finito Determinista (AFD)

## Autor
Angel De Jesus Robles Araque  
Universidad Sergio Arboleda  

## Descripción

Implemente en python una programa que simule un AFD.
Considere el ADF de la presentación 02.
El programa debe llamarse: AFD.py.
El programa debe ser capaz de leer como parámetro un archivo .txt que contenga al menos 10 lineas de cadenas validas y no validas.

Para correr el programa, debe ser así: python AFD.py entrada.txt
Y la salida debe ser por consola. (Pantalla).
Solo puede imprimir ACEPTA o NO ACEPTA.
El AFD reconoce cadenas binarias (compuestas por 0 y 1) que comiencen con el símbolo 0.

## Definición formal del AFD

Estados:
- q1 (estado inicial)
- q2 (estado de aceptación)
- q3 (estado de rechazo)

Alfabeto:
- {0,1}

Tabla de transiciones:

<img width="741" height="106" alt="image" src="https://github.com/user-attachments/assets/df69c49c-c6f7-43ae-931a-c2ee00c7a5cd" />

Condición de aceptación:
- La cadena es aceptada si el estado final es q2.

## Funcionamiento del programa

El programa:

1. Lee un archivo de texto pasado como parámetro.
2. Procesa cada línea como una cadena independiente.
3. Simula el recorrido del AFD.
4. Imprime en consola:
   - ACEPTA
   - NO ACEPTA

## Ejecución

Desde la terminal:
<img width="1167" height="675" alt="image" src="https://github.com/user-attachments/assets/8d3a26fc-93c3-4d94-bc7d-ef8e4f649405" />
Se navega desde el directorio principal hacia la carpeta Escritorio usando el comando cd. Luego se utiliza ls para verificar el contenido del directorio y confirmar que la ruta es correcta

<img width="1376" height="306" alt="image" src="https://github.com/user-attachments/assets/6133bf23-0451-4d31-a2d2-b9235fbe44ca" />
Se ingresa a la carpeta “Lenguajes de Programación y Trasducción” usando comillas debido a los espacios en el nombre. Con ls se listan las subcarpetas disponibles para continuar la navegacion

<img width="1471" height="333" alt="image" src="https://github.com/user-attachments/assets/9f46e0fb-2a38-47e0-bb7d-acdeffa82532" />
Se accede a la carpeta “Automatas Finitos Deterministas” donde se encuentran los archivos del proyecto. Se verifica con ls que existen AFD.py y entrada.txt antes de ejecutar el programa


<img width="1463" height="456" alt="image" src="https://github.com/user-attachments/assets/974a1e73-6816-4974-aa5d-1d0cad1ec49b" />
Se ejecuta el programa con python AFD.py entrada.txt, pasando el archivo como parámetro. El sistema procesa cada cadena del archivo y muestra en consola si el AFD la acepta o no según el estado final






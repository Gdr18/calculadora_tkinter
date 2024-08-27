# Calculadora Tkinter

Esta aplicación es una calculadora implementada en Python utilizando la biblioteca `tkinter` para la interfaz gráfica de usuario.

## Características

- Selecciona el modo oscuro o claro automáticamente basándose en la configuración del sistema.
- Operaciones básicas: suma, resta, multiplicación, división, porcentaje, borrado de operación completa ('C'), borrado de texto de entrada ('CE').
- Manejo de errores y comunicación al usuario de ellos.

## Directorio
- **/assets**: En este directorio se encuentra '*Calculator_30001.ico*', el icono utilizado para la ventana.
- **calculator_logic.py**: En este archivo se desarrolla la lógica principal de la aplicación.
- **calculator.py**: En este archivo se configura la interfaz gráfica de la calculadora y se vinculan los botones a las funciones lógicas definidas en '*calculator_logic.py*'. Además, se aplica el tema visual definido en '*theme_manager.py*'.
- **theme_manager.py**: En este archivo se desarrolla la lógica para la aplicación de un tema u otro según la configuración del usuario.

## Requisitos

- **Python 3.x**
- **tkinter**: Biblioteca estándar de Python para crear interfaces gráficas de usuario. Viene incluida en la mayoría de las distribuciones de Python para Windows.
- **winreg**: Biblioteca estándar de Python para acceder al registro de Windows. Viene incluida en la mayoría de las distribuciones de Python para Windows.

## Instalación

1. Asegúrate de tener Python 3.x instalado.
2. Clona este repositorio en tu máquina local.
    ```bash
    git clone https://github.com/Gdr18/calculadora_tkinter.git
    ```
    ```bash
    cd calculadora_tkinter
    ```
3. Ejecuta el archivo `calculator.py`.

## Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o enviar un pull request.

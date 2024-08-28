# Calculadora Tkinter

Esta aplicación es una calculadora implementada en Python utilizando la biblioteca `tkinter` para la interfaz gráfica de usuario.

## Características

- Selecciona el modo oscuro o claro automáticamente basándose en la configuración del sistema.
- Operaciones básicas: suma, resta, multiplicación, división, porcentaje, borrado de operación completa ('C'), borrado de texto de entrada ('CE').
- Manejo de errores y comunicación al usuario de ellos.

## Directorio
- **/assets**: En este directorio se encuentra '*Calculator_30001.ico*', el icono utilizado para la ventana.
- **/installer**: En este directorio se encuentra el instalador de Windows de la aplicación '*calculadora_v1.0.exe*'.
- **calculator_logic.py**: En este archivo se desarrolla la lógica principal de la aplicación.
- **calculator.py**: En este archivo se configura la interfaz gráfica de la calculadora y se vinculan los botones a las funciones lógicas definidas en '*calculator_logic.py*'. Además, se aplica el tema visual definido en '*theme_manager.py*'.
- **theme_manager.py**: En este archivo se desarrolla la lógica para la aplicación de un tema u otro según la configuración del usuario.
- **Pipfile**: En este archivo se puede encontrar la librería utilizada así como la versión de Python empleada.
- **LICENSE.txt**: Archivo de licencia.
- **README.md**: Este mismo archivo.

## Librerías

- **Python 3.x**
- **tkinter**: Librería estándar de Python para crear interfaces gráficas de usuario. Viene incluida en la mayoría de las distribuciones de Python para Windows.
- **winreg**: Librería estándar de Python para acceder al registro de Windows. Viene incluida en la mayoría de las distribuciones de Python para Windows.

Opcional, si queremos crear el ejecutable con pyinstaller:
- **pyinstaller 6.10.0**: Librería que convierte programas Python en ejecutables autónomos para Windows, Linux y macOS.
- 
**!Atención**: Para que el ejecutable no falle se debe crear una carpeta con el nombre '*/dist*' en la raíz del proyecto, y posteriormente copiar la carpeta '*/assets*' en su interior.

Para crear el instalador compilando el ejecutable y la carpeta */assets* he utilizado el programa '*Inno Setup*'. 

Adjunto un tutorial detallado realizado por *Python Simplified*: 
[Tutorial Pyinstaller](https://www.youtube.com/watch?v=p3tSLatmGvU&t=226s)

## Instalación

1. Asegúrate de tener Python 3.x instalado.
2. Clona este repositorio en tu máquina local.
    ```bash
    git clone https://github.com/Gdr18/calculadora_tkinter.git
    ```
    ```bash
    cd calculadora_tkinter
    ```
3. Ejecuta el archivo:
   ```bash
   python calculator.py
   ```

o (si tu sistema operativo es Windows)

1. Descargas el instalador que se encuentra en [/installer/calculadora_v1.0.exe](/installer/calculadora_v1.0.exe).
2. Ejecutas el instalador, y listo, tendrás el programa instalado en tu equipo.

## Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o enviar un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE.txt).
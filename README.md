# Tarea 1: Pila, Cola y Tabla Hash

Tec de Monterrey, Módulo 3: Compiladores. Hermann Pauwells Rivera, A01741456.

Pila (LIFO), Cola (FIFO) y Tabla Hash (diccionario que guarda el orden de inserción) hechas desde cero en Python 3, solo con la librería estándar.

## Estructura

- `estructuras/pila.py`: Pila (lista de Python)
- `estructuras/cola.py`: Cola (lista ligada)
- `estructuras/tabla.py`: TablaHash (encadenamiento separado, rehash, lista doble para el orden)
- `demo.py`: programa de demostración (paréntesis balanceados, cola de tokens, tabla de símbolos)
- `tests/test_estructuras.py`: pruebas con unittest

## Cómo correr

Desde esta carpeta:

```
python demo.py
python -m unittest -v
```

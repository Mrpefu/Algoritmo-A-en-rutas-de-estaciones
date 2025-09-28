# Búsqueda A* en Estaciones

## Descripción

Este proyecto implementa un **algoritmo de búsqueda A\*** para encontrar la ruta más corta entre estaciones de transporte basadas en una **base de conocimiento (KB)** con coordenadas y conexiones entre estaciones.  

El proyecto está desarrollado en **Python 3** y permite calcular la ruta óptima considerando el costo de tiempo entre estaciones. Ideal para demostraciones de sistemas basados en reglas y algoritmos de búsqueda heurística.

---

## Estructura del proyecto

Busquedas y sistemas/
│
├── route_kb_a_star.py # Código fuente del algoritmo A*
├── kb.txt # Base de conocimiento con estaciones y conexiones
└── README.md # Este archivo


---

## Contenido del archivo `kb.txt`

El archivo contiene dos secciones:

1. **Estaciones con coordenadas (latitud, longitud)**


---

## Contenido del archivo `kb.txt`

El archivo contiene dos secciones:

1. **Estaciones con coordenadas (latitud, longitud)**

station PlazaCentral 9.237 -75.816
station EstacionNorte 9.250 -75.820
station EstacionSur 9.220 -75.810
station EstacionEste 9.240 -75.800
station EstacionOeste 9.240 -75.830


2. **Conexiones entre estaciones con tiempo estimado en minutos**

edge PlazaCentral EstacionNorte 5
edge PlazaCentral EstacionSur 7
edge PlazaCentral EstacionEste 4
edge PlazaCentral EstacionOeste 6
edge EstacionNorte EstacionEste 3
edge EstacionSur EstacionOeste 3


---

## Requisitos

- Python 3.x
- No requiere librerías externas (solo `math` y `argparse` que vienen con Python).

---

## Instrucciones de ejecución

1. Abre la terminal en la carpeta del proyecto.
2. Ejecuta el script con:

```bash
python route_kb_a_star.py --kb kb.txt --start <EstacionInicial> --goal <EstacionDestino>

Ejemplo:
python route_kb_a_star.py --kb kb.txt --start PlazaCentral --goal EstacionNorte
El programa mostrará en consola:

Estaciones cargadas.

Conexiones entre estaciones.

Proceso de búsqueda paso a paso.

Ruta encontrada y costo total.

Autor:

Francisco Mangones Anaya (@Mrpefu)

Proyecto desarrollado como entrega de la asignatura de Sistemas Basados en Reglas y Búsqueda Inteligente.
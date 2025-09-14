# Códigos de Hamming en $Z_2$

## Resumen

En este repositorio, se incluye el proyecto final de la clase de \textit{Ál...}... oh... demasiado LaTeX... de *Fundamentos de Álgebra Lineal* en el *Tecnológico de Monterrey*. El proyecto consiste en la implementación de los códigos de Hamming mediante los recursos del Álgebra Lineal (*campos de Galois* y *multiplicación de matrices*). Fuera de calificación final que vaya a obtener, estoy muy satisfecho con mis resultados en este proyecto, verdaderamente siento que me podido familizarizar con el funcionameinto de los códigos de Hamming. Mi mayor orgullo es decir que no necesite referencias que explícitamente trataran los códigos de Hamming en álgebra lineal para este trabaja, simplemente hice *reverse engineering* a partir de la implementación mediante operadores lógicos.

## Estructura del Repositorio

* `gf2.py` contiene una clase que hereda de `numpy.array` para implmentar el campo de Galois $Z_2 = \{0, 1 \}$
* `custom_channels.py` contiene una clase predefinida para mandar mensajes y alterarlos. La clase fue dada por el docente del curso
* `utils.py` contiene una serie de funciones que codifican y decodifican una matriz mediante los códigos de hamming. Además de una función que identifica la posición donde ocurrio el error.
* `test.py` es un archivo diseñado para relizar pruebas mediante *PyTest*, leáse más abajo como hacer esto.
* `main_fixed_input.py` implementa códigos de Hamming sobre mensajes enviados y mensajes recibidos predeterminados. Dados por el docenete del curso.
* `main_random.py` implementa códigos de Hamming para mensajes aleatorios que son generados dentro del código.
* La carpeta `TeX` contiene el archivo `.tex` usado para generar el reporte `.pdf` también incluido. Una pequeña demostración de mis habilidades con *LaTeX*.

## Uso

Simplemente, cree un ambiente virtual con *venv*

```sh
python -m venv .venv
```

o con *conda*

```sh
conda create --name HammCodes
```

e instale las librerías del proyecto

```sh
pip install -r requirements.txt
```

A partir de este punto es libre de ejecutar los archivos que desee. Por ejemplo, para comprar el buen funcionamiento de la librería puede corre pytest:

```sh
python -m pytest test.py
```

Aunque mi recomendación personal es que juegue con `main_fixed_input.py` o con `main_random.py` pasando el parámetro *show* como verdadero en cada uno de ellos.

```sh
python main_fixed_input.py
```

```sh
python main_random.py
```

## Misceláneo

Existe una librería llamada `galois` en *Python* que ya implementa matrices en $Z_2$ heredando de *Numpy*. Sin embargo, su rendimiento es pésimo, la creación del campo sobre $Z_2$ es cómicamente lenta. Mi implementación es más rápida ya que solo se enfoca en $Z_2$ y no en otros campos de Galois.

# Hamming codes on GF2

... (pending) ... (it'll be worth the wait, my english readers... if any)
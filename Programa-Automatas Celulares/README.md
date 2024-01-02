<div align="center">

# 🦾 🤖 **Autómatas Celulares** 🔬 ♨️


</div>


<div align="center">

[![](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2FhbWdrMjE1cXBqMzd0YTRjeHlzcG56N3RvZnF3a3ZheGd6bXRzYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pIMlKqgdZgvo4/giphy.gif)](https://www.youtube.com/watch?v=ugGN_Z1jPoM)

</div>


---
Los Autómatas Celulares de Wolfram son modelos matemáticos simples que consisten en una cuadrícula de celdas. Cada celda puede tener un estado específico, y evoluciona según reglas predefinidas. Stephen Wolfram propuso 256 reglas binarias que describen cómo las celdas cambian de estado en función de sus estados y los de sus vecinos. Estas reglas generan patrones visuales complejos y se han utilizado en diversos campos, como la teoría de la complejidad y la simulación de fenómenos naturales.

Para saber mas acerca de los Autómatas Celulares de Wolfram acceder al siguiente [enlace](https://mathworld.wolfram.com/ElementaryCellularAutomaton.html).

Una de las reglas descritas por Wolfram es la regla 150, determinada por:

```Haskell
111: 1
110: 0
101: 0
100: 1
011: 0
010: 1
001: 1
000: 0
```

```Rust

|----|----|----|  |----|----|----|  |----|----|----|  |----|----|----|  |----|----|----|  |----|----|----|  |----|----|----|  |----|----|----|  
| *  | *  | *  |  | *  | *  |    |  | *  |    | *  |  | *  |    |    |  |    | *  | *  |  |    | *  |    |  |    |    | *  |  |    |    |    |  
|----|----|----|  |----|----|----|  |----|----|----|  |----|----|----|  |----|----|----|  |----|----|----|  |----|----|----|  |----|----|----|
     | *  |            |    |            |    |            | *  |            |    |            | *  |            | *  |            |    |              
     |----|            |----|            |----|            |----|            |----|            |----|            |----|            |----|       

     |----|            |----|            |----|            |----|            |----|            |----|            |----|            |----|  
     | 1  |            | 0  |            | 0  |            | 1  |            | 0  |            | 1  |            | 1  |            | 0  |              
     |----|            |----|            |----|            |----|            |----|            |----|            |----|            |----|

```

Nota: Recordemos como es que 150 en binario es 10010110, es por esto que la combinacion antes descrita es la numero 150 (por la dispocision de 0's y 1's despues de cada combinacion de las tuplas ternarias).

-----

## **Requerimientos**

Para esta implementacion se contemplo la biblioteca de tkinter para la interfaz grafica, en caso de no tenerla, se
debe correr por terminal el siguiente comando:

```Haskell
C:\Users\C> pip install tk
```


------


## **Uso**

Para correr el programa que genera un autómata celular en una cuadricula mediante el uso de alguna de las reglas de Wolfram:
- Compilar desde `Programa-Automatas Celulares/`:

Linux  : 

```Haskell
\Programa-Automatas Celulares> python3 AutomataCelular.py
```

Windows:  

```Python
\Programa-Automatas Celulares> python AutomataCelular.py
```

----

Para correr el programa que genera un autómata celular en una linea plana:
- Compilar desde `Programa-Automatas Celulares/`:

Linux  : 

```Haskell
\Programa-Automatas Celulares> python3 ProtoAutomataCelular.py
```

Windows:  

```Python
\Programa-Automatas Celulares> python ProtoAutomataCelular.py
```

----

# **Ejemplos de uso**

```Julia
\Programa-Automatas Celulares> python AutomataCelular.py
```

<div align="center">

![AutomataCelular](./../Media/AutomataCelular.gif)

</div>


```Julia
\Programa-Automatas Celulares> python ProtoAutomataCelular.py
```

<div align="center">

![ProtoAutomata](./../Media/ProtoAutomata.gif)

</div>

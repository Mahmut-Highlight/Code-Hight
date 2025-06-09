# Python in geomerty object and variable
---
## Content
1. [Matariel](#matariel)
2. [Foundation](#foundation)
3. [Angle & Edge](#angle--edge-module)
___
### Files
+ Geometry
    *  Foundation for [Basic.py]()
    *  Exeption for [GeomExep.py]()
    *  Polygon for [Polygon.py]()
+ Variable
    * Number for [Numberçpy]()
___
### Foundation
**What's is angle?**
Angles are geometric figures formed by two rays/lines that share a common endpoint, called Vertex
___
### Using
#### Angle & Edge module
1. #### Angle class
    First,start by creating one Angle object
    ```python
    from MathHigh.Basic import *
    myangle : Angle = Angle(90)
    print(myangle)
    ```
    >Angle(90)

    Let see what inside
    + Operators
        This class has its own addition and subtraction operators
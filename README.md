# Python Math High information
---
## Content
1. [Matariel](#Files)
2. [Foundation](#foundation)
3. [Angle & Edge](#angle--edge-module)
4. [Triangle & Poygon]()
___
### Files
+ Geometry
    *  Foundation for [Basic.py]()
    *  Exeption for [GeomExep.py]()
    *  Polygon for [Polygon.py]()
+ Variable
    * Number for [Number.py]()
    * SqRt for [SqRt.py]()
___
### Foundation
**What's is angle?**
Angles are geometric figures formed by two rays/
lines that share a common endpoint, called Vertex

**What's is edge?**
In math, an edge is the line that joins corners or
surfaces of a shape

**What's is shape?**
a geometric figure such as a square, triangle, or rectangle.
___
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
         for easy handling here are the operators you can use
         __Example__
         * \_\_add\_\_ as four operations:
            Not!!
            >If you want to add any number, the result will be given 
            in the int class in the demo version.

            If you try to sum an Angle object with the + operator, 
            you will either get an error or an int object
###### Contiune this project
> if you want to participate in the development of this project you can
 contact me at my email address mahmutprogrammer@gmail.com
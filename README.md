# Python Math High information
---
## Content
* **[Matariel](#Files)**
* **[Foundation](#foundation)**
* **[Angle & Edge](#angle--edge-module)**
    + [Angle](#angle-class)
        - [Class methods](#method)
        - [Opertator](#operators)
    + [Edge]()
* **[Triangle & Poygon]()**
* **[Imager]()**
___
## Matariel
+ Geometry
    *  Foundation for [Basic.py]()
    *  Exeption for [GeomExep.py]()
    *  Polygon for [Polygon.py]()
+ Variable
    * Number for [Number.py]()
    * SqRt for [SqRt.py]()
    * SqRt for [Fracation.py]()
___
## Foundation
**What's is angle?**

Angles are geometric figures formed by two rays/
lines that share a common endpoint, called Vertex.

**What's is edge?**

In math, an edge is the line that joins corners or
surfaces of a shape.

**What's is shape?**

a geometric figure such as a square, triangle, or rectangle.
___
## Angle & Edge module
+ ### <x style="color : Red;">Angle</code>
    #### What does the Angle class do?
    + **drawing shape**
    Each shape contains an angle so this class on the turtle can draw
    all 2d shape exemple circle,triangle and so on
    + **build**
    The Angle class is convenient and user-friendly, but it is a work slow 
    class so fewer errors in the process.
    <br>
    
    First,start by creating one Angle object
    ```python
    from MathHigh.Basic import *
    myangle : Angle = Angle(90)
    print(myangle)
    ```
    ```
    Angle(90)
    ```
    Let see what inside

    + #### Method
        |func|job|
        |-|-|
        |r90|Returns the rest from 90|
        |r180|Returns the rest from 180|
        |r270|Returns the rest from 270|
        |r360|Returns the rest from 360|
        |sum|Returns the sum of all|
        |howa|Returns at what stage|

    + #### Operators
        This class has its own addition and subtraction operators
        for easy handling here are the operators you can use
        __Example__
        * four operations:
            
            >__Not!!__<br>If you want to add any number, the result will be given 
            in the int class in the demo version.

            I added more operations to avoid making mistakes in the 
            operators, which caused it to be very slow and the operation 
            to be correct.

            __exemple code__
            ```python
            from MathHigh.Basic import *
            an1 : Angle = Angle(90)
            an2 : Angle = Angle(45)
            print(an1+an2)
            print(an1-an2)
            print(an1/an2)
            print(an1//an2)
            print(an1%an2)
            ```
            __outout__
            ```pytoh
            135
            45
            2.0
            2
            0
            ```

            and I am add logical operator
    + #### List process

___
### <code style="color : Aqua">Imager</code>
**What does imeger do?**

Now that we know how to manipulate shapes, we can display objects. There are two ways to do it.
|logo|method|build|
|-|-|-|
|![]()|first method|module built on turtle library|
|![]()|second method|module built on matplotlib library|


###### Contiune this project
> if you want to participate in the development of this project you can
 contact me at my email address mahmutprogrammer@gmail.com.
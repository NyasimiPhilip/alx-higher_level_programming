  <h1>Python - More Classes and Objects</h1>
    <p>This project focuses on object-oriented programming in Python associated class methods, static methods, class vs instance attributes, and how to use the special <code>__str__</code> and <code>__repr__</code> methods.</p>
    <h2>Tests ✔️</h2>
    <p>tests: Folder of test files. Provided by Holberton School.</p>
    <h2>Tasks 📃</h2>
    <ol>
        <li>
            <h3>Simple rectangle</h3>
            <p><code>0-rectangle.py</code>: Empty Python class that defines a rectangle.</p>
        </li>
        <li>
            <h3>Real definition of a rectangle</h3>
            <p><code>1-rectangle.py</code>: Python class that defines a rectangle. Builds on <code>0-rectangle.py</code> with:</p>
            <ul>
                <li>Private instance attribute <code>width</code>.</li>
                <li>Property getter <code>def width(self)</code>: to get width.</li>
                <li>Property setter <code>def width(self, value)</code>: to set width.</li>
                <li>Private instance attribute <code>height</code>.</li>
                <li>Property getter <code>def height(self)</code>: to get height.</li>
                <li>Property setter <code>def height(self, value)</code>: to set height.</li>
                <li>Instantiation with optional width and height: <code>def __init(self, width=0, height=0)</code>:</li>
                <ul>
                    <li>If either of width or height is not an integer, a TypeError is raised with the message <code>width must be an integer</code> or <code>height must be an integer</code>.</li>
                    <li>If either of width or height is less than 0, a ValueError is raised with the message <code>width must be >= 0</code> or <code>height must be >= 0</code>.</li>
                </ul>
            </ul>
        </li>
        <li>
            <h3>Area and Perimeter</h3>
            <p><code>2-rectangle.py</code>: Python class that defines a rectangle. Builds on <code>1-rectangle.py</code> with:</p>
            <ul>
                <li>Public instance method <code>def area(self)</code>: that returns the area of the rectangle.</li>
                <li>Public instance attribute <code>def perimeter(self)</code>: that returns the permiter of the rectangle (if either of width or height equals 0, the perimeter is 0).</li>
            </ul>
        </li>
        <li>
            <h3>String representation</h3>
            <p><code>3-rectangle.py</code>: Python class that defines a rectangle. Builds on <code>2-rectangle.py</code> with:</p>
            <ul>
                <li>Special method <code>__str__</code> to print the rectangle with the # character (if either of width or height equals 0, the method returns an empty string.).</li>
            </ul>
        </li>
        <li>
            <h3>Eval is magic</h3>
            <p><code>4-rectangle.py</code>: Python class that defines a rectangle. Builds on <code>3-rectangle.py</code> with:</p>
            <ul>
                <li>Special method <code>__repr__</code> to return a string representation of the rectangle.</li>
            </ul>
        </li>
        <li>
            <h3>Detect instance deletion</h3>
            <p><code>5-rectangle.py</code>: Python class that defines a rectangle. Builds on <code>4-rectangle.py</code> with:</p>
            <ul>
                <li>Special method <code>__del__</code> that prints the message Bye rectangle... when a Rectangle is deleted.</li>
            </ul>
        </li>
        <li>
            <h3>How many instances</h3>
            <p><code>6-rectangle.py</code>: Python class that defines a rectangle. Builds on <code>5-rectangle.py</code> with:</p>
            <ul>
                <li>Public class attribute <code>number_of_instances</code> that is initialized to 0, incremented for each new instantiation, and decremened for each instance deletion.</li>
            </ul>
        </li>
        <li>
            <h3>Change representation</h3>
            <p><code>7-rectangle.py</code>: Python class that defines a rectangle. Builds on <code>6-rectangle.py</code> with:</p>
            <ul>
                <li>Public class attribute <code>class_symbol</code> that is initialized to # but can be any type - used as the symbol for string representation.</li>
            </ul>
        </li>
        <li>
            <h3>Compare rectangles</h3>
            <p><code>8-rectangle.py</code>: Python class that defines a rectangle. Builds on <code>7-rectangle.py</code> with:</p>
            <ul>
                <li>Static method <code>def bigger_or_equal(rect_1, rect_2)</code>: that returns the rectangle with the greater area (returns rect_1 if both areas are equal).</li>
                <li>If either of rect_1 or rect_2 is not a Rectangle instance, a TypeError is raised with the message <code>rect_1 must be an instance of Rectangle</code> or <code>rect_2 must be an instance of Rectangle</code>.</li>
            </ul>
        </li>
        <li>
            <h3>A square is a rectangle</h3>
            <p><code>9-rectangle.py</code>: Python class that defines a rectangle. Builds on <code>8-rectangle.py</code> with:</p>
            <ul>
                <li>Class method <code>def square(cls, size=0)</code>: that returns a new Rectangle instance with width == height == size.</li>
            </ul>
        </li>
        <li>
            <h3>N Queens</h3>
            <p><code>101-nqueens.py</code>: Python program that solves the N queens puzzle.</p>
            <ul>
                <li>Usage: <code>./101-nqueens.py N</code></li>
                <li>Determines all possible solutions for placing N non-attacking queens on an NxN chessboard.</li>
                <li>Exactly two arguments must be provided. Otherwise, the program prints <code>Usage: nqueens N</code> and exits with the status 1.</li>
                <li>If the provided N is not an integer, the program prints <code>N must be a number</code> and exits with the status 1.</li>
                <li>If the provided N is less than 4, the program prints <code>N must be at least 4</code> and exits with the status 1.</li>
                <li>Solutions are printed one per line in the format <code>[[r, c], [r, c], [r, c], [r, c]]</code> where <code>r</code> and <code>c</code> represent the row and column, respectively, where a queen must be placed.</li>
            </ul>
        </li>
    </ol>

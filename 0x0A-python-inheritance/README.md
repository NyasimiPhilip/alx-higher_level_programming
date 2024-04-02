 <h1>Python - Inheritance</h1>
    <p>In this project, I learned about Python class inheritance. I learned about the differences between super- and sub-classes while practicing inheritance, defining classes with multiple base classes, and overriding inherited methods and attributes.</p>
    <h2>Tests ✔️</h2>
    <p>Tests: Folder of test files. Includes both Holberton-provided ones as well as the following two independently-developed:</p>
    <ul>
        <li>1-my_list.txt</li>
        <li>7-base_geometry.txt</li>
    </ul>
    <h2>Function Prototypes 💾</h2>
    <table>
        <thead>
            <tr>
                <th>File</th>
                <th>Prototype</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>0-lookup.py</td>
                <td>def lookup(obj):</td>
            </tr>
            <tr>
                <td>2-is_same_class.py</td>
                <td>def is_same_class(obj, a_class):</td>
            </tr>
            <tr>
                <td>3-is_kind_of_class.py</td>
                <td>def is_kind_of_class(obj, a_class):</td>
            </tr>
            <tr>
                <td>4-inherits_from.py</td>
                <td>def inherits_from(obj, a_class):</td>
            </tr>
            <tr>
                <td>101-add_attribute.py</td>
                <td>def add_attribute(obj, att, value):</td>
            </tr>
        </tbody>
    </table>
    <h2>Tasks 📃</h2>
    <ol>
        <li>
            <h3>Lookup</h3>
            <p>0-lookup.py: Python function that returns a list of available attributes and methods of an objects.</p>
        </li>
        <li>
            <h3>My list</h3>
            <p>1-my_list.py: Python class MyList that inherits from list. Includes:</p>
            <ul>
                <li>Public instance method def print_sorted(self): that prints the list in ascending sorted order (assumes all list elements are ints).</li>
            </ul>
        </li>
        <li>
            <h3>Exact same object</h3>
            <p>2-is_same_class.py: Python function that returns True if an object is exactly an instance of a specified class; otherwise False.</p>
        </li>
        <li>
            <h3>Same class or inherit from</h3>
            <p>3-is_kind_of_class.py: Python function that returns True if an object is an instance or inherited instance of a specified class; otherwise False.</p>
        </li>
        <li>
            <h3>Only sub class of</h3>
            <p>4-inherits_from.py: Python function that returns True if an object is an inherited instance (either directly or indirectly) from a specified class; otherwise False.</p>
        </li>
        <li>
            <h3>Geometry module</h3>
            <p>5-base_geometry.py: An empty Python class BaseGeometry.</p>
        </li>
        <li>
            <h3>Improve Geometry</h3>
            <p>6-base_geometry.py: Python class BaseGeometry. Builds on 5-base_geometry.py with:</p>
            <ul>
                <li>Public instance method def area(self): that raises an Exception with the message area() is not implemented.</li>
            </ul>
        </li>
        <li>
            <h3>Integer validator</h3>
            <p>7-base_geometry.py: Python class BaseGeometry. Builds on 6-base_geometry.py with:</p>
            <ul>
                <li>Public instance method def integer_validator(self, name, value): that validates the parameter value.</li>
                <li>Assumes the parameter name is always a string.</li>
                <li>The parameter value must be an int, otherwise, a TypeError exception is raised with the message &lt;name&gt; must be an integer.</li>
                <li>The parameter value must be greater than 0, otherwise, a ValueError exception is raised with the message &lt;value&gt; must be greater than 0.</li>
            </ul>
        </li>
        <li>
            <h3>Rectangle</h3>
            <p>8-rectangle.py: Python class Rectangle that inherits from BaseGeometry (7-base_geometry.py). Includes:</p>
            <ul>
                <li>Private attributes width and height - validated with integer_validator.</li>
                <li>Instantiation with width and height: def __init__(self, width, height):</li>
            </ul>
        </li>
        <li>
            <h3>Full rectangle</h3>
            <p>9-rectangle.py: Python class Rectangle that inherits from BaseGeometry (7-base_geometry.py). Builds on 8-rectangle.py with:</p>
            <ul>
                <li>Implementation of the method area().</li>
                <li>Special method __str__ to print Rectangles in the format [Rectangle] &lt;width&gt;/&lt;height&gt;.</li>
            </ul>
        </li>
        <li>
            <h3>Square #1</h3>
            <p>10-square.py: Python class Square that inherits from Rectangle (9-rectangle.py). Includes:</p>
            <ul>
                <li>Private attribute size - validated with integer_validator.</li>
                <li>Instantiation with size: def __init__(self, size):.</li>
                <li>Implementation of the area() method.</li>
            </ul>
        </li>
        <li>
            <h3>Square #2</h3>
            <p>11-square.py: Python class Square that inherits from Rectangle (9-rectangle.py). Builds on 10-square.py with:</p>
            <ul>
                <li>Special method __str__ to print squares in the format [Square] &lt;width&gt;/&lt;height&gt;.</li>
            </ul>
        </li>
        <li>
            <h3>My integer</h3>
            <p>100-my_int.py: Python class MyInt that inherits from int. Includes:</p>
            <ul>
                <li>Inversion of the == and != operators.</li>
            </ul>
        </li>
        <li>
            <h3>Can I?</h3>
            <p>101-add_attribute.py: Python function that adds a new attribute to an object if possible.</p>
            <ul>
                <li>If an attribute cannot be added, a TypeError exception is raised with the message can't add new attribute.</li>
            </ul>
        </li>
    </ol>

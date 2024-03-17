<h1>Python - Classes and Objects</h1>

<p>In this project, I began practicing object-oriented programming using classes and objects in Python. I learned about attributes, methods, and properties as well as data abstraction, data encapsulation, and information hiding.</p>
<h2>Tasks 📃</h2>

<ol>
    <li><strong>My first square</strong></li>
    <p>0-square.py: Python class Square that defines a square.</p>
    <li><strong>Square with size</strong></li>
    <p>1-square.py: Python class Square that defines a square. Builds on 0-square.py with:</p>
    <ul>
        <li>Private instance attribute size.</li>
        <li>Instantiation with size.</li>
    </ul>
    <li><strong>Size validation</strong></li>
    <p>2-square.py: Python class Square that defines a square. Builds on 1-square.py with:</p>
    <ul>
        <li>Instantiation with optional size: <code>def __init__(self, size=0):</code></li>
        <li>If a provided size attribute is not an integer, a TypeError exception is raised with the message "must be an integer".</li>
        <li>If a provided size attribute is less than 0, a ValueError exception is raised with the message "size must be >= 0".</li>
    </ul>
    <li><strong>Area of a square</strong></li>
    <p>3-square.py: Python class Square that defines a square. Builds on 2-square.py with:</p>
    <ul>
        <li>Public instance attribute <code>def area(self):</code> that returns the current square area.</li>
    </ul>
    <li><strong>Access and update private attribute</strong></li>
    <p>4-square.py: Python class Square that defines a square. Builds on 3-square.py with:</p>
    <ul>
        <li>Property <code>def size(self):</code> to retrieve the private instance attribute self.</li>
        <li>Property setter <code>def size(self, value):</code> to set self.</li>
    </ul>
    <li><strong>Printing a square</strong></li>
    <p>5-square.py: Python class Square that defines a square. Builds on 4-square.py with:</p>
    <ul>
        <li>Public instance method <code>def my_print(self):</code> that prints the square with the character # to standard output (if size == 0 -> prints an empty line).</li>
    </ul>
    <li><strong>Coordinates of a square</strong></li>
    <p>6-square.py: Python class Square that defines a square. Builds on 5-square.py with:</p>
    <ul>
        <li>Private instance attribute position.</li>
        <li>Property <code>def position(self):</code> to retrieve position.</li>
        <li>Property setter <code>def position(self, value):</code> to set position.</li>
        <li>Instantiation with optional size and position: <code>def __init__(self, size=0, position=(0, 0)):</code></li>
        <li>If a provided position attribute is not a tuple of two integers, a TypeError exception is raised with the message "position must be a tuple of 2 positive integers".</li>
    </ul>
    <li><strong>Singly linked list</strong></li>
    <p>100-singly_linked_list.py: Python classes Node and SinglyLinkedList that define a node of a singly-linked list and a singly-linked list.</p>
    <ul>
        <li>The class Node is defined with:</li>
        <ul>
            <li>Private instance attribute data.</li>
            <li>Property <code>def data(self):</code> to set data.</li>
            <li>Property setter <code>def data(self, value):</code> to set data.</li>
            <li>Private instance attribute next_node.</li>
            <li>Property <code>def next_node(self):</code> to set next_node.</li>
            <li>Property <code>def next_node(self, value):</code> to set next_node.</li>
            <li>Instantiation with data and next_node: <code>def __init__(self, data, next_node=None):</code></li>
            <li>If a provided data attribute is not an integer, a TypeError exception is raised with the message "data must be an integer".</li>
            <li>If a provided next_node attribute is not a Node or None, a TypeError exception is raised with the message "next_node must be a Node object".</li>
        </ul>
        <li>The class SinglyLinkedList is defined with:</li>
        <ul>
            <li>Private instance attribute head.</li>
            <li>Instantiation <code>def __init__(self):</code></li>
            <li>Public instance method <code>def sorted_insert(self, value):</code> that inserts a new Node into the correct sorted position in the list increasing order).</li>
        </ul>
    </ul>
    <li><strong>Print Square instance</strong></li>
    <p>101-square.py: Python class Square that defines a square. Builds on 6-square.py with:</p>
    <ul>
        <li>Method <code>__str__</code> to set printing of a Square instance equivalent to my_print().</li>
    </ul>
    <li><strong>Compare 2 squares</strong></li>
    <p>102-square.py: Python class Square that defines a square. Builds on 101-square.py with:</p>
    <ul>
        <li>Methods <code>__eq__, __ne__, __lt__, __le__, __gt__, and __ge__,</code> to enable usage of Square instances with logical operators ==, !=, <, <=, >, and >=, respectively, based on the square area.</li>
    </ul>
    <li><strong>ByteCode -&gt; Python #5</strong></li>
    <p>103-magic_class.py: Python function matching exactly a bytecode provided by Holberton School.</p>
</ol>

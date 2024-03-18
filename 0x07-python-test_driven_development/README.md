
<h1>Python - Test-driven development</h1>

<p>In this project, I started practicing test-driven development using docstring and unittest in Python.</p>
<h2>Function Prototypes 💾</h2>
<table>
    <tr>
        <th>File</th>
        <th>Prototype</th>
    </tr>
    <tr>
        <td>0-add_integer.py</td>
        <td>def add_integer(a, b=98):</td>
    </tr>
    <tr>
        <td>2-matrix_divided.py</td>
        <td>def matrix_divided(matrix, div):</td>
    </tr>
    <tr>
        <td>3-say_my_name.py</td>
        <td>def say_my_name(first_name, last_name=""):</td>
    </tr>
    <tr>
        <td>4-print_square.py</td>
        <td>def print_square(size):</td>
    </tr>
    <tr>
        <td>5-text_indentation.py</td>
        <td>def text_indentation(text):</td>
    </tr>
    <tr>
        <td>100-matrix_mul.py</td>
        <td>def matrix_mul(m_a, m_b):</td>
    </tr>
    <tr>
        <td>101-lazy_matrix_mul.py</td>
        <td>def lazy_matrix_mul(m_a, m_b):</td>
    </tr>
    <tr>
        <td>102-python.c</td>
        <td>void print_python_string(PyObject *p);</td>
    </tr>
</table>

<h2>Tasks 📃</h2>
<ol>
    <li><strong>Integers addition</strong></li>
    <p>0-add_integer.py: Python function that returns the integer addition of two numbers.</p>
    <ul>
        <li>If either of a or b is not an int or float, a TypeError is raised with the message a must be an integer or b must be an integer.</li>
        <li>If either of a or b is a float, it is casted to an int before addition.</li>
    </ul>
    <li><strong>Divide a matrix</strong></li>
    <p>2-matrix_divided.py: Python function that divides all elements of a matrix by a common divisor.</p>
    <ul>
        <li>Returns a new matrix representing the division of all elements of matrix by div.</li>
        <li>Quotients are rounded to two decimal places.</li>
        <li>If matrix is not a list of lists of ints or floats, a TypeError is raised with the message matrix must be a matrix (list of lists) of integers/floats.</li>
        <li>If matrix contains rows of different lengths, a TypeError is raised with the message Each row of the matrix must have the same size.</li>
        <li>If the divisor div is not an int or float, a TypeError is raised with the message div must be a number.</li>
        <li>If div is 0, a ZeroDivisionError is raised with the message division by zero.</li>
    </ul>    
    <li><strong>Say my name</strong></li>
    <p>3-say_my_name.py: Python function that prints a name in the format My name is <first_name> <last_name>.</p>
    <ul>
        <li>If either of first_name or last_name is not a str, a TypeError is raised with the message first_name must be a string or last_name must be a string.</li>
    </ul>    
    <li><strong>Print square</strong></li>
    <p>4-print_square.py: Python function that prints a square using the # character.</p>
    <ul>
        <li>The paramter size represents the height/width of the square.</li>
        <li>If size is not an int, a TypeError is raised with the message, size must be an integer.</li>
        <li>If size is less than 0, a ValueError is raised with the message size must be >= 0.</li>
    </ul>    
    <li><strong>Text indentation</strong></li>
    <p>5-text_indentation.py: Python function that prints text with indentation.</p>
    <ul>
        <li>Two new lines are printed after any ., ?, or : character.</li>
        <li>If text is not a str, a TypeError is raised with the message text must be a string.</li>
        <li>No spaces are printed at the beginning or end of each printed line.</li>
    </ul>    
    <li><strong>Max integer - Unittest</strong></li>
    <p>tests/6-max_integer_test.py: Python class/script that runs unittests for the function def max_integer(list=[]): (provided by Holberton School).</p>    
    <li><strong>Matrix multiplication</strong></li>
    <p>100-matrix_mul.py: Python function that multiplies two matrices.</p>
    <ul>
        <li>Returns a new matrix representing the multiplication of m_a by m_b.</li>
        <li>If either of m_a or m_b is empty (ie. == [] or == [[]]), a ValueError is raised with the message m_a can't be empty or m_b can't be empty.</li>
        <li>If either of m_a or m_b is not a list, a TypeError is raised with the message m_a must be a list or m_b must be a list.</li>
        <li>If either of m_a or m_b is not a list of lists, a TypeError is raised with the message m_a must be a list of lists or m_b must be a list of lists.</li>
        <li>If either of m_a or m_b is not a list of lists of ints or floats, a TypeError is raised with the message m_a should contain only integers or floats or m_b should contain only integers or floats.</li>
        <li>If either of m_a or m_b contains rows of different lengths, a TypeError is raised with the message each row of m_a must should be of the same size or each row of m_b must should be of the same size.</li>
        <li>If m_a and m_b cannot be multiplied (ie. row size of m_a does not match column size of m_b), a ValueError is raised with the message m_a and m_b can't be multiplied.</li>
    </ul>    
    <li><strong>Lazy matrix multiplication</strong></li>
    <p>101-lazy_matrix_mul.py: Python function that multiplies two matrices using the module NumPy.</p>
    <ul>
        <li>Identical in function to 100-matrix_mul.py.</li>
    </ul>    
    <li><strong>CPython #3: Python Strings</strong></li>
    <p>102-python.c: C function that prints basic information about Python string objects.</p>
</ol>

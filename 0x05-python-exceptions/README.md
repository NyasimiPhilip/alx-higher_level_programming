 <h1>Python - Exceptions</h1>
    <p>In this project, I learned handling errors and exceptions in Python with try and except.</p>
    <h2>Function Prototypes 💾</h2>
    <p>Prototypes for functions written in this project:</p>
    <table>
        <tr>
            <th>File</th>
            <th>Prototype</th>
        </tr>
        <tr>
            <td>0-safe_print_list.py</td>
            <td>def safe_print_list(my_list=[], x=0):</td>
        </tr>
        <tr>
            <td>1-safe_print_integer.py</td>
            <td>def safe_print_integer(value):</td>
        </tr>
        <tr>
            <td>2-safe_print_list_integers.py</td>
            <td>def safe_print_list_integers(my_list=[], x=0):</td>
        </tr>
        <tr>
            <td>3-safe_print_division.py</td>
            <td>def safe_print_division(a, b):</td>
        </tr>
        <tr>
            <td>4-list_division.py</td>
            <td>def list_division(my_list_1, my_list_2, list_length):</td>
        </tr>
        <tr>
            <td>5-raise_exception.py</td>
            <td>def raise_exception():</td>
        </tr>
        <tr>
            <td>6-raise_exception_msg.py</td>
            <td>def raise_exception_msg(message=""):</td>
        </tr>
        <tr>
            <td>100-safe_print_integer_err.py</td>
            <td>def safe_print_integer_err(value):</td>
        </tr>
        <tr>
            <td>101-safe_function.py</td>
            <td>def safe_function(fct, *args):</td>
        </tr>
        <tr>
            <td>102-magic_calculation.py</td>
            <td>def magic_calculation(a, b):</td>
        </tr>
        <tr>
            <td>103-python.c</td>
            <td>void print_python_list(PyObject *p);<br>
            void print_python_bytes(PyObject *p);<br>
            void print_python_float(PyObject *p);</td>
        </tr>
    </table>
    <h2>Tasks 📃</h2>
    <ol>
        <li>
            <h3>Safe list printing</h3>
            <p>0-safe_print_list.py: Python function that prints x elements of a list on the same line, followed by a new line.<br>
            The parameter x represents the number of elements to print - can be bigger than the length of my_list.<br>
            Returns the real number of elements printed.<br>
            Without importing modules or using len().</p>
        </li>
        <li>
            <h3>Safe printing of an integers list</h3>
            <p>1-safe_print_integer.py: Python function that prints an integer in "{:d}".format() format.<br>
            The parameter value can be any type.<br>
            Returns True if value was printed correctly (i.e., was an integer), False otherwise.<br>
            Without importing modules or using type().</p>
        </li>
        <li>
            <h3>Print and count integers</h3>
            <p>2-safe_print_list_integers.py: Python function that prints the first x elements of a list that are integers on the same line, followed by a new line.<br>
            The parameter my_list can contain any type.<br>
            The parameter x represents the number of elements to print - can be bigger than the length of my_list.<br>
            Returns the real number of integers printed.<br>
            Without importing modules or using len().</p>
        </li>
        <li>
            <h3>Integers division with debug</h3>
            <p>3-safe_print_division.py: Python function that divides two integers and prints the result using finally:.<br>
            The function assumes that the arguments are integers.<br>
            Upon success, returns the value of the division; otherwise - returns None.<br>
            Without importing modules.</p>
        </li>
        <li>
            <h3>Divide a list</h3>
            <p>4-list_division.py: Python function that divides two lists element by element.<br>
            Returns a new list of length list_length with all divisions.<br>
            The lists my_list_1 and my_list_2 can contain any type.<br>
            The parameter list_length can be larger than the lengths of either list.<br>
            If an element is not an integer or float, the function prints wrong type.<br>
            If the division cannot be done, the result of the division is 0 and the function prints: division by 0.<br>
            If either of my_list_1 or my_list_2 is too short, the function prints: out of range.<br>
            Without importing modules.</p>
        </li>
        <li>
            <h3>Raise exception</h3>
            <p>5-raise_exception.py: Python function that raises a type exception.<br>
            Without importing modules.</p>
        </li>
        <li>
            <h3>Raise a message</h3>
            <p>6-raise_exception_msg.py: Python function that raises a name exception with a message.<br>
            Without importing modules.</p>
        </li>
        <li>
            <h3>Safe integer print with error message</h3>
            <p>100-safe_print_integer_err.py: Python function that prints an integer with type-checking in "{:d}".format()) format.<br>
            The parameter value can be any type.<br>
            Returns True if value was printed correctly (i.e., was an integer).<br>
            Otherwise, prints an exception error to stderr and returns False.<br>
            Without importing modules.</p>
        </li>
        <li>
            <h3>Safe function</h3>
            <p>101-safe_function.py: Python function that executes a function safely.<br>
            The function assumes that the parameter fct is always a pointer to a function.<br>
            Upon success, returns the result of the function.<br>
            Otherwise, prints an exception error to stderr and returns None.</p>
        </li>
        <li>
            <h3>ByteCode -&gt; Python #4</h3>
            <p>102-magic_calculation.py: Python function matching exactly a bytecode provided by Holberton School.</p>
        </li>
        <li>
            <h3>CPython #2: PyFloatObject</h3>
            <p>103-python.c: C functions that print basic information about Python lists, bytes, and float objects.</p>
        </li>
    </ol>

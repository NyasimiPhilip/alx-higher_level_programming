 <h1>Python - More Data Structures: Set, Dictionary</h1>
    <p>In this project, I learned about sets and dictionaries in Python. I practiced using them with the lambda, map, filter, and reduce methods.</p>
    <h2>Tests ✔️</h2>
    <p>tests: Folder of test files. Provided by Holberton School.</p>
    <h2>Function Prototypes 💾</h2>
    <p>Prototypes for functions written in this project:</p>
    <table>
        <tr>
            <th>File</th>
            <th>Prototype</th>
        </tr>
        <tr>
            <td>0-square_matrix_simple.py</td>
            <td>def square_matrix_simple(matrix=[]):</td>
        </tr>
        <tr>
            <td>1-search_replace.py</td>
            <td>def search_replace(my_list, search, replace):</td>
        </tr>
        <tr>
            <td>2-uniq_add.py</td>
            <td>def uniq_add(my_list=[]):</td>
        </tr>
        <tr>
            <td>3-common_elements.py</td>
            <td>def common_elements(set_1, set_2):</td>
        </tr>
        <tr>
            <td>4-only_diff_elements.py</td>
            <td>def only_diff_elements(set_1, set_2):</td>
        </tr>
        <tr>
            <td>5-number_keys.py</td>
            <td>def number_keys(a_dictionary):</td>
        </tr>
        <tr>
            <td>6-print_sorted_dictionary.py</td>
            <td>def print_sorted_dictionary(a_dictionary):</td>
        </tr>
        <tr>
            <td>7-update_dictionary.py</td>
            <td>def update_dictionary(a_dictionary, key, value):</td>
        </tr>
        <tr>
            <td>8-simple_delete.py</td>
            <td>def simple_delete(a_dictionary, key=""):</td>
        </tr>
        <tr>
            <td>9-multiply_by_2.py</td>
            <td>def multiply_by_2(a_dictionary):</td>
        </tr>
        <tr>
            <td>10-best_score.py</td>
            <td>def best_score(a_dictionary):</td>
        </tr>
        <tr>
            <td>11-mutiply_list_map.py</td>
            <td>def mutiply_list_map(my_list=[], number=0):</td>
        </tr>
        <tr>
            <td>12-roman_to_int.py</td>
            <td>def roman_to_int(roman_string):</td>
        </tr>
        <tr>
            <td>100-weight_average.py</td>
            <td>def weight_average(my_list=[]):</td>
        </tr>
        <tr>
            <td>101-square_matrix_map.py</td>
            <td>def square_matrix_map(matrix=[]):</td>
        </tr>
        <tr>
            <td>102-complex_delete.py</td>
            <td>def complex_delete(a_dictionary, value):</td>
        </tr>
        <tr>
            <td>103-python.c</td>
            <td>void print_python_list(PyObject *p);<br>void print_python_bytes(PyObject *p);</td>
        </tr>
    </table>
    <h2>Tasks 📃</h2>
    <ol>
        <li>
            <h3>Squared simple</h3>
            <p><code>0-square_matrix_simple.py</code>: Python function that computes the square value of all integers of a matrix.</p>
            <ul>
                <li>The parameter matrix is a two-dimensional array.</li>
                <li>Returns a matrix of the same size as matrix where each value is the square of the input value.</li>
                <li>The initial matrix is not modified.</li>
                <li>Without importing modules.</li>
            </ul>
        </li>
        <li>
            <h3>Search and replace</h3>
            <p><code>1-search_replace.py</code>: Python function that replaces all occurrences of an element by another in a new list.</p>
            <ul>
                <li>The parameter my_list is the initial list.</li>
                <li>The parameter search is the element to replace in the list.</li>
                <li>The parameter replace is the new element.</li>
                <li>Without importing modules.</li>
            </ul>
        </li>
        <li>
            <h3>Unique addition</h3>
            <p><code>2-uniq_add.py</code>: Python function that adds all unique integers in a list (once for each integer).</p>
            <ul>
                <li>Without importing modules.</li>
            </ul>
        </li>
        <li>
            <h3>Present in both</h3>
            <p><code>3-common_elements.py</code>: Python function that returns a set of common elements in two sets.</p>
            <ul>
                <li>Without importing modules.</li>
            </ul>
        </li>
        <li>
            <h3>Only differents</h3>
            <p><code>4-only_diff_elements.py</code>: Python function that returns a set of all elements present in only one set.</p>
            <ul>
                <li>Without importing modules.</li>
            </ul>
        </li>
        <li>
            <h3>Number of keys</h3>
            <p><code>5-number_keys.py</code>: Python function that returns the number of keys in a dictionary.</p>
            <ul>
                <li>Without importing modules.</li>
            </ul>
        </li>
        <li>
            <h3>Print sorted dictionary</h3>
            <p><code>6-print_sorted_dictionary.py</code>: Python function that prints a dictionary by ordered keys.</p>
            <ul>
                <li>The function assumes all keys are strings.</li>
                <li>Keys are printed in alphabetic order.</li>
                <li>Keys are only sorted on the first level.</li>
                <li>Dictionary values can have any type.</li>
                <li>Without importing modules.</li>
            </ul>
        </li>
        <li>
            <h3>Update dictionary</h3>
            <p><code>7-update_dictionary.py</code>: Python function that replaces or adds key/value pairs in a dictionary.</p>
            <ul>
                <li>The parameter key is always a string.</li>
                <li>The parameter value is any type.</li>
                <li>If a key exists in the dictionary, the value is replaced.</li>
                <li>If a key does not exist in the dictionary, it is created.</li>
                <li>Without importing modules.</li>
            </ul>
        </li>
        <li>
            <h3>Simple delete by key</h3>
            <p><code>8-simple_delete.py</code>: Python function that deletes a key in a dictionary.</p>
            <ul>
                <li>The parameter key is always a string.</li>
                <li>If the key does not exist, the dictionary does not change.</li>
                <li>Without importing modules.</li>
            </ul>
        </li>
        <li>
            <h3>Multiply by 2</h3>
            <p><code>9-multiply_by_2.py</code>: Python function that returns a new dictionary with all values multiplied by 2.</p>
            <ul>
                <li>The function assumes all values are integers.</li>
                <li>Without importing modules.</li>
            </ul>
        </li>
        <li>
            <h3>Best score</h3>
            <p><code>10-best_score.py</code>: Python function that returns a key value with the biggest integer value.</p>
            <ul>
                <li>The function assumes all values are integers.</li>
                <li>The function assumes all students have a different score.</li>
                <li>If no score is found, the function returns None.</li>
                <li>Without importing modules.</li>
            </ul>
        </li>
        <li>
            <h3>Multiply by using map</h3>
            <p><code>11-mutiply_list_map.py</code>: Python function that returns a list with all values multiplied by a number using map.</p>
            <ul>
                <li>Returns a new length of the same length has my_list with each value multiplied by number.</li>
                <li>The initial list is not modified.</li>
                <li>Without using loops or importing modules.</li>
            </ul>
        </li>
        <li>
            <h3>Roman to Integer</h3>
            <p><code>12-roman_to_int.py</code>: Python function that converts a roman numeral to an integer.</p>
            <ul>
                <li>The function assumes the number will be between 1-3999.</li>
                <li>If the parameter roman_string is not a string or None, the function returns 0.</li>
            </ul>
        </li>
        <li>
            <h3>Weighted average!</h3>
            <p><code>100-weight_average.py</code>: Python function that returns the weighted average of all integers in a list of tuples.</p>
            <ul>
                <li>Tuple format: (&lt;score&gt;, &lt;weight&gt;).</li>
                <li>If the list is empty - returns 0.</li>
                <li>Without importing modules.</li>
            </ul>
        </li>
        <li>
            <h3>Squared by using map</h3>
            <p><code>101-square_matrix_map.py</code>: Python function that computes the square value of all integers of a matrix using map.</p>
            <ul>
                <li>The parameter matrix is a two-dimensional array.</li>
                <li>Returns a new matrix of the same size as matrix with each value squared.</li>
                <li>The initial matrix is not modified.</li>
                <li>Without using loops or importing modules.</li>
            </ul>
        </li>
        <li>
            <h3>Delete by value</h3>
            <p><code>102-complex_delete.py</code>: Python function that deletes keys with a specific value in a dictionary.</p>
            <ul>
                <li>If the value does not exist, the dictionary is not changed.</li>
                <li>All keys having the searched value are deleted.</li>
                <li>Without importing modules.</li>
            </ul>
        </li>
        <li>
            <h3>CPython #1: PyBytesObject</h3>
            <p><code>103-python.c</code>: C functions that print basic information about Python lists and Python bytes objects.</p>
        </li>
    </ol>

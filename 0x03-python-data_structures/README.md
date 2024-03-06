  <h1>Python - Data Structures: Lists, Tuples</h1>
    <p>In this project, I learned about how sequence data types work in Python - specifically, lists and tuples.</p>
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
                <td>0-print_list_integer.py</td>
                <td>def print_list_integer(my_list=[]):</td>
            </tr>
            <tr>
                <td>1-element_at.py</td>
                <td>def element_at(my_list, idx):</td>
            </tr>
            <tr>
                <td>2-replace_in_list.py</td>
                <td>def replace_in_list(my_list, idx, element):</td>
            </tr>
            <tr>
                <td>3-print_reversed_list_integer.py</td>
                <td>def print_reversed_list_integer(my_list=[]):</td>
            </tr>
            <tr>
                <td>4-new_in_list.py</td>
                <td>def new_in_list(my_list, idx, element):</td>
            </tr>
            <tr>
                <td>5-no_c.py</td>
                <td>def no_c(my_string):</td>
            </tr>
            <tr>
                <td>6-print_matrix_integer.py</td>
                <td>def print_matrix_integer(matrix=[[]]):</td>
            </tr>
            <tr>
                <td>7-add_tuple.py</td>
                <td>def add_tuple(tuple_a=(), tuple_b=()):</td>
            </tr>
            <tr>
                <td>8-multiple_returns.py</td>
                <td>def multiple_returns(sentence):</td>
            </tr>
            <tr>
                <td>9-max_integer.py</td>
                <td>def max_integer(my_list=[]):</td>
            </tr>
            <tr>
                <td>10-divisible_by_2.py</td>
                <td>def divisible_by_2(my_list=[]):</td>
            </tr>
            <tr>
                <td>11-delete_at.py</td>
                <td>def delete_at(my_list=[], idx=0):</td>
            </tr>
            <tr>
                <td>100-print_python_list_info.c</td>
                <td>void print_python_list_info(PyObject *p);</td>
            </tr>
        </tbody>
    </table>
    <h2>Tasks 📃</h2>
    <ol>
        <li>
            <h3>Print a list of integers</h3>
            <p><code>0-print_list_integer.py</code>: Python function that prints all integers of a list, one per line.</p>
            <p>Without importing modules or casting integers into strings.</p>
        </li>
        <li>
            <h3>Secure access to an element in a list</h3>
            <p><code>1-element_at.py</code>: Python function that retrieves an element from a list.</p>
            <p>If idx is negative or out of range (greater than the number of elements in my_list), the function returns None.</p>
            <p>Without import modules or using try/except.</p>
        </li>
        <li>
            <h3>Replace element</h3>
            <p><code>2-replace_in_list.py</code>: Python function that replaces an element of a list at a specific position.</p>
            <p>If idx is negative or out of range (greater than the number of elements in my_list), the function returns the original list.</p>
            <p>Without importing modules or using try/except.</p>
        </li>
        <li>
            <h3>Print a list of integers... in reverse!</h3>
            <p><code>3-print_reversed_list_integer.py</code>: Python function that prints all integers of a list, one per line, in reverse order.</p>
            <p>Without importing modules or casting integers into strings.</p>
        </li>
        <li>
            <h3>Replace in a copy</h3>
            <p><code>4-new_in_list.py</code>: Python function that replaces an element of a list at a specific position without modifying the original list.</p>
            <p>If idx is negative or out of range (greater than the number of elements in my_list), the function returns the original list.</p>
            <p>Without importing modules or using try/except.</p>
        </li>
        <li>
            <h3>Can you C me now?</h3>
            <p><code>5-no_c.py</code>: Python function that removes all characters c and C from a string and returns the string.</p>
            <p>Without importing modules or using str.replace().</p>
        </li>
        <li>
            <h3>Lists of lists = Matrix</h3>
            <p><code>6-print_matrix_integer.py</code>: Python function that prints a matrix of integers, one row per line.</p>
            <p>Without casting integers into strings.</p>
        </li>
        <li>
            <h3>Tuples addition</h3>
            <p><code>7-add_tuple.py</code>: Python function that adds two tuples.</p>
            <p>Returns a tuple with two integers:</p>
            <ul>
                <li>The first element is the addition of the first element of each argument.</li>
                <li>The second element is the addition of the second element of each argument.</li>
            </ul>
            <p>If a tuple is smaller than 2, the value 0 is used for the missing integer.</p>
            <p>If a tuple is larger than 2, only the first two integers are used.</p>
            <p>Without importing modules.</p>
        </li>
        <li>
            <h3>More returns!</h3>
            <p><code>8-multiple_returns.py</code>: Python function that returns a tuple with the length of a string and its first character.</p>
            <p>If the string is empty, the first character should equal None.</p>
            <p>Without importing modules.</p>
        </li>
        <li>
            <h3>Find the max</h3>
            <p><code>9-max_integer.py</code>: Python function that finds the biggest integer of a list.</p>
            <p>If the list is empty, the function returns None.</p>
            <p>Without importing modules or using the builtin max().</p>
        </li>
        <li>
            <h3>Only by 2</h3>
            <p><code>10-divisible_by_2.py</code>: Python function that finds all multiples of 2 in a list.</p>
            <p>Returns a new list of the same size. Each element of the new list contains either True or False corresponding to whether the integer at the same position in the original list is a multiple of 2.</p>
            <p>Without importing modules.</p>
        </li>
        <li>
            <h3>Delete at</h3>
            <p><code>11-delete_at.py</code>: Python function that deletes an item at a specific position in a list.</p>
            <p>If idx is negative or out of range (greater than the number of elements in my_list), the function returns the original list.</p>
            <p>Without importing modules or using pop().</p>
        </li>
        <li>
            <h3>Switch</h3>
            <p><code>12-switch.py</code>: Python program that switches the values of variable a and b.</p>
            <p>Completion of this source code.</p>
        </li>
        <li>
            <h3>Linked list palindrome</h3>
            <p><code>13-is_palindrome.c</code>: C function that checks if a singly-linked list is a palindrome.</p>
            <p>If the function is not a palindrome - returns 0.</p>
            <p>If the function is a palindrome - returns 1.</p>
            <p>An empty list is considered a palindrome.</p>
            <p>Helper files:</p>
            <ul>
                <li>linked_lists.c: C functions handling linked lists for testing 13-is_palindrome.c (provided by Holberton School).</li>
                <li>lists.h: Header file containing definitions and prototypes for all types and functions used in linked_lists.c and 13-insert_number.c.</li>
            </ul>
        </li>
        <li>
            <h3>CPython #0: Python lists</h3>
            <p><code>100-print_python_list_info.c</code>: C function that prints basic information about Python lists.</p>
        </li>
    </ol>

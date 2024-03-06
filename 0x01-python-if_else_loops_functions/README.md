 <h1>Python - if/else, loops, functions</h1>
    <p>In this project, I began utilizing conditionals and loops in Python by using if, if ... else, break, continue, pass, and range statements with while and for loops. I practiced writing my own Python functions while learning about scope of variables, tracebacks, and arithmetic operators.</p>
    <table>
        <thead>
            <tr>
                <th>File</th>
                <th>Prototype</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>7-islower.py</td>
                <td>def islower(c):</td>
            </tr>
            <tr>
                <td>8-uppercase.py</td>
                <td>def uppercase(str):</td>
            </tr>
            <tr>
                <td>9-print_last_digit.py</td>
                <td>def print_last_digit(number):</td>
            </tr>
            <tr>
                <td>10-add.py</td>
                <td>def add(a, b):</td>
            </tr>
            <tr>
                <td>11-pow.py</td>
                <td>def pow(a, b):</td>
            </tr>
            <tr>
                <td>12-fizzbuzz.py</td>
                <td>def fizzbuzz():</td>
            </tr>
            <tr>
                <td>13-insert_number.c</td>
                <td>listint_t *insert_node(listint_t **head, int number);</td>
            </tr>
            <tr>
                <td>101-remove_char_at.py</td>
                <td>def remove_char_at(str, n):</td>
            </tr>
            <tr>
                <td>102-magic_calculation.py</td>
                <td>def magic_calculation(a, b, c):</td>
            </tr>
        </tbody>
    </table>
    <h2>Tasks 📃</h2>
    <ol>
        <li>
            <h3>Positive anything is better than negative nothing</h3>
            <p><code>0-positive_or_negative.py</code>: Python program that assigns a random signed number to the variable number each time it is executed and prints whether number is positive or negative. Prints the number followed by:</p>
            <ul>
                <li>If the number is greater than 0: is positive</li>
                <li>If the number is 0: is zero</li>
                <li>If the number is less than 0: is negative</li>
            </ul>
            <p>Followed by a new line. Completion of this source code.</p>
        </li>
        <li>
            <h3>The last digit</h3>
            <p><code>1-last_digit.py</code>: Python program that assigns a random signed number to the variable number each time it is executed and prints its last digit. Prints the string Last digit of [number] is [last_digit] followed by:</p>
            <ul>
                <li>If the number is greater than 5: and is greater than 5</li>
                <li>If the number is 0: and is 0</li>
                <li>If the number is less than 6 and not 0: and is less than 6 and not 0</li>
            </ul>
            <p>Followed by a new line. Completion of this source code.</p>
        </li>
        <li>
            <h3>I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game</h3>
            <p><code>2-print_alphabet.py</code>: Python program that prints the alphabet in lowercase, not followed by a new line. Using only one print and one loop. Without storing characters in variables or importing modules.</p>
        </li>
        <li>
            <h3>When I was having that alphabet soup, I never thought that it would pay off</h3>
            <p><code>3-print_alphabt.py</code>: Python program that prints the alphabet in lowercase, followed by a new line. Using only one print and one loop. Without storing characters in variables or importing modules. Prints every letter except for q and e.</p>
        </li>
        <li>
            <h3>Hexadecimal printing</h3>
            <p><code>4-print_hexa.py</code>: Python program that prints all numbers from 0 to 98 in decimal and hexadecimal. Using only one print and one loop. Without storing numbers or strings in variables or importing modules. Printing format: [decimal] = [hexadecimal]</p>
        </li>
        <li>
            <h3>00...99</h3>
            <p><code>5-print_comb2.py</code>: Python program that prints numbers from 0 to 99 two digits each. Numbers are separated by <code>,</code>, except for the last number, which is followed by a new line. Using no more than two print functions and one loop. Without storing numbers or strings in variables or importing modules.</p>
        </li>
        <li>
            <h3>Inventing is a combination of brains and materials. The more brains you use, the less material you need</h3>
            <p><code>6-print_comb3.py</code>: Python program that prints all possible different combinations of two digits in ascending order. Numbers are separated by <code>,</code>, except for the last number, which is followed by a new line. The two digits must be different - 01 and 10 are considered identical. Using no more than three print functions and two loops. Without storing numbers or strings in variables or importing modules.</p>
        </li>
        <li>
            <h3>islower</h3>
            <p><code>7-islower.py</code>: Python function that checks for lowercase characters. Returns True if c is lowercase, False otherwise. Without importing modules or using str.upper() or str.isupper().</p>
        </li>
        <li>
            <h3>To uppercase</h3>
            <p><code>8-uppercase.py</code>: Python function that prints a string in uppercase followed by a new line. Using no more than two print functions and one loop. Without importing modules or using str.upper() or str.isupper().</p>
        </li>
        <li>
            <h3>There are only 3 colors, 10 digits, and 7 notes; its what we do with them that's important</h3>
            <p><code>9-print_last_digit.py</code>: Python function that prints the last digit of a number. Returns the value of the last digit. Without importing modules.</p>
        </li>
        <li>
            <h3>a + b</h3>
            <p><code>10-add.py</code>: Python function that returns the addition of two integers. Without importing modules.</p>
        </li>
        <li>
            <h3>a ^ b</h3>
            <p><code>11-pow.py</code>: Python function that returns a to the power of b. Without importing modules.</p>
        </li>
        <li>
            <h3>Fizz Buzz</h3>
            <p><code>12-fizzbuzz.py</code>: Python function that prints the numbers from 1 to 100 followed by a space. For multiples of three, Fizz is printed instead of the number. For multiples of five, Buzz is printed instead of the number. For multiples of three and five, FizzBuzz is printed instead of the number. Without importing modules.</p>
        </li>
        <li>
            <h3>Insert in sorted linked list</h3>
            <p><code>13-insert_number.c</code>: C function that inserts a number into a sorted linked list. If the function fails, returns NULL. Otherwise, returns the address of the new node. Helper files: <code>linked_lists.c</code>: C functions handling linked lists for testing <code>13-insert_number.c</code> (provided by Holberton School). <code>lists.h</code>: Header file containing definitions and prototypes for all types and functions used in linked_lists.c and <code>13-insert_number.c</code>.</p>
        </li>
        <li>
            <h3>Smile in the mirror</h3>
            <p><code>100-print_tebahpla.py</code>: Python program that prints the alphabet in reverse order, alternating lowercase and uppercase, not followed by a new line. Using only one print and one loop. Without storing characters in variables or importing modules.</p>
        </li>
        <li>
            <h3>Remove at position</h3>
            <p><code>101-remove_char_at.py</code>: Python function that creates a copy of a string without the character at position n. Without importing modules.</p>
        </li>
        <li>
            <h3>ByteCode -&gt; Python #2</h3>
            <p><code>102-magic_calculation.py</code>: Python function matching exactly a bytecode provided by Holberton School.</p>
        </li>
    </ol>

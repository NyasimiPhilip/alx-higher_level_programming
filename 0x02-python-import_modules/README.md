 <h1>Python - import &amp; modules</h1>
    <p>In this project, I learned about importing and using functions and creating modules in Python. I further practiced using the built-in function <code>dir()</code> and using command line arguments within Python programs.</p>
    <h2>Tasks 📃</h2>
    <ol>
        <li>
            <h3>Import a simple function from a simple file</h3>
            <p><code>0-add.py</code>: Python program that imports the function <code>def add(a, b):</code> from the file <code>add_0.py</code> and prints the result of the addition <code>1 + 2 = 3</code>.</p>
            <p>Output: <code>&lt;a value&gt; + &lt;b value&gt; = &lt;add(a, b) value&gt;</code> followed by a new line.</p>
        </li>
        <li>
            <h3>My first toolbox!</h3>
            <p><code>1-calculation.py</code>: Python program that imports functions from the file <code>calculator_1.py</code> and prints the result of the addition, subtraction, multiplication, and division of <code>10</code> and <code>5</code>.</p>
            <p>Output: <code>&lt;a value&gt; &lt;operator&gt; &lt;b value&gt; = &lt;operation(a, b) value&gt;</code> followed by a new line.</p>
        </li>
        <li>
            <h3>How to make a script dynamic!</h3>
            <p><code>2-args.py</code>: Python program that prints the number of and list of its arguments.</p>
            <p>Output: <code>[Number of arguments]</code> argument (if number is one) or arguments (otherwise), followed by:</p>
            <p>: (or . if no arguments were passed), followed by</p>
            <p>A new line, followed by</p>
            <p>One argument per line - the position of the argument (starting at 1) followed by : followed by the argument value and another new line.</p>
        </li>
        <li>
            <h3>Infinite addition</h3>
            <p><code>3-infinite_add.py</code>: Python program that prints the result of the addition of all arguments.</p>
            <p>Output: Sum of the arguments followed by a new line.</p>
        </li>
        <li>
            <h3>Who are you?</h3>
            <p><code>4-hidden_discovery.py</code>: Python program that prints all the names defined by the compiled module <code>hidden_4.pyc</code>.</p>
            <p>Output: One name per line in alphabetical order.</p>
            <p>Names starting with __ are not printed.</p>
        </li>
        <li>
            <h3>Everything can be imported</h3>
            <p><code>5-variable_load.py</code>: Python program that imports the variable <code>a</code> from the file <code>variable_load_5.py</code> and prints its value.</p>
        </li>
        <li>
            <h3>Build my own calculator!</h3>
            <p><code>100-my_calculator.py</code>: Python program that imports all functions from the file <code>calculator_1.py</code> and handles basic operations.</p>
            <p>Usage: <code>./100-my_calculator.py &lt;a&gt; &lt;operator&gt; &lt;b&gt;</code> followed by a new line.</p>
            <p>Output: <code>&lt;a&gt; &lt;operator&gt; &lt;b&gt; = &lt;result&gt;</code> followed by a new line.</p>
            <p>The parameter operator can be:</p>
            <ul>
                <li>+ for addition</li>
                <li>- for subtraction</li>
                <li>* for multiplication</li>
                <li>/ for division</li>
            </ul>
            <p>If the operator is none of the above, the function prints Unknown operator. Available operators: +, -, *, and / followed by a new line and exits with a status value of 1.</p>
            <p>If the number of arguments is not three, the program prints Usage: ./100-my_calculator.py &lt;a&gt; &lt;operator&gt; &lt;b&gt; followed by a new line and exits with a status value of 1.</p>
        </li>
        <li>
            <h3>Easy print</h3>
            <p><code>101-easy_print.py</code>: Python program that prints <code>#pythoniscool</code> followed by a new line in the standard output.</p>
            <p>Without using <code>print</code>, <code>eval</code>, <code>open</code>, or <code>sys</code>.</p>
        </li>
        <li>
            <h3>ByteCode -&gt; Python #3</h3>
            <p><code>102-magic_calculation.py</code>: Python function matching exactly a bytecode provided by Holberton School.</p>
        </li>
        <li>
            <h3>Fast alphabet</h3>
            <p><code>103-fast_alphabet.py</code>: Python program that prints the alphabet in uppercase, followed by a new line.</p>
            <p>Without using loops, conditionals, <code>str.join()</code>, string literals, or system calls.</p>
        </li>
    </ol>

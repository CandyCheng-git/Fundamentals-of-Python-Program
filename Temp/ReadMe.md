# Fundamentals of Programming – Summary

```python
# Comment on a single line  
  
name = "Alice" # variable name has the value of Alice  

```
<table>
  <tbody>
    <tr>
      <td>
        <p>
          <strong>Comments</strong>
        </p>
        <p>
          <strong>#</strong> character enables a comment
        </p>
      </td>
      <td>
        <p>
          <em># Comment on a single line</em>
        </p>
        <p>
          <em></em>
        </p>
        <p>name = "Alice" <em># variable name has the value of Alice</em>
        </p>
      </td>
      <td>
        <p>Week 1</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>
          <strong>print() Function</strong>
        </p>
        <p>The <strong>print()</strong> function prints a message to the console or output </p>
      </td>
      <td>
        <p>
          <em># Prints blank line</em>
        </p>
        <p>print()</p>
        <p>
          <em># Prints message "Cheatsheet"</em> print("Cheatsheet")
        </p>
      </td>
      <td>
        <p>Week 1</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>
          <strong>Synax</strong>
        </p>
      </td>
      <td>
        <p>Strings, Boolean, Lists, and so on</p>
      </td>
      <td>
        <p>Week 1</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>
          <strong>Strings</strong>
        </p>
        <p>Strings contains characters enclosed by single quotes or double quotes</p>
      </td>
      <td>
        <p>
          <em># Single quotes </em>single = 'Single'
        </p>
        <p>
          <em># Double quotes </em>double = "Double"
        </p>
      </td>
      <td>
        <p>Week 1</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>
          <strong>String Concatenation </strong>The plus sign <strong>+</strong> can add two str types or Strings (and not just numeric types)
        </p>
      </td>
      <td>
        <p>single = 'Single' <br>double = "Double" <br>
          <em># String Concatenation</em>
        </p>
        <p>
          <em># concatenate becomes "SingleDouble"</em> concatenate = single + double
        </p>
      </td>
      <td>
        <p>Week 1</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>
          <strong>Integer (and Float)</strong>
        </p>
        <ul>
          <li>
            <strong>Integer</strong> must be a whole
          </li>
        </ul>
        <p>number, it can be 0, positive or negative, but must be without decimals</p>
        <ul>
          <li>
            <strong>Float</strong> is a number, it can be positive or negative, but must contain one or more decimals
          </li>
        </ul>
      </td>
      <td>
        <p>
          <em># Integer or int</em>
        </p>
        <p>height = 183</p>
        <p>weather = -6</p>
        <p>zero = 0</p>
        <p>
          <em># Float</em>
        </p>
        <p>f = 1.33</p>
        <p>
          <em># If unsure, use type() function</em>
        </p>
        <p>
          <em># For example</em>
        </p>
        <p>
          <em># print type(f)</em>
        </p>
      </td>
      <td>
        <p>Week 1</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>
          <strong>Variables</strong>
        </p>
        <p>Variables assign a value or store data using an equals sign <strong>=</strong>
        </p>
      </td>
      <td>
        <p>
          <em># Valid variable names and assignment</em> string_var = "String is here"
        </p>
        <p>int_var = 10</p>
        <p>float_var = 10.13</p>
        <p>bool_statement = False</p>
        <p>
          <em># Variable value can be changed after</em> int_var = 12
        </p>
      </td>
      <td>
        <p>Week 1</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>
          <strong>Arithmetic Operations</strong>
        </p>
        <ul>
          <li>
            <strong>+</strong> for addition
          </li>
          <li>
            <strong>-</strong> for subtraction
          </li>
          <li>
            <strong>*</strong> for multiplication
          </li>
          <li>
            <strong>/</strong> for division
          </li>
          <li>
            <strong>%</strong> for modulus (returns the remainder)
          </li>
          <li>
            <strong>**</strong> for exponentiation (number^number)
          </li>
        </ul>
      </td>
      <td>
        <p>
          <em># Arithmetic operations</em>
        </p>
        <p>
          <em></em>
        </p>
        <p>addition = 2 + 5 <em># 7 </em>subtraction = 30 - 40 <em># -10 </em>multiplication = 2 * 90 <em># 180</em> division = 4 / 4.0 <em># 1.0 </em>modulus = 13 % 2 <em># 1 </em>exponentiation = 2 ** 3 <em># 8</em>
        </p>
      </td>
      <td>
        <p>Week 1</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>
          <strong>Modulo operator (%)</strong>
        </p>
        <p>Modulo operation, with a percent sign <strong>%</strong>, returns the remainder of the division operation </p>
        <ol>
          <li>6 % 2 results 0 because 6 divided by 2 would return 3, leaving no remainder</li>
          <li>7 % 2 results 1 because 7 divided by 2 is not evenly divisible, leaving 1 remainder</li>
          <li>9 % 50000 results 9 because 9 divided by 50000 is not evenly divisible, leaving 9 remainder</li>
        </ol>
      </td>
      <td>
        <p>
          <em>
            <sup># Modulo operator %</sup>
          </em>
        </p>
        <p>
          <em>#Example 1</em>
        </p>
        <p>zero = 6 % 2 <em># 0</em>
        </p>
        <p>
          <em></em>
        </p>
        <p>
          <em>#Example 2</em>
        </p>
        <p>one = 7 % 2 <em># 1</em>
        </p>
        <p>
          <em></em>
        </p>
        <p>
          <em>#Example 3</em>
        </p>
        <p>nine = 9 % 50000 <em># 9</em>
        </p>
      </td>
      <td>
        <p>Week 1</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>
          <strong>Plus Equals</strong>
        </p>
        <p>A shortcut to update a variable value can be done by using the plus equals sign <strong>+=</strong>
        </p>
      </td>
      <td>
        <p>
          <em># Plus Equals (int)</em>
        </p>
        <p>count = 0</p>
        <p>count += 1 <em># equivalent to count = count + 1</em>
        </p>
        <p>
          <em></em>
        </p>
        <p>
          <em># Plus Equals (str)</em>
        </p>
        <p>data = "Plus "</p>
        <p>data += " Equals" <em># equivalent to data = data + " Equals"</em>
        </p>
      </td>
      <td>
        <p>Week 1</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>
          <strong>Errors</strong>
        </p>
        <p>PyCharm will (a) display the error type; and (b) information where the error has occurred</p>
      </td>
      <td>
        <p>If unsure, use type() function</p>
        <p>^^^^^^</p>
        <p>SyntaxError: invalid syntax <em></em>
        </p>
      </td>
      <td>
        <p>Week 1</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>
          <strong>NameError </strong>NameError is produced variable(s) were not defined
        </p>
      </td>
      <td>
        <p>
          <em># NameError </em>print(result)
        </p>
      </td>
      <td>
        <p>Week 1</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>
          <strong>SyntaxError</strong>
        </p>
        <p>SyntaxError is produced when Python syntax is not followed</p>
      </td>
      <td>
        <p>
          <em># SyntaxError</em>
        </p>
        <p>result = 'Wrong quotes"</p>
      </td>
      <td>
        <p>Week 1</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>
          <strong>ZeroDivisionError </strong>ZeroDivisionError occurs when a number (denominator) is divided by a 0 or 0.0
        </p>
      </td>
      <td>
        <p>
          <em>#ZeroDivisionError</em>
        </p>
        <p>numerator = 50</p>
        <p>denominator = 0</p>
        <p>result = numerator / denominator print(result)</p>
      </td>
      <td>
        <p>Week 1</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>
          <strong>Boolean - False</strong>
        </p>
      </td>
      <td>
        <p>Empty, False, 0 None</p>
      </td>
      <td>
        <p>Week 2</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>
          <strong>Boolean – True</strong>
        </p>
      </td>
      <td>
        <p>Any number (beside 0), True, String(that is not empty)</p>
      </td>
      <td>
        <p>Week 2</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Equals and Not Equals</p>
      </td>
      <td>
        <p>test = ""</p>
        <p>print(bool(test)) <em># False</em>
        </p>
        <p>'13' == 13 <em># False</em>
        </p>
      </td>
      <td>
        <p>Week 2</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>If Statement</p>
      </td>
      <td>
        <p>day = 'Monday' <em># Enter day here</em>
        </p>
        <p>if day == 'Monday':</p>
        <p>print('attend the Workshop')</p>
      </td>
      <td>
        <p>Week 2</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Ask for User input</p>
      </td>
      <td>
        <p>print('Enter your age: ')</p>
        <p>age = input() <em># stores String</em>
        </p>
        <p>age = int(age) <em># converts to int</em>
        </p>
      </td>
      <td>
        <p>Week 2</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Logical Operators</p>
        <p>1. and</p>
        <p>2. or</p>
        <p>3. not</p>
      </td>
      <td>
        <table>
          <tbody>
            <tr>
              <th>
                <p>First Condition</p>
              </th>
              <th>
                <p>Second Condition</p>
              </th>
              <th>
                <p>Output</p>
              </th>
            </tr>
            <tr>
              <td>
                <p>F</p>
              </td>
              <td>
                <p>F</p>
              </td>
              <td>
                <p>F</p>
              </td>
            </tr>
            <tr>
              <td>
                <p>F</p>
              </td>
              <td>
                <p>T</p>
              </td>
              <td>
                <p>F</p>
              </td>
            </tr>
            <tr>
              <td>
                <p>T</p>
              </td>
              <td>
                <p>F</p>
              </td>
              <td>
                <p>F</p>
              </td>
            </tr>
            <tr>
              <td>
                <p>T</p>
              </td>
              <td>
                <p>T</p>
              </td>
              <td>
                <p>
                  <strong>T</strong>
                </p>
              </td>
            </tr>
          </tbody>
        </table>
      </td>
      <td>
        <p>Week 2</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Logical operator: not</p>
      </td>
      <td>
        <p>print(not True) <em># prints False</em>
        </p>
        <p>print(not False) <em># prints True</em>
        </p>
      </td>
      <td>
        <p>Week 2</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Else statement</p>
      </td>
      <td>
        <p>credits = 35 <em># Modify credits value here</em>
        </p>
        <p>if credits &gt;= 1000:</p>
        <p>print("You are a Platinum member")</p>
        <p>elif credits &gt;= 500:</p>
        <p>print("You are a Gold member")</p>
        <p>elif credits &gt;= 250:</p>
        <p>print("You are a Silver member")</p>
        <p>else:</p>
        <p>print("You are a Red member")</p>
      </td>
      <td>
        <p>Week 2</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Loops</p>
        <p>(1) initialisation;</p>
        <p>(2) repetitions;</p>
        <p>(3) an ending condition</p>
      </td>
      <td>
        <p>Iteration</p>
        <ol>
          <li>Indefinite: where the number of times a loop is executed depends on the number of times a condition is met</li>
          <li>Definite: where the number of times a loop will be executed is declared in-advance</li>
        </ol>
      </td>
      <td>
        <p>Week 3</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Loops</p>
        <p>typically utilised to iterate a</p>
        <p>collection of items</p>
      </td>
      <td>
        <p>grades = [35, 50, 65, 85]</p>
        <p>print(grades[0]) <em># 35</em>
        </p>
        <p>print(grades[1]) <em># 50</em>
        </p>
        <p>print(grades[2]) <em># 65</em>
        </p>
        <p>print(grades[3]) <em># 85</em>
        </p>
      </td>
      <td>
        <p>Week 3</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>For Loops</p>
        <ul>
          <li>a type of definite iteration</li>
          <li>which will know how many times to iterate the loop because our grades list contains a collection of elements or items with a predefined length</li>
        </ul>
      </td>
      <td>
        <p>for &lt;temp var&gt; in &lt;collection&gt;:</p>
        <p>&lt;action&gt;</p>
        <p>grades = [35, 50, 65, 85]</p>
        <p>for g in grades:</p>
        <p>
          <em>#Any code at this indentation</em>
        </p>
        <p>
          <em>#will be executed on each</em>
        </p>
        <p>
          <em>#iteration of the loop</em>
        </p>
        <p>print(g)</p>
        <p>
          <em>1. g is the &lt;temp var&gt;</em>
        </p>
        <p>
          <em>2. grades list is the &lt;collection&gt;</em>
        </p>
        <p>
          <em>3. print(g) is the &lt;action&gt; completed on every</em>
        </p>
        <p>
          <em>iteration using the temporary variable g</em>
        </p>
      </td>
      <td>
        <p>Week 3</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>One line for loops</p>
      </td>
      <td>
        <p>grades = [35, 50, 65, 85]</p>
        <p>for g in grades: print(g)</p>
      </td>
      <td>
        <p>Week 3</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Using Range in For Loops</p>
      </td>
      <td>
        <p>for temp in range(11):</p>
        <p>
          <em>#Iterates 11 times, from 0 to 10</em>
        </p>
        <p>
          <em>#temp does nothing, but print</em>
        </p>
        <p>
          <em>#statement repeats the message</em>
        </p>
        <p>
          <em># </em>
          <em>range(11) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]</em>
        </p>
        <p>print('I must attend my workshops')</p>
        <p>for temp in range(11):</p>
        <p>print('Iteration number is: ' + str(temp))</p>
        <p>
          <em>#Output:</em>
        </p>
        <p>
          <em>#Iteration number is: 0</em>
        </p>
        <p>
          <em>#Iteration number is: 1</em>
        </p>
        <p>
          <em>#Iteration number is: 2</em>
        </p>
        <p>
          <em>#Iteration number is: 3</em>
        </p>
        <p>
          <em>#Iteration number is: 4</em>
        </p>
        <p>
          <em>#Iteration number is: 5</em>
        </p>
        <p>
          <em>#Iteration number is: 6</em>
        </p>
        <p>
          <em>#Iteration number is: 7</em>
        </p>
        <p>
          <em>#Iteration number is: 8</em>
        </p>
        <p>
          <em>#Iteration number is: 9</em>
        </p>
        <p>
          <em>#Iteration number is: 10</em>
        </p>
      </td>
      <td>
        <p>Week 3</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>While Loops</p>
      </td>
      <td>
        <p>while &lt;conditional statement&gt;:</p>
        <p>&lt;action&gt;</p>
        <p>iteration = 0</p>
        <p>while iteration &lt; 11:</p>
        <p>print('Iteration number is: ' + str(iteration))</p>
        <p>iteration = iteration + 1</p>
        <p>grades = [35, 50, 65, 85]</p>
        <p>iteration = 0</p>
        <p>while iteration &lt; len(grades):</p>
        <p>print(grades[iteration])</p>
        <p>iteration = iteration + 1</p>
      </td>
      <td>
        <p>Week 3</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Loop Control</p>
        <p>1. Break</p>
      </td>
      <td>
        <p>grades = [35, 50, 65, 85]</p>
        <p>for grade in grades:</p>
        <p>pass</p>
        <p>grades = [35, 50, 65, 85]</p>
        <p>for grade in grades:</p>
        <p>print(grade)</p>
        <p>if grade &lt; 50:</p>
        <p>break</p>
        <p>
          <em># prints 35 because the break</em>
        </p>
        <p>
          <em># is after the print function</em>
        </p>
      </td>
      <td>
        <p>Week 3</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Loop Control</p>
        <p>2. Continue</p>
      </td>
      <td>
        <p>grades = [35, 50, 65, 85]</p>
        <p>for grade in grades:</p>
        <p>if grade &lt; 50:</p>
        <p>continue</p>
        <p>print(grade)</p>
        <p>
          <em># prints 50, 65, 85</em>
        </p>
        <p>
          <em># Order of "continue" before</em>
        </p>
        <p>
          <em># print function is important</em>
        </p>
      </td>
      <td>
        <p>Week 3</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Loop Control</p>
        <p>3. Else</p>
      </td>
      <td>
        <p>grades = [35, 50, 65, 85]</p>
        <p>for grade in grades:</p>
        <p>print(grade)</p>
        <p>else:</p>
        <p>print('Completed the grades for loop.')</p>
        <p>
          <em>"""</em>
        </p>
        <p>
          <em>prints</em>
        </p>
        <p>
          <em>35</em>
        </p>
        <p>
          <em>50</em>
        </p>
        <p>
          <em>65</em>
        </p>
        <p>
          <em>85</em>
        </p>
        <p>
          <em>Completed the for grades for loop.</em>
        </p>
        <p>
          <em>"""</em>
        </p>
      </td>
      <td>
        <p>Week 3</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Nested Loops</p>
      </td>
      <td>
        <p>gradebook = [</p>
        <p>['Jing', 35],</p>
        <p>['Jim', 50],</p>
        <p>['Kerrie', 65],</p>
        <p>['Rakesh', 85]</p>
        <p>]</p>
        <p>for student in gradebook</p>
        <p>print(student)</p>
        <p>for detail in student</p>
        <p>print(details)</p>
      </td>
      <td>
        <p>Week 3</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>List Comprehension</p>
      </td>
      <td>
        <p>
          <em># Assuming if there is a &lt;conditional statement&gt;</em>
        </p>
        <p>new_list = [&lt;expression&gt; for &lt;temp var&gt; in &lt;collection&gt; &lt;conditional statement&gt;]</p>
        <p># If there isn't a &lt;conditional statement&gt;</p>
        <p>new_list = [&lt;expression&gt; for &lt;temp var&gt; in &lt;collection&gt;]</p>
        <p>students = ['Jing', 'Jim', 'Kerrie', 'Rakesh']</p>
        <p>new_list = [name for name in students if 'i' in name]</p>
        <p>
          <em>For example, creating a new_list list with values from 0 to 10:</em>
        </p>
        <p>new_list = [i for i in range(11)]</p>
        <p>
          <em>For example, creating a new_list list with values from 0 to 10, but only including values 6 and above:</em>
        </p>
        <p>new_list = [i for i in range(11) if i &gt; 5]</p>
      </td>
      <td>
        <p>Week 3</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Summary of Python collections</p>
      </td>
      <td>
        <p>1. List: “is a collection which is <strong>ordered</strong> and <strong>changeable(Mutable)</strong>. </p>
        <p>Allows duplicate members.”</p>
        <p>2. Tuple: “is a collection which is <strong>ordered</strong> and <strong>unchangeable</strong>. </p>
        <p>Allows duplicate members.”</p>
        <p>3. Set: “is a collection which is <strong>unordered</strong>, <strong>unchangeable</strong>*, and </p>
        <p>unindexed. No duplicate members.”</p>
        <p>4. Dictionary: “is a collection which is <strong>ordered</strong>** and </p>
        <p>
          <strong>changeable(Mutable)</strong>. No duplicate members.”
        </p>
      </td>
      <td>
        <p>Week 4</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>List</p>
        <ul>
          <li>list is created using square brackets []</li>
          <li>Each item is separated by a comma , <ul>
              <li>Good Python practice: insert a space after each comma</li>
            </ul>
          </li>
          <li>store a combination of different data types</li>
        </ul>
      </td>
      <td>
        <p>list = ["String", 27, False, 25.65, [1, 2, 3, 4, "Count"], None]</p>
        <p>
          <em># Create an empty list</em>
        </p>
        <p>list_empty = []</p>
        <p>list_empty = list(())</p>
      </td>
      <td>
        <p>Week 4</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>List Methods / Class</p>
      </td>
      <td>
        <p>
          <em># list_name is our list</em>
        </p>
        <p>
          <em># .method() is a method of our list</em>
        </p>
        <p>
          <em># This example is for structure illustration,</em>
        </p>
        <p>
          <em># it will not work</em>
        </p>
        <p>list_name.method()</p>
        <p>AttributeError: 'list' object has no attribute 'method'</p>
        <p>
          <em># Syntax for List methods</em>
        </p>
        <p>list.method(parameter)</p>
      </td>
      <td>
        <p>Week 4</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Reference</p>
        <p>Check Methods - Documentation</p>
      </td>
      <td>
        <p>Use the following official website:</p>
        <p>1. Official Python Docs:</p>
        <p>
          <a href="https://docs.python.org/3/tutorial/datastructures.html">https://docs.python.org/3/tutorial/datastructures.html</a>
        </p>
        <p>• Use any other unofficial websites:</p>
        <p>2. W3Schools Docs:</p>
        <p>
          <a href="https://www.w3schools.com/python/python_ref_list.asp">https://www.w3schools.com/python/python_ref_list.asp</a>
        </p>
        <p>3. GeeksforGeeks Docs:</p>
        <p>
          <a href="https://www.geeksforgeeks.org/list-methods-in-python/">https://www.geeksforgeeks.org/list-methods-in-python/</a>
        </p>
      </td>
      <td>
        <p>Week 4</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>List Method: .append()</p>
        <p>adds an element to the end of a list</p>
      </td>
      <td>
        <p>grades = [35, 50, 65, 85]</p>
        <p>grades.append(67)</p>
        <p>print(grades) <em># Prints [35, 50, 65, 85, 67]</em>
        </p>
      </td>
      <td>
        <p>Week 4</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Adding multiple items to a list</p>
      </td>
      <td>
        <p>grades = [35, 50, 65, 85, 67]</p>
        <p>grades += [76, 78, 52] <em># OR grades = grades + [76, 78, 52]</em>
        </p>
        <p>grades.extend([68, 72]) <em># square brackets are used here and above</em>
        </p>
        <p>print(grades) <em># prints [35, 50, 65, 85, 67, 76, 78, 52, 68, 72]</em>
        </p>
      </td>
      <td>
        <p>Week 4</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Accessing list elements</p>
        <ul>
          <li>the first element in a list has an index of 0</li>
          <li>Negative index can be used to access last element(s) of a list</li>
        </ul>
      </td>
      <td>
        <p>students = ['Jing', 'Jim', 'Kerrie', 'Rakesh']</p>
        <p>print(students[1]) <em># prints Jim</em>
        </p>
        <p>print(students[-1]) <em># prints Rakesh</em>
        </p>
        <table>
          <tbody>
            <tr>
              <th>
                <p>Element</p>
              </th>
              <th>
                <p>Index</p>
              </th>
              <th>
                <p>Negative Index</p>
              </th>
            </tr>
            <tr>
              <td>
                <p>'Jing'</p>
              </td>
              <td>
                <p>0</p>
              </td>
              <td>
                <p>-4</p>
              </td>
            </tr>
            <tr>
              <td>
                <p>'Jim'</p>
              </td>
              <td>
                <p>1</p>
              </td>
              <td>
                <p>-3</p>
              </td>
            </tr>
            <tr>
              <td>
                <p>'Kerrie'</p>
              </td>
              <td>
                <p>2</p>
              </td>
              <td>
                <p>-2</p>
              </td>
            </tr>
            <tr>
              <td>
                <p>'Rakesh'</p>
              </td>
              <td>
                <p>3</p>
              </td>
              <td>
                <p>-1</p>
              </td>
            </tr>
          </tbody>
        </table>
      </td>
      <td>
        <p>Week 4</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Length</p>
        <ul>
          <li>len() function returns the number of items* in a object*</li>
        </ul>
      </td>
      <td>
        <p>students = ['Jing', 'Jim', 'Kerrie', 'Rakesh']</p>
        <p>print(len(students)) <em># prints 4</em>
        </p>
        <p>guess = 'Howmansafayhschatersarehere can you guess? :-)'</p>
        <p>print(len(guess)) <em># prints 46</em>
        </p>
      </td>
      <td>
        <p>Week 4</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Remove list elements</p>
        <p>1. grades.remove(value)</p>
        <p>2. grades.pop(specific_index)</p>
        <p>3. del grades[specific_index]</p>
      </td>
      <td>
        <p>grades = [35, 50, 65, 85]</p>
        <p>grades.remove(35)</p>
        <p>print(grades) <em># prints [50, 65, 85]</em>
        </p>
        <p>grades = [35, 50, 65, 85]</p>
        <p>grades.pop(0)</p>
        <p>print(grades) <em># prints [50, 65, 85]</em>
        </p>
        <p>grades = [35, 50, 65, 85]</p>
        <p>del grades[0]</p>
        <p>print(grades) <em># prints [50, 65, 85]</em>
        </p>
      </td>
      <td>
        <p>Week 4</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Two Dimensional (2D) Lists</p>
        <p>– Known as a nested list – this logic can be applied to create a three dimensional (3D) list</p>
      </td>
      <td>
        <p>gradebook = [['Jing', 35], ['Jim', 50], ['Kerrie', 65], ['Rakesh', 85]]</p>
        <p>gradebook = [</p>
        <p>['Jing', 35],</p>
        <p>['Jim', 50],</p>
        <p>['Kerrie', 65],</p>
        <p>['Rakesh', 85]</p>
        <p>]</p>
        <p>print(gradebook[-1][1]) <em># prints 85</em>
        </p>
        <p>gradebook[0][1] = 35</p>
        <p>gradebook[-4][1] = 35</p>
        <p>gradebook[-4][-1] = 35</p>
      </td>
      <td>
        <p>Week 4</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Zip</p>
        <ul>
          <li>joins lists together. Extremely powerful!</li>
          <li>If zip parameters – or iterators – lengths are different, than the iterator with the least element determines the length of the new iterator</li>
        </ul>
      </td>
      <td>
        <p>students = ['Jing', 'Jim', 'Kerrie', 'Rakesh' , 'Candy']</p>
        <p>grades = [35, 50, 65, 85]</p>
        <p>gradebook_zip = list(zip(students, grades))</p>
        <p>
          <em># print(gradebook_zip) # zip creation - note the tuples</em>
        </p>
        <p>
          <em># [('Jing', 35), ('Jim', 50), ('Kerrie', 65), ('Rakesh', 85)]</em>
        </p>
        <p>
          <em># print(gradebook) # original</em>
        </p>
        <p>
          <em># [['Jing', 35], ['Jim', 50], ['Kerrie', 65], ['Rakesh', 85]]</em>
        </p>
        <p>
          <em># </em>
          <em>"Candy" will be disappeared</em>
        </p>
      </td>
      <td>
        <p>Week 4</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Tuples</p>
        <ul>
          <li>do the same operation as Lists</li>
          <li>Tuples are unchangeable</li>
          <li>However, instead declaring using square brackets</li>
          <li>[] like Lists, it uses round brackets ()</li>
        </ul>
      </td>
      <td>
        <ol>
          <li>.count(): returns the number of times the specified element appears in the list</li>
          <li>.insert(): inserts the specified value at the specified position</li>
          <li>.sort(): sorts the list ascending by</li>
        </ol>
        <p>default</p>
        <ol>
          <li>.sorted(): returns a sorted list of the specified iterable object</li>
        </ol>
      </td>
      <td>
        <p>Week 4</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Built-in function</p>
      </td>
      <td>
        <p>
          <em># Syntax for a built-in function</em>
        </p>
        <p>builtinfuncion(parameter)</p>
      </td>
      <td>
        <p>Week 4</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Range</p>
      </td>
      <td>
        <p>numbers = [0, 1, 2, 3, 4, 5]</p>
      </td>
      <td>
        <p>Week 4</p>
      </td>
    </tr>
    <tr>
      <td></td>
      <td>
        <ol>
          <li>0 to 5</li>
        </ol>
        <p>range(6)</p>
        <ol>
          <li>(2) 0 to 999</li>
        </ol>
        <p>range(1000)</p>
      </td>
      <td>
        <p>Week 4</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Reference</p>
        <p>Range</p>
      </td>
      <td>
        <p>W3Schools:</p>
        <p>
          <a href="https://www.w3schools.com/python/ref_func_range.asp">https://www.w3schools.com/python/ref_func_range.asp</a>
        </p>
        <p>even sequence of numbers ranging from -255 to 255</p>
        <p>ans = list(range(-254, 256, 2))</p>
        <p>print(list(range(-10, 10, 2)))</p>
        <p>
          <em># [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8]</em>
        </p>
        <p>print(list(range(-10, 10, 3)))</p>
        <p>
          <em># [-10, -7, -4, -1, 2, 5, 8]</em>
        </p>
        <p>print(list(range(0, 10, 3)))</p>
        <p>
          <em># [0, 3, 6, 9]</em>
        </p>
      </td>
      <td>
        <p>Week 4</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Slicing Lists</p>
      </td>
      <td>
        <p>nums[start:end]</p>
        <p>nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]</p>
        <p>len(nums) = 9</p>
        <p>nums[2:7] <em># For i = 2 ; i &lt; 7</em>
        </p>
        <p>nums[:n] <em># For i = 0 ; i = n</em>
        </p>
        <p>nums[:3] <em># For i = 0 ; i = 3</em>
        </p>
        <p>nums[n:] <em># For i = len(nums)-n ; i &lt; len(nums)</em>
        </p>
        <p>nums[-6:] <em># For i = len(nums)-6 ; i &lt; len(nums)</em>
        </p>
        <p>
          <em># [3, 4, 5, 6, 7, 8]</em>
        </p>
      </td>
      <td>
        <p>Week 4</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Sets</p>
        <p>using curly brackets {}</p>
        <p>1. Set items are unchangeable</p>
        <p>a) The exception: add and remove items allowed</p>
        <p>2. Set items are unordered – items can’t be indexed as there’s no structure</p>
      </td>
      <td>
        <p>
          <em># prints {65, 50, 35, 85}</em>
        </p>
        <p>grades_set = {35, 50, 65, 85, 85, 85}</p>
        <p>print(grades_set)</p>
      </td>
      <td>
        <p>Week 4</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Dictionary</p>
        <p>using curly brackets {}, but store data values in key:value pairs</p>
      </td>
      <td>
        <p>gradebook_dict = {</p>
        <p>'Jing': {</p>
        <p>'address': 'Fake Rd',</p>
        <p>'student_id': 12345,</p>
        <p>'ass1_grade': 20,</p>
        <p>'ass2_grade': 15,</p>
        <p>'ass3_grade': 0,</p>
        <p>'final_grade': 35</p>
        <p>},</p>
        <p>'Jim': 50,</p>
        <p>'Kerrie': 65,</p>
        <p>'Rakesh': 85</p>
        <p>}</p>
        <p>print(gradebook_dict['Jing']) <em># prints {'address': 'Fake Rd', 'student_id': 12345, 'ass1_grade': 20, 'ass2_grade': 15, 'ass3_grade': 0, 'final_grade': 35}</em>
        </p>
      </td>
      <td>
        <p>Week 4</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>User Defined Functions</p>
      </td>
      <td>
        <p>def function_name(first_parameter):</p>
        <p>pass</p>
      </td>
      <td>
        <p>Week 5</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Functions</p>
        <ul>
          <li>Arguments</li>
        </ul>
      </td>
      <td>
        <p>def print_hello(name):</p>
        <p>print('Welcome ' + name + ' to print_hello function')</p>
        <p>print_hello('Mark') # OR print_hello(name = 'Mark')</p>
        <p>
          <em># prints Welcome Mark to print_hello function</em>
        </p>
      </td>
      <td>
        <p>Week 5</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Functions</p>
        <ul>
          <li>Multiple parameters and multiple arguments</li>
        </ul>
      </td>
      <td>
        <p>def print_hello(name, surname):</p>
        <p>print('Welcome ' + name + ' ' + surname + ' to print_hello function')</p>
        <p>
          <em># prints Welcome Mark Smith to print_hello function</em>
        </p>
        <p>print_hello('Mark', 'Smith')</p>
        <p>
          <em># OR print_hello(name = 'Mark', surname = 'Smith')</em>
        </p>
        <p>
          <em># OR print_hello(surname = 'Smith', name = 'Mark')</em>
        </p>
      </td>
      <td>
        <p>Week 5</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Functions</p>
        <ul>
          <li>Returns</li>
          <li>Multiple Returns</li>
        </ul>
      </td>
      <td>
        <p>def find_max(numbers):</p>
        <p>max_value = numbers[0] <em># Initialise the max value to the first number in the list</em>
        </p>
        <p>for num in numbers:</p>
        <p>if num &gt; max_value:</p>
        <p>max_value = num <em># Update the max value if the current number is greater</em>
        </p>
        <p>return max_value</p>
        <p>numbers = [3, 6, 2, 8, 4, 10, 1</p>
        <p>max_num = find_max(numbers)</p>
        <p>print(max_num) <em># Output: 10</em>
        </p>
        <p>def exchange_usd_to_aud(usd_amount, exchange_rate):</p>
        <p>return usd_amount * exchange_rate</p>
        <p>aud_amount = exchange_usd_to_aud(100, 1.433)</p>
        <p>print('100 US dollars would give: ' + str(aud_amount) + ' AUD dollars')</p>
        <p>
          <em># prints 100 US dollars would give: 143.3 AUD dollars</em>
        </p>
        <p>weather_data = [37, 23, 30]</p>
        <p>def weather_report(weather):</p>
        <p>first = 'Today: ' + str(weather[0])</p>
        <p>second = 'Tomorrow: ' + str(weather[1])</p>
        <p>third = 'Two days after: ' + str(weather[2])</p>
        <p>return first, second, third</p>
        <p>monday, tuesday, wednesday = weather_report(weather_data)</p>
        <p>
          <em># monday = 'Today: 37'</em>
        </p>
        <p>
          <em># tuesday = 'Tomorrow: 23'</em>
        </p>
        <p>
          <em># wednesday = 'Two days after: 30'</em>
        </p>
      </td>
      <td>
        <p>Week 5</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Types of Arguments</p>
        <ol>
          <li>Positional arguments:</li>
        </ol>
        <p>arguments that are called by their position in the function definition</p>
        <ol>
          <li>Keyword arguments:</li>
        </ol>
        <p>arguments that are called by their name</p>
        <ol>
          <li>Default arguments:</li>
        </ol>
        <p>arguments that are given default values</p>
      </td>
      <td>
        <p>def travel_cost(destination_km, price_per_km):</p>
        <p>return destination_km * price_per_km</p>
        <ol>
          <li>Positional arguments:</li>
        </ol>
        <p>travel_cost(15, 5)</p>
        <ol>
          <li>Keyword arguments:</li>
        </ol>
        <p>travel_cost(destination_km = 15, price_per_km = 15)</p>
        <p>def travel_cost(destination_km, price_per_km = 5):</p>
        <p>return destination_km * price_per_km</p>
        <ol>
          <li>Default arguments:</li>
        </ol>
        <p>travel_cost(15)</p>
        <p>savings = 1000</p>
        <p>def travel_cost(destination_km, price_per_km = 5):</p>
        <p>print('Your savings is: ' + str(savings))</p>
        <p>print('Destination (in km) provided: ' + str(destination_km))</p>
        <p>print('Total cost: ' + str(destination_km * price_per_km))</p>
        <p>print(savings)</p>
        <p>travel_cost(20)</p>
        <p>
          <em># 1000</em>
        </p>
        <p>
          <em># Your savings is: 1000</em>
        </p>
        <p>
          <em># Destination (in km) provided: 20</em>
        </p>
        <p>
          <em># Total cost: 100</em>
        </p>
      </td>
      <td>
        <p>Week 5</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Built-in Functions</p>
      </td>
      <td>
        <p>print()</p>
      </td>
      <td>
        <p>Week 5</p>
      </td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
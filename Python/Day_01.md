🐍 Python 50 Days — Day 01

Python Fundamentals

---

🎯 Agenda

Today we will understand:

1. What is Python?
2. Python applications
3. Variables
4. Data types
5. Dynamic typing
6. Static typing
7. "print()"
8. "input()"
9. Type conversion
10. Arithmetic operators
11. Comparison operators
12. Logical operators
13. "if / elif / else"
14. Compiler vs Interpreter
15. How Python executes code

---

1. What is Python?

Python is a high-level, general-purpose programming language known for its simple syntax and readability.

Why Python is popular

- Easy to learn
- Easy to read and maintain
- Large standard library
- Huge ecosystem of third-party libraries
- Useful for automation and scripting
- Strong support for data processing
- Widely used in DevOps, testing, APIs and ETL
- Used extensively in data science and AI

Python applications

Automation
Data Processing
ETL
Data Analysis
API Development
Testing
DevOps
Financial Applications
Machine Learning

---

2. Python Program — First Example

print("Hello World")

"print()" is used to display information on the screen.

Example:

print("Welcome to Python")
print(100)
print(10.5)

---

3. Variables

A variable is a name that refers to a value/object.

Example:

name = "Veera"
age = 35
salary = 140000

Conceptually:

name   → "Veera"
age    → 35
salary → 140000

Python does not normally require explicit type declaration.

salary = 140000

We don't need to write:

int salary = 140000

This is one reason Python is considered dynamically typed.

---

4. Variable Naming Rules

Valid examples:

salary = 140000
employee_name = "Veera"
loan_amount = 500000
salary1 = 150000

Invalid:

1salary = 140000

A variable name cannot start with a number.

Also:

employee-name = "Veera"

should not be used because "-" represents subtraction.

Recommended practice

Use meaningful names:

monthly_salary = 140000
loan_amount = 500000
credit_score = 780

rather than:

x = 140000
a = 500000
b = 780

---

5. Basic Python Data Types

A data type tells us what kind of value we are working with.

Data Type| Example| Description
"int"| "100"| Whole number
"float"| "10.5"| Decimal number
"str"| ""Python""| Text
"bool"| "True" / "False"| Boolean value

Integer

age = 35

Type:

int

Float

interest_rate = 8.5

Type:

float

String

name = "Veera"

Type:

str

Boolean

loan_approved = True

Type:

bool

---

6. Checking Data Type

Python provides the "type()" function.

salary = 140000

print(type(salary))

Output:

<class 'int'>

Example:

interest_rate = 8.5
print(type(interest_rate))

Output:

<class 'float'>

---

7. Dynamic Typing

Python is a dynamically typed language.

This means we don't normally declare a variable's type explicitly, and type checking occurs during program execution.

Example:

x = 100

x = "Hello"

The name "x" can be rebound to an object of another type.

x = 100
print(type(x))

x = "Hello"
print(type(x))

Output:

<class 'int'>
<class 'str'>

Remember

«Dynamic typing → type checking mainly happens at runtime.»

Python still has types. It simply doesn't require us to explicitly declare the type of every variable.

---

8. Static Typing

In a statically typed language, types are generally known and checked at compile time.

Example in Java:

int salary = 140000;

Here "salary" is declared as an integer.

This is not valid:

int salary = 140000;
salary = "Hello";

because a string cannot be assigned to an integer variable.

Remember

«Static typing → type checking mainly happens at compile time.»

---

9. Static vs Dynamic Typing

Feature| Static Typing| Dynamic Typing
Type checking| Mainly compile time| Mainly runtime
Explicit type declaration| Common| Usually not required
Variable can refer to different types| Generally restricted| Yes
Examples| Java, C, C++| Python, JavaScript

Easy memory trick

STATIC  → Check type before running
DYNAMIC → Check type while running

---

10. "input()"

"input()" is used to receive input from the user.

Example:

name = input("Enter your name: ")

print(name)

Important

"input()" always returns a string.

For example:

age = input("Enter your age: ")

If the user enters:

35

Python initially receives:

"35"

not:

35

---

11. Type Conversion

We can convert one type into another.

Common functions:

int()
float()
str()
bool()

Example:

age = int(input("Enter your age: "))

Now "age" is an integer.

Another example:

salary = float(input("Enter salary: "))

Example

salary = "140000"

salary = int(salary)

print(salary + 10000)

Output:

150000

---

12. Arithmetic Operators

Python supports normal mathematical operations.

Operator| Meaning| Example
"+"| Addition| "10 + 5"
"-"| Subtraction| "10 - 5"
"*"| Multiplication| "10 * 5"
"/"| Division| "10 / 5"
"%"| Remainder| "10 % 3"
"//"| Floor division| "10 // 3"
"**"| Power| "10 ** 2"

Example:

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)

---

13. Comparison Operators

Comparison operators compare values and return:

True
False

Operator| Meaning
">"| Greater than
"<"| Less than
">="| Greater than or equal
"<="| Less than or equal
"=="| Equal to
"!="| Not equal to

Example:

salary = 140000

print(salary > 100000)
print(salary == 140000)
print(salary != 50000)

---

14. "=" vs "=="

This is extremely important.

"="

Used for assignment.

salary = 140000

Meaning:

«Assign "140000" to "salary".»

"=="

Used for comparison.

salary == 140000

Meaning:

«Check whether salary is equal to "140000".»

Example:

salary = 140000

print(salary == 140000)

Output:

True

---

15. Logical Operators

Python provides:

and
or
not

"and"

Both conditions must be true.

salary = 140000
experience = 6

print(salary >= 100000 and experience >= 5)

Result:

True

---

"or"

At least one condition must be true.

salary = 80000
experience = 6

print(salary >= 100000 or experience >= 5)

Result:

True

---

"not"

Reverses a Boolean result.

loan_approved = True

print(not loan_approved)

Result:

False

---

16. "if" Statement

An "if" statement is used to make a decision.

Example:

salary = 140000

if salary >= 100000:
    print("Eligible")

If the condition is "True", the indented code executes.

Important

Python uses indentation to define a block.

if salary >= 100000:
    print("Eligible")

The ":" and indentation are important.

---

17. "if / else"

Used when there are two possible outcomes.

salary = 80000

if salary >= 100000:
    print("Eligible")
else:
    print("Not Eligible")

Output:

Not Eligible

---

18. "if / elif / else"

Used when there are multiple conditions.

salary = 140000

if salary >= 150000:
    print("High Income")
elif salary >= 100000:
    print("Medium Income")
else:
    print("Lower Income")

Output:

Medium Income

Python checks the conditions from top to bottom.

---

19. Nested "if"

An "if" statement can exist inside another "if".

Example:

salary = 140000
credit_score = 780

if salary >= 100000:
    if credit_score >= 750:
        print("Loan Eligible")

The second condition is checked only when the first condition is true.

---

20. Banking Example

salary = 140000
rent = 16500
emi = 53713
other_emi = 17550

total_expenses = rent + emi + other_emi
remaining_salary = salary - total_expenses

print("Total Expenses:", total_expenses)
print("Remaining Salary:", remaining_salary)

if remaining_salary >= 50000:
    print("Comfortable")
elif remaining_salary >= 30000:
    print("Manageable")
else:
    print("Tight")

Expected result:

Total Expenses: 87763
Remaining Salary: 52237
Comfortable

This combines:

Variables
+
Arithmetic
+
Comparison
+
Conditions

---

21. Comments

Comments are used to explain code.

# Monthly salary
salary = 140000

# Monthly EMI
emi = 53713

Python ignores comments during execution.

---

22. Compiler

A compiler translates source code into another executable form, typically before execution.

Conceptually:

Source Code
     ↓
Compiler
     ↓
Machine / Executable Code
     ↓
CPU
     ↓
Result

Languages such as C are commonly described as compiled languages.

---

23. Interpreter

An interpreter/runtime executes program instructions through a runtime system rather than relying solely on a traditional ahead-of-time native executable.

Conceptually:

Source Code
     ↓
Interpreter / Runtime
     ↓
Execution
     ↓
Result

---

24. How Python Executes

It is common to hear:

«"Python is an interpreted language."»

This is useful at a beginner level, but it is an oversimplification.

With the standard CPython implementation:

Python Source Code
        ↓
    Compilation
        ↓
     Bytecode
        ↓
Python Virtual Machine
        ↓
    Execution

Therefore:

«Python source code is compiled to bytecode and that bytecode is executed by the Python runtime.»

---

25. Compiler vs Interpreter — Quick Comparison

Compiler| Interpreter / Runtime
Translation generally happens before execution| Execution happens through the runtime
Often produces executable/native code| Executes instructions through a runtime
Compilation errors can prevent execution| Errors can appear during execution
C is a common example| Python is commonly described this way

Important

Do not memorize:

Python = No Compiler

Instead remember:

CPython:
Source → Bytecode → Python Virtual Machine → Execution

---

⚡ QUICK REMINDER — DAY 01

🧠 Core Concepts

Python
  ↓
Variables
  ↓
Data Types
  ↓
Operators
  ↓
Conditions

Variables

name = "Veera"
age = 35
salary = 140000

Data Types

int
float
str
bool

Type

type(value)

Input

input()

Remember:

input() → string

Conversion

int()
float()
str()
bool()

Assignment vs Comparison

=   → Assignment
==  → Comparison

Logical Operators

and → all required conditions must be True
or  → at least one condition must be True
not → reverses True/False

Conditions

if condition:
    ...

elif condition:
    ...

else:
    ...

Typing

Static  → type checked mainly at compile time
Dynamic → type checked mainly at runtime

Python

Dynamically Typed

CPython Execution

Source
  ↓
Bytecode
  ↓
Python Virtual Machine
  ↓
Execution

---

🎤 INTERVIEW QUICK REVISION

What is Python?

A high-level, general-purpose programming language known for readability and a large ecosystem.

Is Python dynamically typed?

Yes. Python is dynamically typed; type checking primarily occurs at runtime and variable names can be rebound to objects of different types.

What is static typing?

A typing approach where types are generally checked at compile time.

What does "input()" return?

A string.

Difference between "=" and "=="?

"=" performs assignment.
"==" performs equality comparison.

What does "type()" do?

It returns the type of an object.

Is Python compiled or interpreted?

CPython compiles Python source into bytecode, which is then executed by the Python virtual machine. Python is commonly described as interpreted because of this runtime execution model.

---

🏦 Banking / Data Engineering Connection

The concepts from Day 01 will become building blocks for later work:

Variables
    ↓
Process trade / transaction values

Data Types
    ↓
Handle amounts, dates, strings, flags

Conditions
    ↓
Validation / business rules

Operators
    ↓
Calculations / reconciliations

Input
    ↓
Files / user input / APIs / database data

Python
    ↓
Automation
    ↓
ETL
    ↓
Data Mart
    ↓
Production Support

---

✅ Day 01 Completion Checklist

- [ ] Understand Python
- [ ] Understand variables
- [ ] Understand basic data types
- [ ] Understand dynamic typing
- [ ] Understand static typing
- [ ] Understand "print()"
- [ ] Understand "input()"
- [ ] Understand type conversion
- [ ] Practice arithmetic operators
- [ ] Practice comparison operators
- [ ] Practice logical operators
- [ ] Practice "if / elif / else"
- [ ] Understand compiler vs interpreter
- [ ] Understand basic CPython execution
- [ ] Complete Day 01 challenges
- [ ] Review interview questions

Next: Day 01 challenges → solve independently → review → Day 02.

🐍 Python 50 Days — Chapter 01: Python Fundamentals

> Learning Approach: Concept → Notes → Example → Coding Practice → Real-World Scenario → Interview Questions → Review




---

📋 Agenda

[ ] Python Overview

[ ] Python Interpreter

[ ] Python Execution Model

[ ] Python Versions

[ ] Python Installation

[ ] Python Environment

[ ] Interactive Interpreter

[ ] .py Files

[ ] Python Syntax

[ ] Indentation

[ ] Comments

[ ] Variables

[ ] Naming Conventions

[ ] Constants

[ ] Keywords

[ ] Identifiers

[ ] Literals

[ ] Dynamic Typing

[ ] Strong Typing

[ ] Built-in Data Types

[ ] Type Checking

[ ] Type Conversion

[ ] Input

[ ] Output

[ ] print()

[ ] input()



---

1. 🐍 Python Overview

Python is a high-level, general-purpose programming language.

Python is known for:

Simple and readable syntax

Easy learning curve

Large standard library

Huge third-party ecosystem

Cross-platform support

Automation capabilities

Data processing capabilities

Strong support for APIs and databases

Usage in DevOps, testing, ETL, Data Science and AI


Common Python Applications

Automation
Data Processing
ETL
API Development
Testing
DevOps
Data Analysis
Data Science
Machine Learning
Financial Applications

Python Characteristics

High-Level
General-Purpose
Dynamically Typed
Strongly Typed
Object-Oriented
Interpreted/Runtime-Based


---

2. 🔧 Python Interpreter

A Python interpreter/runtime is the software environment that executes Python programs.

Example:

print("Hello Python")

The Python implementation processes the program and produces:

Hello Python

CPython

CPython is the standard and most widely used Python implementation.


---

3. ⚙️ Python Execution Model

It is common to say:

> Python is an interpreted language.



However, this is an oversimplification.

With CPython, the basic execution flow is:

Python Source Code
        ↓
   Compilation
        ↓
     Bytecode
        ↓
Python Virtual Machine
        ↓
    Execution

For example:

print("Hello")

The .py source code is processed by CPython, compiled to bytecode, and that bytecode is executed by the Python runtime.

Important Interview Point

❌ Incorrect:

Python has no compiler.

✅ Better:

CPython compiles Python source code into bytecode,
and the Python Virtual Machine executes that bytecode.


---

4. 🐍 Python Versions

Python has had multiple versions.

Historically:

Python 2
Python 3

Python 2 is obsolete and unsupported.

Modern Python development uses:

Python 3.x

Examples of Python 3 releases include:

Python 3.8
Python 3.9
Python 3.10
Python 3.11
Python 3.12
Python 3.13
Python 3.14

The version used for a project depends on project requirements and compatibility.

Check Python Version

python --version

or:

python3 --version

Inside Python:

import sys

print(sys.version)


---

5. 💻 Python Installation

Python needs to be installed before we can execute Python programs locally.

After installation, verify it:

python --version

or:

python3 --version

Example

Python 3.x.x

The exact version depends on the installed Python release.


---

6. 🌍 Python Environment

A Python environment is the setup in which Python programs run.

It can contain:

Python Interpreter
Libraries
Packages
Project Dependencies
Environment Variables

Why environments are important

Different projects may require different versions of packages.

Example:

Project A
    ↓
pandas version A

Project B
    ↓
pandas version B

Installing everything globally can create dependency conflicts.

Virtual Environment

Python provides virtual environments to isolate project dependencies.

Example:

python -m venv myenv

Conceptually:

System Python
     │
     ├── Project A Environment
     │
     └── Project B Environment

> Virtual environments isolate project-specific dependencies.



We will study virtual environments in more detail later.


---

7. 💻 Interactive Interpreter

Python can be used interactively from a terminal.

Start Python:

python

You may see:

>>>

The >>> is the Python prompt.

Now we can execute code directly:

>>> 10 + 20
30

Another example:

>>> name = "Veera"
>>> print(name)
Veera

Uses

The interactive interpreter is useful for:

Learning Python

Testing small pieces of code

Experimenting

Quickly checking Python behavior


Interactive vs Script

Interactive:

>>> 10 + 20
30

Script:

program.py
    ↓
Python
    ↓
Output


---

8. 📄 .py Files

Python source files normally use the:

.py

extension.

Example:

hello.py

Contents:

print("Hello World")

Run it:

python hello.py

Remember

.py → Python source code file


---

9. 📝 Python Syntax

Syntax means the rules for writing valid Python code.

Example:

name = "Veera"
print(name)

This follows Python syntax.

Example of invalid syntax

if salary >= 100000
    print("Eligible")

The : is missing.

Correct:

if salary >= 100000:
    print("Eligible")

Remember

> Syntax = rules/grammar of the programming language.




---

10. 📐 Indentation

Indentation means spaces at the beginning of a line.

Python uses indentation to define blocks of code.

Example:

if salary >= 100000:
    print("Eligible")

The print() statement belongs to the if block because it is indented.

Multiple statements:

if salary >= 100000:
    print("Eligible")
    print("Process loan")

Recommended Practice

Use 4 spaces for indentation.

if condition:
    statement

Incorrect

if condition:
print("Hello")

Important

Python uses indentation instead of {} to define code blocks.


---

11. 💬 Comments

Comments are notes written for humans.

Python ignores comments during normal execution.

Single-Line Comment

Use #:

# Calculate monthly salary
salary = 140000

Inline comment:

salary = 140000  # Monthly salary

Good Comment

# Calculate remaining salary after fixed monthly expenses
remaining_salary = salary - expenses

Comments should explain useful information rather than obvious code.


---

12. 📦 Variables

A variable is a name that refers to an object/value.

Example:

name = "Veera"
age = 35
salary = 140000

Conceptually:

name   → "Veera"
age    → 35
salary → 140000

Python does not normally require explicit type declaration.

Example:

salary = 140000

Python determines the type from the object assigned to the name.


---

13. ✏️ Naming Conventions

Naming conventions make code easier to read and maintain.

Variables and Functions

Use snake_case:

monthly_salary = 140000
employee_name = "Veera"
loan_amount = 500000

Classes

Use PascalCase:

class EmployeeDetails:
    pass

Constants

Use UPPER_SNAKE_CASE:

MAX_RETRY_COUNT = 3
INTEREST_RATE = 8.5

Important

Naming conventions are conventions. Python does not automatically enforce them.


---

14. 🔒 Constants

A constant is a value intended not to change during program execution.

Python does not have a general const keyword for variables.

Instead, programmers use uppercase names by convention.

Example:

MAX_RETRY_COUNT = 3
INTEREST_RATE = 8.5

This communicates:

> "This value is intended to remain constant."



However, Python does not prevent reassignment:

MAX_RETRY_COUNT = 3

MAX_RETRY_COUNT = 5

Therefore:

> Python constants are mainly enforced by convention, not by a language-level const declaration.




---

15. 🔑 Keywords

Keywords are reserved words with special meaning in Python.

Examples:

if
else
elif
for
while
def
class
return
import
try
except
True
False
None
and
or
not
in
is

A keyword cannot normally be used as a variable name.

Invalid:

if = 10

View Python Keywords

import keyword

print(keyword.kwlist)


---

16. 🏷️ Identifiers

An identifier is a name used to identify something in Python.

Example:

salary = 140000

Here:

salary → identifier
140000 → literal

Identifiers can represent names of:

Variables

Functions

Classes

Modules

Other program elements


Valid Identifiers

salary
employee_name
loan_amount1
_private_value

Invalid Identifiers

1salary
employee-name

Keywords cannot be used as identifiers:

class = 10

is invalid.


---

17. 🔢 Literals

A literal is a value written directly in source code.

Examples:

100
10.5
3 + 4j
"Hello"
True
None

Example:

age = 35

Here:

age → identifier
35  → integer literal

Another:

name = "Veera"

Here:

name    → identifier
"Veera" → string literal

Common Literal Types

Integer Literal
Float Literal
Complex Literal
String Literal
Boolean Literal
None Literal


---

18. 🔄 Dynamic Typing

Python is a dynamically typed language.

We don't normally need to declare a variable's type explicitly.

Example:

x = 100

Python knows that the object 100 is an integer.

Later:

x = "Hello"

Now the name x refers to a string object.

Example:

x = 100
print(type(x))

x = "Hello"
print(type(x))

Output:

<class 'int'>
<class 'str'>

Important

Dynamic typing means:

Type information is associated with objects.

Type checking occurs during runtime.

A variable name can be rebound to an object of another type.


Easy Reminder

Dynamic Typing
       ↓
Types are determined/checked at runtime


---

19. 💪 Strong Typing

Python is also considered a strongly typed language.

Strong typing means Python generally does not automatically perform arbitrary conversions between incompatible types.

Example:

x = 10
y = "20"

print(x + y)

This produces:

TypeError

Python does not automatically convert "20" to 20 for this operation.

We need explicit conversion:

x = 10
y = "20"

print(x + int(y))

Output:

30

Dynamic vs Strong Typing

These are two different concepts.

Dynamic Typing
      ↓
How/when type information is determined and checked

Strong Typing
      ↓
How strictly incompatible types are handled

Python is:

Dynamic + Strongly Typed


---

20. 🧱 Built-in Data Types

Important built-in types in this chapter:

int
float
complex
bool
str
NoneType


---

21. 🔢 int

int represents whole numbers.

Examples:

age = 35
salary = 140000
quantity = -10

Check the type:

x = 100

print(type(x))

Output:

<class 'int'>

Python integers can represent arbitrarily large whole numbers, subject mainly to available memory.


---

22. 🔢 float

float represents floating-point numbers.

Examples:

interest_rate = 8.5
price = 125.75

Example:

x = 10.5

print(type(x))

Output:

<class 'float'>

Financial Note

Binary floating-point numbers can have precision limitations.

For financial calculations, Python also provides:

decimal.Decimal

We will study this later.


---

23. 🧮 complex

Python supports complex numbers.

A complex number contains:

Real Part + Imaginary Part

Example:

x = 3 + 4j

Here:

3 → Real part
4j → Imaginary part

Check:

print(type(x))

Output:

<class 'complex'>

Access the parts:

print(x.real)
print(x.imag)

Output:

3.0
4.0


---

24. ✅ bool

bool represents Boolean values.

There are two Boolean values:

True
False

Example:

loan_approved = True
is_active = False

Check:

print(type(loan_approved))

Output:

<class 'bool'>

Booleans are commonly used in conditions.

if loan_approved:
    print("Process Loan")


---

25. 🔤 str

str represents text.

Examples:

name = "Veera"
city = "Hyderabad"

Strings can use either single or double quotes:

"Hello"
'Hello'

Example:

message = "Welcome to Python"

print(type(message))

Output:

<class 'str'>

Strings are extremely important for:

Files

CSV

JSON

APIs

Database data

Logs

Murex data



---

26. 🚫 None

None represents the absence of a value.

Example:

result = None

Check its type:

print(type(result))

Output:

<class 'NoneType'>

Important

None is different from:

0
""
False

None represents the absence of a value.


---

27. 📊 Built-in Data Types — Quick Table

Type	Example	Purpose

int	100	Whole numbers
float	10.5	Floating-point numbers
complex	3 + 4j	Complex numbers
bool	True	Boolean values
str	"Python"	Text
NoneType	None	Absence of value



---

28. 🔍 Type Checking

Type checking means determining or checking the type of an object.

Python provides:

type()

and:

isinstance()


---

29. type()

type() returns the type of an object.

Example:

salary = 140000

print(type(salary))

Output:

<class 'int'>

More examples:

print(type(10))
print(type(10.5))
print(type("Hello"))
print(type(True))
print(type(None))


---

30. isinstance()

isinstance() checks whether an object is an instance of a specified type/class.

Example:

salary = 140000

print(isinstance(salary, int))

Output:

True

Another:

name = "Veera"

print(isinstance(name, str))

Output:

True

Wrong type:

salary = 140000

print(isinstance(salary, str))

Output:

False


---

31. type() vs isinstance()

type()

Tells us the object's exact type.

x = 10

print(type(x))

isinstance()

Checks whether the object is an instance of a specified type/class.

x = 10

print(isinstance(x, int))

Quick Difference

type()
  ↓
"What is the object's type?"

isinstance()
  ↓
"Is this object an instance of this type/class?"

In real Python code, isinstance() is often preferred for type checks because it also works naturally with class inheritance.


---

32. 🔄 Type Conversion

Type conversion means converting a value from one type to another.

Common functions:

int()
float()
str()
bool()


---

Integer → Float

x = 10

y = float(x)

print(y)

Output:

10.0


---

Integer → String

x = 100

y = str(x)

print(y)
print(type(y))

Output:

100
<class 'str'>


---

String → Integer

x = "100"

y = int(x)

print(y + 50)

Output:

150

The string must contain a valid integer representation.


---

String → Float

x = "10.5"

y = float(x)

print(y)

Output:

10.5


---

33. 📥 Input

Python uses:

input()

to receive input from the user.

Example:

name = input("Enter your name: ")

print(name)

If the user enters:

Veera

then:

name

contains:

"Veera"

⚠️ Very Important

input() always returns a string.

Example:

age = input("Enter age: ")

print(type(age))

Even if the user enters:

35

the type is:

str

Therefore, if we need an integer:

age = int(input("Enter age: "))


---

34. 📤 Output

Output means displaying information produced by a program.

Python commonly uses:

print()

Example:

print("Hello World")

Output:

Hello World


---

35. print()

print() displays values on the screen.

Example:

name = "Veera"
salary = 140000

print(name)
print(salary)

Multiple values:

print("Name:", name, "Salary:", salary)

Output:

Name: Veera Salary: 140000


---

36. print() with f-Strings

An f-string provides a convenient way to include variables inside text.

Example:

name = "Veera"
salary = 140000

print(f"Name: {name}")
print(f"Salary: {salary}")

Output:

Name: Veera
Salary: 140000

We will study strings and formatting in greater detail later.


---

37. 🔄 Input → Conversion → Output

Example:

name = input("Enter employee name: ")
salary = int(input("Enter monthly salary: "))

print(f"Employee: {name}")
print(f"Salary: {salary}")

Flow:

User
  ↓
input()
  ↓
String
  ↓
Type Conversion
  ↓
Required Data Type
  ↓
print()
  ↓
Output


---

38. 🏦 Real-World Example

Consider a simple salary calculation:

salary = 140000
emi = 53713
rent = 16500

remaining_salary = salary - emi - rent

print(f"Salary: {salary}")
print(f"EMI: {emi}")
print(f"Rent: {rent}")
print(f"Remaining Salary: {remaining_salary}")

Output:

Salary: 140000
EMI: 53713
Rent: 16500
Remaining Salary: 69787

This example combines:

Variables
Data Types
Arithmetic
Strings
Output

These same fundamentals will later be used in much larger automation and data-processing programs.


---

🧠 Chapter 01 Concept Map

PYTHON
                            │
        ┌───────────────────┼───────────────────┐
        ↓                   ↓                   ↓
      Syntax             Data Types          Execution
        │                   │                   │
   ┌────┼────┐        ┌─────┼──────┐           │
   ↓    ↓    ↓        ↓     ↓      ↓           ↓
Indent Comments   int/float str/bool None     Source
ation              complex                      ↓
                                              Bytecode
                                                 ↓
                                                PVM
                                                 ↓
                                             Execution


---

⚡ Quick Cheat Sheet

Python

High-Level
General-Purpose
Dynamic
Strongly Typed

Execution

.py Source
    ↓
CPython
    ↓
Bytecode
    ↓
Python Virtual Machine
    ↓
Execution

Basic Data Types

int      → 100
float    → 10.5
complex  → 3 + 4j
bool     → True / False
str      → "Hello"
None     → No value

Type Checking

type(x)

→ Returns the object's type.

isinstance(x, int)

→ Checks whether x is an instance of int.

Type Conversion

int()
float()
str()
bool()

Input

input()

⚠️ Always returns str.

Output

print()

→ Displays output.

Naming

variable_name  → snake_case
ClassName      → PascalCase
CONSTANT_NAME  → UPPER_SNAKE_CASE

Keywords

if
else
elif
for
while
def
class
return
import
True
False
None
and
or
not

Assignment vs Comparison

=   → Assignment
==  → Equality comparison

Dynamic vs Strong Typing

Dynamic Typing
→ Type checking/determination primarily at runtime

Strong Typing
→ Incompatible types are not freely mixed through
  arbitrary implicit conversions

Python:

Dynamic + Strongly Typed

Indentation

if condition:
    statement

Recommended:

4 spaces


---

🎤 Interview Questions

1. What is Python?

Python is a high-level, general-purpose programming language known for its readable syntax and large ecosystem.


---

2. Is Python compiled or interpreted?

A precise answer:

> CPython compiles Python source code into bytecode, and the Python Virtual Machine executes that bytecode. Python is commonly described as interpreted because execution occurs through its runtime.




---

3. What is dynamic typing?

Dynamic typing means Python does not require explicit type declarations for variables, and type checking occurs during runtime.


---

4. What is strong typing?

Strong typing means Python generally does not automatically perform arbitrary conversions between incompatible types.


---

5. What is an identifier?

An identifier is a name used to identify a variable, function, class or other program element.


---

6. What is a keyword?

A keyword is a reserved word with a predefined meaning in Python.


---

7. What is a literal?

A literal is a value written directly in source code.

Examples:

100
10.5
"Hello"
True
None


---

8. What does input() return?

input() always returns a string.


---

9. What is the difference between type() and isinstance()?

type()
→ Returns the object's type.

isinstance()
→ Checks whether the object is an instance of
  a specified type/class.


---

10. What is indentation in Python?

Indentation is whitespace at the beginning of a line used to define blocks of code.


---

11. What is None?

None is a special singleton object used to represent the absence of a value.

Its type is:

NoneType


---

12. Does Python have constants?

Python does not provide a general const keyword for ordinary variables. Constants are usually represented using uppercase naming conventions.

Example:

MAX_RETRY_COUNT = 3


---

🏦 Real-World Connection

The concepts in Chapter 01 are the foundation for our later Python learning:

Python Fundamentals
        ↓
Variables & Data Types
        ↓
Operators & Expressions
        ↓
Control Flow
        ↓
Functions
        ↓
Data Structures
        ↓
Exception Handling
        ↓
File Handling
        ↓
OOP
        ↓
Modules & Packages
        ↓
SQL / Databases
        ↓
Pandas
        ↓
ETL
        ↓
API Integration
        ↓
Automation
        ↓
Data Mart
        ↓
Production Support


---

✅ Chapter 01 Completion Checklist

[ ] Python overview

[ ] Python interpreter

[ ] Python execution model

[ ] Python versions

[ ] Python installation

[ ] Python environment

[ ] Interactive interpreter

[ ] .py files

[ ] Python syntax

[ ] Indentation

[ ] Comments

[ ] Variables

[ ] Naming conventions

[ ] Constants

[ ] Keywords

[ ] Identifiers

[ ] Literals

[ ] Dynamic typing

[ ] Strong typing

[ ] int

[ ] float

[  ↓
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

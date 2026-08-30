🐍 Python 50-Day Preparation

📅 Day 01 — Python Fundamentals Challenge

File: day1_challenge.py

🎯 Objective

Build a simple Employee Profile & Salary Information program to practice the core Python fundamentals covered in Chapter 01.


---

📚 Concepts to Practice

Variables

Naming conventions

int

float

str

bool

None

input()

print()

f-strings

type()

isinstance()

Type conversion

Comments

Constants

Basic Python syntax



---

🧩 Challenge Requirements

1. Get Employee Details

Ask the user to enter:

Employee Name
Employee ID
Monthly Salary
Experience in Years

Important: Remember that input() returns a str. Convert numeric inputs to the appropriate data types.


---

2. Create Employee Variables

Use these variable names:

employee_name
employee_id
monthly_salary
experience_years
is_active
department

Requirements:

Variable	Expected Type

employee_name	str
employee_id	int
monthly_salary	int or float
experience_years	int
is_active	bool
department	None


Set:

is_active = True
department = None


---

3. Display Employee Details

Display the information in a clean format.

Expected style:

================================
       EMPLOYEE DETAILS
================================

Employee Name     : Veera
Employee ID       : 1001
Monthly Salary    : 140000
Experience        : 8 years
Active Employee   : True
Department        : None

Your values can obviously be different.


---

4. Type Checking — type()

Use type() to display the type of each important variable.

Example:

================================
         TYPE CHECKING
================================

Employee Name Type  : <class 'str'>
Employee ID Type    : <class 'int'>
Salary Type         : <class 'int'>
Experience Type     : <class 'int'>
Active Type         : <class 'bool'>
Department Type     : <class 'NoneType'>


---

5. Type Validation — isinstance()

Use isinstance() to validate the variables.

Check:

employee_name      → str
employee_id        → int
monthly_salary     → int or float
experience_years   → int
is_active          → bool

Expected style:

================================
       TYPE VALIDATION
================================

Employee Name is string : True
Employee ID is integer  : True
Salary is numeric       : True
Experience is integer   : True
Active is boolean       : True


---

6. Type Conversion

Create:

salary_text = "140000"

Convert it into an integer:

salary_text → salary_number

Display both types.

Expected:

================================
       TYPE CONVERSION
================================

Salary Text Type   : <class 'str'>
Salary Number Type : <class 'int'>


---

7. Create a Constant

Create one constant using Python's naming convention.

Example:

MAX_WORKING_HOURS = 40

Choose a reasonable value yourself.


---

8. Add Comments

Organize your program using comments such as:

# Get employee details

# Store employee information

# Display employee information

# Validate data types

# Demonstrate type conversion


---

⭐ Bonus Challenge

Use:

salary = 140000
rent = 16500
emi = 53713

Calculate:

remaining_salary

Expected result:

Remaining Salary : 69787


---

🚫 Restrictions

For Day 01, do NOT use concepts that haven't been covered yet:

❌ if / else
❌ for
❌ while
❌ functions
❌ lists
❌ tuples
❌ sets
❌ dictionaries
❌ classes

✅ Allowed

✓ Variables
✓ input()
✓ print()
✓ type()
✓ isinstance()
✓ int()
✓ float()
✓ str()
✓ bool()
✓ f-strings
✓ Comments
✓ Basic arithmetic


---

🎯 Expected Learning Outcome

After completing this challenge, you should be able to explain:

1. What is a variable?
2. What is an identifier?
3. What is a literal?
4. What is dynamic typing?
5. What is strong typing?
6. What does input() return?
7. Why do we use type conversion?
8. Difference between type() and isinstance()
9. What is None?
10. What are Python's basic built-in data types?
11. What is a constant in Python?
12. Why is indentation important?


---

🏆 Day 01 Completion Criteria

[ ] Program runs without errors
[ ] Employee details are accepted from user
[ ] Correct data types are used
[ ] Employee details are displayed
[ ] type() is demonstrated
[ ] isinstance() is demonstrated
[ ] Type conversion is demonstrated
[ ] Constant is created
[ ] Comments are added
[ ] Bonus salary calculation completed
[ ] Code follows naming conventions


---

📁 Git Structure

python-50-days/
│
├── 01-python-fundamentals/
│   ├── notes.md
│   └── day1_challenge.py
│
└── README.md

Suggested Git Commit

git add 01-python-fundamentals/
git commit -m "Day 01: Python fundamentals challenge"
git push

Important: Don't look for a solution yet. Write day1_challenge.py completely on your own. When you paste your code here, I'll review your solution first, point out mistakes, and explain why each correction is needed.

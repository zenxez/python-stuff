# Lesson 2: Conditional Statements and Operations

## Table of Contents
1. [Introduction to Conditional Statements](#introduction-to-conditional-statements)
2. [If Statement](#if-statement)
3. [Elif Statement](#elif-statement)
4. [Else Statement](#else-statement)
5. [Comparison Operations](#comparison-operations)
6. [Logical Operations](#logical-operations)
7. [Nested If Statements](#nested-if-statements)

---

## Introduction to Conditional Statements

Conditional statements allow your program to make decisions based on certain conditions. They control the flow of execution in your code, enabling you to create programs that can respond differently to different situations.

In Python, conditional statements are built around the concept of **boolean values** (True or False) and **expressions** that evaluate to these boolean values.

---

## If Statement

The `if` statement is the most basic conditional statement. It executes a block of code only if a condition is True.

### Syntax:
```python
if condition:
    # code to execute if condition is True
    statement1
    statement2
    # ... more statements
```

### Example:
```python
age = 18

if age >= 18:
    print("You are eligible to vote!")
    print("Welcome to democracy!")
```

### Key Points:
- The condition must be followed by a colon `:`
- The code block must be indented (usually 4 spaces)
- Only the indented code will execute if the condition is True

---

## Elif Statement

The `elif` (else if) statement allows you to check multiple conditions in sequence. It's used when you have multiple possible conditions to test.

### Syntax:
```python
if condition1:
    # code for condition1
elif condition2:
    # code for condition2
elif condition3:
    # code for condition3
# ... more elif statements
```

### Example:
```python
score = 85

if score >= 90:
    grade = "A"
    print("Excellent!")
elif score >= 80:
    grade = "B"
    print("Good job!")
elif score >= 70:
    grade = "C"
    print("Not bad!")
elif score >= 60:
    grade = "D"
    print("You passed!")
else:
    grade = "F"
    print("You need to study more!")
```

### Key Points:
- `elif` is checked only if the previous `if` or `elif` conditions were False
- You can have multiple `elif` statements
- `elif` must come after an `if` statement

---

## Else Statement

The `else` statement provides a fallback option when all previous conditions are False.

### Syntax:
```python
if condition:
    # code if condition is True
else:
    # code if condition is False
```

### Example:
```python
temperature = 25

if temperature > 30:
    print("It's hot outside!")
    print("Wear light clothing.")
else:
    print("The weather is pleasant.")
    print("Enjoy your day!")
```

### Key Points:
- `else` is optional but provides a default action
- `else` must come at the end of an if-elif chain
- Only one `else` statement is allowed per if-elif chain

---

## Comparison Operations

Comparison operations are used to compare values and return boolean results (True or False).

### Comparison Operators:

| Operator | Description | Example | Result |
|----------|-------------|---------|---------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `10 > 5` | `True` |
| `<` | Less than | `3 < 7` | `True` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `4 <= 6` | `True` |

### Examples:
```python
# Numeric comparisons
x = 10
y = 5

print(x == y)    # False
print(x != y)    # True
print(x > y)     # True
print(x < y)     # False
print(x >= y)    # True
print(x <= y)    # False

# String comparisons
name1 = "Alice"
name2 = "Bob"

print(name1 == name2)  # False
print(name1 != name2)  # True
print(name1 > name2)   # False (lexicographic order)
```

### String Comparison:
Strings are compared lexicographically (alphabetically):
```python
print("apple" < "banana")  # True
print("cat" > "dog")       # False
print("A" < "a")           # True (uppercase comes before lowercase)
```

---

## Logical Operations

Logical operations combine multiple boolean expressions using logical operators.

### Logical Operators:

| Operator | Description | Example | Result |
|----------|-------------|---------|---------|
| `and` | Both conditions must be True | `True and True` | `True` |
| `or` | At least one condition must be True | `True or False` | `True` |
| `not` | Reverses the boolean value | `not True` | `False` |

### Truth Tables:

#### AND Operator:
| A | B | A and B |
|---|---|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

#### OR Operator:
| A | B | A or B |
|---|---|---------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

#### NOT Operator:
| A | not A |
|---|-------|
| True | False |
| False | True |

### Operator Precedence:
1. `not` (highest)
2. `and`
3. `or` (lowest)

---
## Nested If Statements

Nested if statements are if statements inside other if statements. They allow for more complex decision-making logic.

### Syntax:
```python
if condition1:
    if condition2:
        # code if both conditions are True
        statement1
    else:
        # code if condition1 is True but condition2 is False
        statement2
else:
    if condition3:
        # code if condition1 is False but condition3 is True
        statement3
    else:
        # code if both condition1 and condition3 are False
        statement4
```

## Summary

Conditional statements are fundamental to programming and allow you to:

- **Make decisions** based on data
- **Control program flow** with different execution paths
- **Handle various scenarios** in your applications
- **Create interactive programs** that respond to user input

Key concepts to remember:
- Use `if` for single conditions
- Use `elif` for multiple alternative conditions
- Use `else` for default actions
- Master comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- Understand logical operators (`and`, `or`, `not`)
- Use nested if statements carefully and consider alternatives
- Follow best practices for readable and maintainable code

With these tools, you can create programs that make intelligent decisions and respond appropriately to different situations!

## ---Tasks---

### Task 1
Ask for age and print:

- If less than 18 → "Underage"
- If 18 or more → "Adult"

### Task 2
Ask for a number and print whether it's even or odd.

### Task 3
Ask for temperature and print:

- More than 30 → "Hot"
- 20–30 → "Warm"
- 10–20 → "Cool"
- Otherwise → "Cold"

### Task 4
Ask for a password (input()) and compare it to "Python123".
- If correct, print "Access granted"
- If not → "Wrong password"

### Task 5
Ask for two numbers and print which one is larger.

### Task 6
Ask for age and print:

- <13 → "child"
- 13–17 → "teenager"
- 18–64 → "adult"
- ≥65 → "senior"

### Task 7
Ask for a number and check if it's positive, negative, or zero and print.

### Task 8
Ask the user two questions:

- has_ticket (Yes/No)
- is_vip (Yes/No)

- If either is Yes → "You can enter."
- If both are No → "You cannot enter."

👉 Use the `or` operator.

### Task 9
Ask the user for age and student status (True/False).
- If over 18 and is a student → "Discount 50%"
- If only a student → "Discount 25%"
- Otherwise → "No discount"



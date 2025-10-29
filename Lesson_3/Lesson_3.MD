# Lesson 3: Loops

## 1. What Is Loop?

A loop is used when we want the same action to be repeated multiple times — for example, printing text 10 times or listing all the elements in a list.

## 2. For Loop

A for loop iterates over elements (for example, in a list, string, or range).

```python
for i in range(5):
    print("Hello")
```
Output:
Hello
Hello
Hello
Hello
Hello

🟢 Explanation:

range(5) means: numbers from 0 to 4 (5 not included)

The variable i takes each value

---
## 3. range(start, stop, step) Function
```python
range(start, stop, step)
```
### examples:
```python
for i in range(1, 6):
    print(i)
```
Output:
1,2,3,4,5

```python
for i in range(2, 11, 2):
    print(i)
```
Output: 2,4,6,8,10

## 4. String Iteration
```python
for letter in "Python":
    print(letter)
```
Each letter will be printed separately.
Output: P,y,t,h,o,n

## 5. While Loop
The while loop runs as long as the condition is true.
```python
count = 1
while count <= 5:
    print("Count is:", count)
    count = count + 1

```
Output:
1. Count is: 1
2. Count is: 2
3. Count is: 3
4. Count is: 4
5. Count is: 5

## 6. break And continue
break – stop the loop
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```
Output:
- 0
- 1
- 2
- 3
- 4

continue – skips a specific iteration
```python
for i in range(5):
    if i == 2:
        continue
    print(i)

```
Output:
- 0
- 1
- 3
- 4

## 7. Nested loops
```python
for i in range(3):
    for j in range(2):
        print(i, j)

```
Output:
- 0 0
- 0 1
- 1 0
- 1 1
- 2 0
- 2 1

## 8. else With Loops
A for or while loop can have an else, which is executed if the loop reaches the end without a break.
```python
for i in range(3):
    print(i)
else:
    print("Loop finished!")

```
Output:
- 0
- 1
- 2
- Loop finished!

## Tasks 
### Task 1 — Repetition

Print "Python is fun!" exactly 5 times using a for loop.

### Task 2 — A series of numbers

Print the numbers 1 to 10 using a for loop.

### Task 3 — Recursion.

Print the numbers from 10 to 1 in reverse using a for loop

### Task 4 — Even Numbers

Print only the even numbers from 2 to 20.

### Task 5 — Sum of numbers

print the sum of numbers from 1 to 10.

### Task 6 — Text Letters

Prompt the user for a word (input()),
and print each letter on a separate line.

### Task 7 — Password Verification

Prompt the user for a password until they enter "12345678".
When they enter it correctly, print "Access granted!".

### Task 8 — Star Shape

Write a program that prints:
```markdown
*
**
***
****
*****
```

### Task 9 — Sum of Digits

Ask the user for an number and calculate the sum of its digits.

Example:
```markdown
Enter number: 1234
Sum of digits: 10
```

### Task 10 — Reverse a Number

Ask the user for a number and print it in reverse.

Example:
```markdown
Enter number: 12345
Reversed: 54321
```



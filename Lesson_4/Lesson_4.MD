# Lists

## What is list?
A list is a collection of elements that we can modify, add, or delete.

## Indexes and access
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple
print(fruits[-1]) # cherry
```

## Change elements
```python
fruits[1] = "orange"
print(fruits)  # ['apple', 'orange', 'cherry']
```

### Add elements
| მეთოდი              | გამოყენება                  | შედეგი                                  |
| ------------------- | --------------------------- | --------------------------------------- |
| `.append(x)`        | ბოლოში ამატებს              | `["apple", "banana", "cherry", "kiwi"]` |
| `.insert(index, x)` | ამატებს კონკრეტულ პოზიციაზე | `["apple", "kiwi", "banana", "cherry"]` |
| `+`                 | აერთიანებს სიებს            | `[1, 2] + [3, 4] → [1, 2, 3, 4]`        |

## Delte elements
| მეთოდი        | მაგალითი                  | აღწერა                      |
| ------------- | ------------------------- | --------------------------- |
| `.remove(x)`  | `fruits.remove("banana")` | შლის კონკრეტულ მნიშვნელობას |
| `.pop(index)` | `fruits.pop(1)`           | შლის ელემენტს ინდექსით      |
| `del`         | `del fruits[0]`           | შლის ელემენტს               |
| `.clear()`    | `fruits.clear()`          | აცილებს მთელ სიას           |

## Iteration on a list (for loop)
```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

## List length
```python
numbers = [10, 20, 30]
print(len(numbers))  # 3
```

## Multiplying and merging on a list
```python
a = [1, 2]
b = [3, 4]
print(a + b)   # [1, 2, 3, 4]
print(a * 3)   # [1, 2, 1, 2, 1, 2]
```

## Useful methods
| მეთოდი          | აღწერა                    | მაგალითი            | შედეგი       |
| --------------- | ------------------------- | ------------------- | ------------ |
| `.append(x)`    | ელემენტის დამატება ბოლოში | `lst.append(5)`     | `[1, 2, 5]`  |
| `.insert(i, x)` | ელემენტის ჩასმა           | `lst.insert(1, 10)` | `[1, 10, 2]` |
| `.remove(x)`    | შლის მნიშვნელობას         | `lst.remove(10)`    | `[1, 2]`     |
| `.pop()`        | შლის ბოლო ელემენტს        | `lst.pop()`         | `[1]`        |
| `.index(x)`     | აბრუნებს პოზიციას         | `lst.index(2)`      | `1`          |
| `.count(x)`     | ითვლის რაოდენობას         | `[1,2,2].count(2)`  | `2`          |

## Tasks
### Task 1

Create a list of "apple", "banana", "cherry" and print the second element.

### Task 2

Replace "banana" with "orange" and print the result.

### Task 3

Add "kiwi" and "mango" to the bottom of the list.

### Task 4

Remove "apple" from the list using the method.

### Task 5

Check if "cherry" is in the list.
If yes, print "Yes", if not, print "No".

### Task 6

Print each element on a separate line using a for loop.

### Task 7

Create a list "a", "b", "c" and print it in reverse -> "cba"

### Task 8

Create a list of 5 numbers (for example [3, 12, 7, 5, 10])
and find the largest number using a loop

### Task 9

Ask the user how many numbers they want to enter.
Then store each number entered in a list and print a new list with all values ​​doubled.

example:
```markdawn
How many numbers? 3
Enter number: 5
Enter number: 2
Enter number: 7
New list: [10, 4, 14]
```

### Task 10

You have two lists (for example, names),
and prints only those elements that are in both.

example:
```markdawn
List1 = ["Ana", "Luka", "Nika"]
List2 = ["Nika", "Saba", "Luka"]
Common: ["Luka", "Nika"]
```
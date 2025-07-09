# javascript-warm_up

This project introduces the fundamentals of scripting with JavaScript using Node.js.
It covers basic syntax, data types, loops, functions, and command-line argument parsing.

## 🧠 Learning Objectives

- How to run a JavaScript script using Node.js
- Understanding variables, constants, and scopes
- Using `if`, `else`, loops (`for`, `while`)
- String and number manipulation
- Working with arrays and objects
- How to use functions, both regular and recursive
- Understanding modules and how to export/import functions
- Handling command-line arguments with `process.argv`

## 📄 Project Structure

Each task is implemented in a separate file, named according to the task number (e.g. `0-javascript_is_amazing.js`).

## ✅ Tasks Breakdown

### 0. First constant, first print
Prints a string using `const` and `console.log`.

### 1. 3 languages
Prints 3 lines using only one `console.log` with line breaks.

### 2. Arguments
Checks if any arguments are passed to the script and prints the appropriate message.

### 3. Value of my argument
Prints the first argument passed, or "No argument" if none is passed.

### 4. Create a sentence
Prints two arguments in the format: “<arg1> is <arg2>”.

### 5. An Integer
Prints “My number: <converted integer>” if the first argument can be converted to an integer; otherwise prints “Not a number”.

### 6. Loop to languages
Prints an array of strings using a loop.

### 7. I love C
Prints “C is fun” x times, where x is the first argument (must be an integer).

### 8. Square
Prints a square made of `X` characters of the given size (from argument).

### 9. Add
Prints the result of adding two integers passed as arguments.

### 10. Factorial
Computes and prints the factorial of an integer passed as argument. Uses recursion.

### 11. Second biggest!
Finds and prints the second biggest number from the list of arguments.

### 12. Object
Modifies the value of a key in an object and prints the object before and after.

### 13. Add file
Defines a function `add(a, b)` that is visible from outside the file using `module.exports`.

## 🛠 Usage

To run a script, use:
```bash
./<filename>.js <arguments>
# Or with Node.js
node <filename>.js <arguments>
```

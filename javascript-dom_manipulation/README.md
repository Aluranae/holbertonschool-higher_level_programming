# JavaScript - DOM Manipulation

## 📚 Project Overview

This project is part of the Holberton School curriculum and focuses on practicing **DOM (Document Object Model) manipulation using JavaScript**. The goal is to dynamically update, create, and remove HTML elements, modify style or content, and fetch remote data using the Fetch API — all without reloading the page.

You’ll also learn how to make sure your JavaScript behaves correctly even when loaded from the `<head>` section before the DOM is fully rendered.

---

## 🎯 Learning Objectives

- What is the DOM and how to access HTML elements from JavaScript
- How to update the content or style of an HTML element
- How to create, append, and remove HTML elements dynamically
- How to add and remove CSS classes via JavaScript
- How to respond to user events (clicks, page load)
- How to fetch data from an external API using `fetch()`
- How to handle JSON responses
- How to make your code wait until the DOM is fully loaded

---

## 📂 Task Breakdown

### ✅ 0. Color Me
Update the `<header>` text color to red using `document.querySelector`.  
✔ Immediate effect when the page loads.

---

### ✅ 1. Click and turn red
On clicking the element with `id="red_header"`, update the `<header>` color to red.  
✔ You must attach a click event listener.

---

### ✅ 2. Add `.red` class
On click, **add the class** `red` to the `<header>` element instead of changing its color directly.

---

### ✅ 3. Toggle classes
When clicking the element with `id="toggle_header"`, toggle the class between `red` and `green`.  
✔ Only one class must be present at a time.

---

### ✅ 4. List of elements
When clicking `id="add_item"`, append a new `<li>Item</li>` into the list `.my_list`.

---

### ✅ 5. Change the text
When clicking `id="update_header"`, replace the `<header>` text content with `"New Header!!!"`.

---

### ✅ 6. Star wars character
Fetch and display the name of character ID 5 from SWAPI:  
`https://swapi-api.hbtn.io/api/people/5/?format=json`  
✔ Display the result in the element `id="character"`.

---

### ✅ 7. Star Wars movies
Fetch and display the **titles of all Star Wars movies** from:  
`https://swapi-api.hbtn.io/api/films/?format=json`  
✔ Each title must appear in a `<li>` inside `id="list_movies"`.

---

### ✅ 8. Say Hello!
Fetch `"hello"` in French from:  
`https://hellosalut.stefanbohacek.dev/?lang=fr`  
✔ Display it in `id="hello"`  
✔ Script must work even when placed in `<head>` (use `DOMContentLoaded`)

---

## ✅ Requirements

- JavaScript must be **semistandard** compliant
- No `var` allowed — use `const` or `let`
- No page reload allowed
- All code must be dynamic (DOM manipulation only)
- Scripts must handle being loaded from `<head>`

---

## 🛠 Usage

Each script (0-script.js to 8-script.js) corresponds to a specific task.  
You can test each one using the provided `X-main.html` files in a browser.

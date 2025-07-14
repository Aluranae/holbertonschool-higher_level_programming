/*
  Script that adds a new <li> element with the text "Item" to a <ul> with class "my_list" when clicking on the element with id "add_item"
*/

const addItem = document.querySelector('#add_item');
const ul = document.querySelector('.my_list');
addItem.addEventListener('click', () => {
  const li = document.createElement('li');
  li.textContent = 'Item';
  ul.appendChild(li);
});

/*
  Script that toggles the header class between "red" and "green" when clicking on the element with id "toggle_header"
*/

const bouton = document.querySelector('header');
const elemTogHead = document.querySelector('#toggle_header');
elemTogHead.addEventListener('click', () => {
  if (bouton.classList.contains('red')) {
    bouton.classList.remove('red');
    bouton.classList.add('green');
  } else {
    bouton.classList.remove('green');
    bouton.classList.add('red');
  }
});

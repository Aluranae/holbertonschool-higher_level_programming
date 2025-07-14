/*
  Script that updates the <header> text to "New Header!!!" when clicking on the element with id "update_header"
*/

const elemHeader = document.querySelector('header');
const upHead = document.querySelector('#update_header');
upHead.addEventListener('click', () => {
  elemHeader.textContent = 'New Header!!!';
});

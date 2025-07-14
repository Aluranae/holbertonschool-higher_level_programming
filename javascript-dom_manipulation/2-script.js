/*
  Script that adds the class "red" to the header element when clicking on the element with id "red_header"
*/

const elemHeader = document.querySelector('header');
const elemRedHead = document.querySelector('#red_header');
elemRedHead.addEventListener('click', () => {
  elemHeader.classList.add('red');
});

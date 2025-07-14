/*
  Script that changes the header text color to red when clicking on the element with id 'red_header'
*/

const elemHeader = document.querySelector('header');
const elemRedHead = document.querySelector('#red_header');
elemRedHead.addEventListener('click', () => {
  elemHeader.style.color = '#FF0000';
});

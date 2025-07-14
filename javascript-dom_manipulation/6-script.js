/*
  Script that fetches data from the Star Wars API and displays the name of character ID 5
  The name must be placed inside the element with id "character"
*/

const char = document.getElementById('character');
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(res => res.json())
  .then(data => {
    char.textContent = `name : ${data.name}`;
  });

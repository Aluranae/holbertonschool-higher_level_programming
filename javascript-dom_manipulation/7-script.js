/*
  Script that fetches Star Wars movies and lists each title in the <ul> element with id "list_movies"
*/

const ul = document.querySelector('#list_movies');
const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';
fetch(apiUrl)
  .then(res => res.json())
  .then(data => {
    data.results.forEach(movie => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      ul.appendChild(li);
    });
  });

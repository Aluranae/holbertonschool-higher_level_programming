/*
  Script that fetches the translation of "Hello" from a remote API and displays it inside the <div> with id "hello"
  The script must work even when loaded from the <head> tag
*/

document.addEventListener('DOMContentLoaded', () => {
  const helloDiv = document.getElementById('hello');
  const apiUrl = ('https://hellosalut.stefanbohacek.dev/?lang=fr');
  fetch(apiUrl)
    .then(res => res.json())
    .then(data => {
      helloDiv.textContent = `hello : ${data.hello}`;
    });
});

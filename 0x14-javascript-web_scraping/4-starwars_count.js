#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API_URL>');
  process.exit(1);
}

request(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  const filmsObj = JSON.parse(body).results;

  if (!Array.isArray(filmsObj)) {
    console.error('Unexpected response format from the API');
    process.exit(1);
  }

  const machArr = filmsObj.filter(film =>
    film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
  );
  console.log(machArr.length);
});

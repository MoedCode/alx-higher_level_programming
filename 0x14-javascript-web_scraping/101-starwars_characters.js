#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./101-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    process.exit(1);
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, function (charError, charResponse, charBody) {
      if (charError) {
        console.error(charError);
        process.exit(1);
      }

      if (charResponse.statusCode !== 200) {
        console.error(`Error: ${charResponse.statusCode}`);
        process.exit(1);
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});

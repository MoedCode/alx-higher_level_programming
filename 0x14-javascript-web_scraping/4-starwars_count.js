#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = '/people/18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    let totalMovies = 0;

    films.forEach((movie) => {
      const hasCharacter = movie.characters.some(apiUrl => apiUrl.includes(characterId));
      if (hasCharacter) totalMovies += 1;
    });

    console.log(totalMovies);
  }
});

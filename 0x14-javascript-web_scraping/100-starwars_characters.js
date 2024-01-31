#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./100-starwars_characters.js <movie_id>');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Function to fetch characters from the Star Wars API
function getCharacters (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

// Function to print character names
async function printCharacterNames () {
  try {
    const movieData = await getCharacters(apiUrl);
    const characters = movieData.characters;

    for (const characterUrl of characters) {
      const characterData = await getCharacters(characterUrl);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

printCharacterNames();

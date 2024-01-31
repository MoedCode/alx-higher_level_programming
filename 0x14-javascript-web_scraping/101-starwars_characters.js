#!/usr/bin/node
const request = require('request-promise-native'); // Use 'request-promise-native' for Promise-based requests

async function getMovieData (movieId) {
  const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;
  try {
    const response = await request(url);
    return JSON.parse(response);
  } catch (error) {
    console.error(`Error fetching movie data: ${error.message}`);
    process.exit(1);
  }
}

async function printCharacters (characterUrls) {
  for (const characterUrl of characterUrls) {
    try {
      const response = await request(characterUrl);
      const characterData = JSON.parse(response);
      console.log(characterData.name);
    } catch (error) {
      console.error(`Error fetching character data: ${error.message}`);
      process.exit(1);
    }
  }
}

async function main () {
  const movieId = process.argv[2];

  if (!movieId) {
    console.error('Usage: ./101-starwars_characters.js <Movie ID>');
    process.exit(1);
  }

  const movieData = await getMovieData(movieId);
  const characters = movieData.characters;
  await printCharacters(characters);
}

main();

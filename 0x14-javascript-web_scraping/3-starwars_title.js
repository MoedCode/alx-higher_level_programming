#!/usr/bin/node

const request = require('request');

const moviId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${moviId}`;

request(apiUrl, (err, res, body) => {
  if (err) {
    console.err('Error', err);
    return;
  }
  const filmObj = JSON.parse(body);
  filmObj.title && console.log(filmObj.title);
  !filmObj.title && console.log('Movie not found!');
});

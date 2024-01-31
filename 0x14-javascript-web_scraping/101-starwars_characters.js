#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(apiUrl, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    putchar(characters, 0);
  }
});

function putchar (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        putchar(characters, index + 1);
      }
    }
  });
}

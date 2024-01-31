#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('<=>\n',error);
    return;
  }

  const tasks = JSON.parse(body);

  // Your logic to count completed tasks for each user goes here

  // Output the result as specified
  console.log(tasks);
});

#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const apiUrl = process.argv[2];
const filePath = process.argv[3];

if (!filePath && !apiUrl) {
  console.error('Usage: ./0-readme.js <file-path>');
  process.exit(1);
}
request(apiUrl, (err, res, body) => {
  if (err) {
    console.err('Error', err);
    return;
  }
  fs.writeFile(filePath, body, (err) => {
    err && console.log(err);
  });
});

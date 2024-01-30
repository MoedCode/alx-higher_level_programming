#!/usr/bin/node

const request = require('request');
const { writeFile } = require('fs');

const reqUrl = process.argv[2];
const filePath = process.argv[3];

if (!filePath && !reqUrl) {
  console.error('Usage: ./0-readme.js <file-path>');
  process.exit(1);
}

request(reqUrl, (err, res, body) => {
  err && console.log(err.body);
  err && process.exit(1);
  writeFile(filePath, body, 'utf-8', (err) => {
    err && console.log(err);
  });
});

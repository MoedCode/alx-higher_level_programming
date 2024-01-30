#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const str = process.argv[3];

if (!filePath && !str) {
  console.error('Usage: ./0-readme.js <file-path>');
  process.exit(1);
}

fs.writeFile(filePath, str, (err) => {
  err && console.log(err);
});

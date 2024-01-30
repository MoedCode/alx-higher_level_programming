#!/usr/bin/node
const { readFile } = require('node:fs');

const filePath = process.argv[2];
readFile(filePath, 'utf-8', (err, res) => {
  err && console.error(err);
  res && console.log(res);
});

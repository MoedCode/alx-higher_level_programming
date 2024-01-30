#!/usr/bin/node

const request = require('request');

const reqUrl = process.argv[2];

request(reqUrl, (err, res, body) => {
  err && console.log(err);
  err && process.exit(1);
  console.log(`code: ${res.statusCode}`);
});

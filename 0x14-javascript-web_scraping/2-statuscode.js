#!/usr/bin/node

const REQ  = require('request');

req_url = process.argv[2];

REQ (req_url, (err,res, body)=>{
    err && console.log(err);
    err && process.exit(1);
    console.log(`code: ${res.statusCode}`);
});
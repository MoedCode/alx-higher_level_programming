#!/usr/bin/node

const { argv } = require('node:process');

const len = argv.length;
if (len < 3)
{
    console.log('No argument');
}
else if (len === 3)
{
     console.log('Argument found');
 }
else
{
     console.log('Argument found');
 }

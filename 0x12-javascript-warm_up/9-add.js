#!/usr/bin/node
const args = process.argv;

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
    return;
  }
  console.log(parseInt(a) + parseInt(b));
}
add(args[2], args[3]);

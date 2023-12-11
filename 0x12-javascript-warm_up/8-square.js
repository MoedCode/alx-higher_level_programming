#!/usr/bin/node
const args = process.argv;

if (isNaN(args[2])) {
  console.log('Missing size');
} else {
  let str = '';
  for (let i = 0; i < parseInt(args[2]); i++) {
    str += 'x';
  }

  for (let i = 0; i < parseInt(args[2]); i++) {
    console.log(str);
  }
}

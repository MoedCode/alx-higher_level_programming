#!/usr/bin/node
const args = process.argv;

if (isNaN(args[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(args[2]); i++) {
    for (let i = 0; i < parseInt(args[2]); i++) {
      process.stdout.write('x');
    }
    console.log();
  }
}

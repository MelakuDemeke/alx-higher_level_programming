#!/usr/bin/node

const arg = process.argv[2];
const parsedInt = parseInt(arg);

if (!isNaN(parsedInt)) {
  for (let i = 0; i < parsedInt; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}

#!/usr/bin/node

const arg = process.argv[2];
const parsedInt = parseInt(arg);

if (!isNaN(parsedInt)) {
  for (let i = 0; i < parsedInt; i++) {
    let row = '';
    for (let j = 0; j < parsedInt; j++) {
      row += 'X'
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}

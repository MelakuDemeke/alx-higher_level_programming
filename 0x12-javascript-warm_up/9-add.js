#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const firstNum = (Number(process.argv[2]));
const secondNum = (Number(process.argv[3]));

console.log(add(firstNum, secondNum));

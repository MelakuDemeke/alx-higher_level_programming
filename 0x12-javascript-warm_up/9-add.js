#!/usr/bin/node

const firstNum = Math.floor(Number(process.argv[2]));
const secondNum = Math.floor(Number(process.argv[3]));

if (isNaN(firstNum) || isNaN(secondNum)) {
  console.log('NaN');
} else {
  console.log(add(firstNum, secondNum));
}

function add(a, b){
  return a + b;
}
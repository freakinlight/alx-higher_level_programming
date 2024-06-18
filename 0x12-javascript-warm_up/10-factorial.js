#!/usr/bin/node

function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

const number = parseInt(process.argv[2]);

if (isNaN(number)) {
  console.log(1);
} else {
  const result = factorial(number);
  if (result === Infinity) {
    console.log(Infinity);
  } else {
    console.log(result);
  }
}

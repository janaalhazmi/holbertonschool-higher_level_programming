#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2).map(Number);

  numbers.sort(function (a, b) {
    return b - a;
  });

  console.log(numbers[1]);
}

#!/usr/bin/node

const arg = process.argv[2];
const convArg = Number(arg);
if ((isNaN(convArg)) || convArg < 0) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < convArg; i++) {
    console.log('C is fun');
  }
}

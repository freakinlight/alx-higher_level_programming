#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);

if (args.length !== 3) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const fileA = args[0];
const fileB = args[1];
const fileC = args[2];

let contentA, contentB;

try {
  contentA = fs.readFileSync(fileA, 'utf8');
} catch (err) {
  console.error(`Error reading ${fileA}:`, err.message);
  process.exit(1);
}

try {
  contentB = fs.readFileSync(fileB, 'utf8');
} catch (err) {
  console.error(`Error reading ${fileB}:`, err.message);
  process.exit(1);
}

try {
  fs.writeFileSync(fileC, contentA.trim() + '\n' + contentB.trim() + '\n');
  console.log(`Concatenated ${fileA} and ${fileB} into ${fileC}`);
} catch (err) {
  console.error(`Error writing to ${fileC}:`, err.message);
  process.exit(1);
}

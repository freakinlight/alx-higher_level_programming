#!/usr/bin/env node

// Retrieve the arguments passed to the script
const args = process.argv.slice(2);

// Access the first and second arguments
const firstArg = args[0];
const secondArg = args[1];

// Print the arguments in the specified format
console.log(`${firstArg} is ${secondArg}`);

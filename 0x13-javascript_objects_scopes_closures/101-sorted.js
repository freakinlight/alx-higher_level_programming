#!/usr/bin/node

const dict = require('./101-data').dict;

const sortedDict = {};

Object.keys(dict).forEach(userId => {
  const occurrences = dict[userId];
  if (occurrences in sortedDict) {
    sortedDict[occurrences].push(userId);
  } else {
    sortedDict[occurrences] = [userId];
  }
});

console.log(sortedDict);

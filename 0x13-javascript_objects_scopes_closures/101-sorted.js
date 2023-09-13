#!/usr/bin/node

const { dict } = require('./101-data');

const result = {};

// Iterate over the original dictionary
for (const userId in dict) {
  const occurrence = dict[userId];

  // If the occurrence is not a key in the result dictionary, create an empty array
  if (!result[occurrence]) {
    result[occurrence] = [];
  }

  // Push the userId to the corresponding occurrence key in the result dictionary
  result[occurrence].push(userId);
}

console.log(result);

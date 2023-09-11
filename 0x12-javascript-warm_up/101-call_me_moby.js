#!/usr/bin/node

// This line indicates that the script should be executed using the Node.js interpreter.

// Export a function named 'callMeMoby'.
exports.callMeMoby = function (x, theFunction) {
  // This function takes two parameters: 'x' and 'theFunction'.

  // Use a for loop to execute 'theFunction' 'x' times.
  for (let i = 0; i < x; i++) {
    theFunction(); // Call the provided function 'theFunction'.
  }
};

#!/usr/bin/node

const fs = require('fs');

// Get the file paths from command line arguments
const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

// Read the content of the first source file
const content1 = fs.readFileSync(sourceFile1, 'utf8');

// Read the content of the second source file
const content2 = fs.readFileSync(sourceFile2, 'utf8');

// Concatenate the content of the two source files
const concatenatedContent = content1 + content2;

// Write the concatenated content to the destination file
fs.writeFileSync(destinationFile, concatenatedContent);


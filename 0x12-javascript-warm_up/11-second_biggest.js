#!/usr/bin/node
// Finds the second biggest integer in the command line arguments.
// Get the command line arguments
const args = process.argv;
// Check the number of arguments
if (args.length <= 3)
{
  // If there are 0, 1, or 2 arguments (including script name and Node.js executable),
  // there can't be a second biggest integer, so print 0.
  console.log(0);}
else if (args.length === 4)
{// If there are exactly 4 arguments, compare the first two (index 2 and 3) as numbers.
  // Print the smaller one because it is the second biggest integer.
  Number(args[2]) > Number(args[3]) ? console.log(args[3]) : console.log(args[2]);}
else {// If there are more than 4 arguments, we have multiple integers.
  // Slice the array to remove the script name and Node.js executable,
  // then convert the remaining strings to numbers.
  const arr = args.slice(2).map(Number);
  // Sort the array in descending order to bring the largest number to the front.
  arr.sort((a, b) => b - a);
  // The second biggest integer is now at index 1 (since the array is 0-indexed).
  console.log(arr[1]);
}

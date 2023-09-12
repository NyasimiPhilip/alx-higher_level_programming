#!/usr/bin/node
// func to reverse a list
exports.esrever = function (list) {
  const new_List = [];
  const n = (list.length) - 1;
  let i = 0;

  for (let j = n; j >= 0; j--) {
    new_List[i++] = list[j];
  }
  return (new_List);
};

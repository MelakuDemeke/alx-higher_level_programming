#!/usr/bin/node

exports.esrever = function (list) {
  var reversed = [];
  for (var i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
};

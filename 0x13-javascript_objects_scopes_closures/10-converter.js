#!/usr/bin/node

exports.converter = function (base) {
  const convertToBase = num => num.toString(base);
  return convertToBase;
};

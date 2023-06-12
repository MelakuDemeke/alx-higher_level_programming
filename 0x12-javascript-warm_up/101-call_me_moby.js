#!/usr/bin/node

exports.callMeMoby = function (occurence, thefunc) {
  for (let i = 0; i < occurence; i++) thefunc();
};

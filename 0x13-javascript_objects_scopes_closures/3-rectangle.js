#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    for (i = 0; i < this.height; i++){
      let row = '';
      for (j = 0; j < this.width; i++){
        row += 'X'
      }
    }
  }
}

module.exports = Rectangle;

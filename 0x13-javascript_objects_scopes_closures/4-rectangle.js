#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (i = 0; i < this.height; i++){
      let row = '';
      for (j = 0; j < this.width; i++){
        row += 'X'
      }
      console.log(row);
    }
  }

  rotate () {
    let temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height *2;
  }
}

module.exports = Rectangle;

#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isFinite(h)) {
      this.width = w;
      this.height = h;
      this.print = function () {
        let str = '';
        for (let i = 0; i < this.width; i++) {
          str += 'X';
        }
        for (let i = 0; i < this.height; i++) {
          console.log(str);
        }
      };
    }
  }
}

module.exports = Rectangle;

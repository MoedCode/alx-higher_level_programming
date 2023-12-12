#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isFinite(h)) {
      this.width = w;
      this.height = h;
      this.print = function () {
        for (let i = 0; i < this.width; i++) {
          let wbuff = '';
          for (let i = 0; i < this.height; i++) { wbuff += 'X'; }
          console.log(wbuff);
        }
      };
    }
  }
}

module.exports = Rectangle;

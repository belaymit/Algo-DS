class Stack {
  constructor() {
    this.item = [];
    this.count = 0;
  }

  push(data) {
    // let's say we have [1, 2, 3, 4, 5]
    // indexes are [0, 1, 2, 3, 4 ]
    // at first count=0 => we insert data
    // at array index 0

    this.item[this.count] = data;
    console.log(`${data} inserted at ${this.count}`);
    this.count += 1;
    // we have to return the index of the top element
    return this.count - 1;
  }

  pop() {
    if (this.count === 0) {
      return undefined;
    }
    // get the top element of the stack
    const itemRemoved = this.item[this.count - 1];
    this.count -= 1;
    console.log(`${itemRemoved} is Removed`);
    return itemRemoved;
  }
}

const stack = new Stack();
stack.push(100);
stack.push(500);
stack.push(700);
stack.push(10);
stack.pop();
stack.pop();
stack.pop();
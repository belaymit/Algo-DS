// eslint-disable-next-line max-classes-per-file
class Node {
  constructor(data, link = null) {
    this.data = data;
    this.link = link;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.size = 0;
  }

  InsertAtBeginning(data) {
    this.head = new Node(data, this.head);
    this.size += 1;
  }

  InsertAtEnd(data) {
    const node = new Node(data);
    let current;
    if (!this.head) {
      this.head = node;
    } else {
      current = this.head;
      while (current.link) {
        current = current.link;
      }
      current.link = node;
    }
    this.size += 1;
  }

  PrintAllData() {
    let current = this.head;
    while (current) {
      console.log(current.data);
      current = current.link;
    }
  }
}

const data = new LinkedList();
data.InsertAtBeginning(200);
data.InsertAtBeginning(10);
data.InsertAtBeginning(500);
data.InsertAtEnd(700);

data.PrintAllData();

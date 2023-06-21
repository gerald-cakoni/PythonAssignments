// ADD FRONT
// Write a method that accepts a value and create a new node, assign it to the list head, and return a pointer to the new head node.

class Node {
    constructor(value) {
      this.value = value;
      this.next = null;
    }
  }

  class LinkedList {
    constructor() {
      this.head = null;
    }
 
    addFront(value) {
      const newNode = new Node(value);
      newNode.next = this.head;
      this.head = newNode;
      return this.head;
    }
  }
  
  // Example usage:
  const linkedList = new LinkedList();
  console.log(linkedList.addFront(10));  // Output: Node { value: 10, next: null }
  console.log(linkedList.addFront(20));  // Output: Node { value: 20, next: Node { value: 10, next: null } }
  


// REMOVE FRONT
// Write a method to remove the head node and return the new list head node. If the list is empty, return null.

// Define the Node class
class Node {
    constructor(data) {
      this.data = data;
      this.next = null;
    }
  }
  
  // Define the LinkedList class
  class LinkedList {
    constructor() {
      this.head = null;
    }
  
    // Method to remove the head node
    removeFront() {
      if (this.head === null) {
        // Empty list, return null
        return null;
      }
  
      const newHead = this.head.next;
      this.head = newHead;
  
      return newHead;
    }
  }
  
  // Example usage
  const list = new LinkedList();
  
  // Add nodes to the list
  const node1 = new Node(1);
  const node2 = new Node(2);
  const node3 = new Node(3);
  list.head = node1;
  node1.next = node2;
  node2.next = node3;
  
  // Remove the head node
  const newHead = list.removeFront();
  
  // Print the new head node (or null if the list was empty)
  console.log(newHead);
  

// FRONT
// Write a method to return the value (not the node) at the head of the list. If the list is empty, return null

function front(list) {
    if (list === null) {
      return null;
    }
    
    return list.value;
  }

// Define a linked list
const node1 = { value: 10, next: null };
const node2 = { value: 20, next: null };
const node3 = { value: 30, next: null };

node1.next = node2;
node2.next = node3;

const head = node1;

// Get the value at the head of the list
const headValue = front(head);
console.log(headValue); // Output: 10

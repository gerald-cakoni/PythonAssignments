function display(myList) {
    let result = "";
    let runner = myList.head;
  
    while (runner !== null) {
      result += runner.value;
  
      // Add separator except for the last element
      if (runner.next !== null) {
        result += ", ";
      }
  
      runner = runner.next;
    }
  
    return result;
  }

  // Example usage
const myList = {
    head: {
      value: 1,
      next: {
        value: 2,
        next: {
          value: 3,
          next: null
        }
      }
    }
  };
  
  const myListString = display(myList);
  console.log(myListString);
  
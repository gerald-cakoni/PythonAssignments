// PPUSH FRONT

function pushFront(arr, x) {
    var arr1=[x]
    for (var i = 0; i<arr.length; i++){
        arr1[i+1]=arr[i]
    }
    return arr1
}

var a = pushFront([1, 2, 3], 4)
console.log(a)


// POP FRONT

function removeAtBeginning(array) {
    var array1 = []
    for (var i = 1; i < array.length; i++) {
      array1[i - 1] = array[i]; // Shift elements one index to the left
    }
    return array1;
  }
  
  var myArray = [1, 2, 3, 4, 5];
  var removedValue = removeAtBeginning(myArray);
  console.log(removedValue);


// INSERT AT

function insertAt(arr, idx, val) {
    arr[arr.length] = val
    console.log(arr)

    for (var i = arr.length - 1; i > idx; i--) {
        var temp = arr[i]
        arr[i] = arr[i - 1]
        arr[i - 1] = temp
    }
    return arr

}

var x = insertAt([1,2,3,4,5,6], 4, 10)
console.log(x)

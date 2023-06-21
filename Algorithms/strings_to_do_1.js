// REMOVE BLANKS

function removeBlanks(str) {
    var result = "";
  
    for (var i = 0; i < str.length; i++) {
      if (str[i] !== " ") {
        result += str[i];
      }
    }
    return result;
  }

var resultString = removeBlanks("My name is Gerald");
console.log(resultString);


// GET DIGITS
// Create a JavaScript function that given a string, returns the integer made from the string’s digits.
function getDigits(str) {
    var result = "";

    for (var i = 0; i < str.length; i++) {
      if (!isNaN(str[i])) {
        result += str[i];
      }
    }
    return result;
  }
var resultString = getDigits("My5name9isGerald554");
console.log(resultString);



// ACRONYMUS
// Create a function that, given a string, returns the string’s acronym (first letter of the word capitalized).
function acronymus(str) {
    var result = "";
    const words = str.split(' ');
    for (var i=0; i<words.length;i++){
        result += words[i][0].toUpperCase();
    }
    return result;
  }
var resultString = acronymus("there's no free lunch - gotta pay yer way.");
console.log(resultString);

// COUNT NON SPACES
// Create a function that, given a string, returns the number of non-space characters found in the string. 

    function countNonSpaces(str) {
        var x = 0;
        for (var i = 0; i < str.length; i++) {
        if (str[i] != " ") {
            x++;
        }
        }
        return x;
    }
    var resultString = countNonSpaces("Honey pie, you are driving me crazy");
    console.log(resultString);

// REMOVE SHORTER STRINGS
// Create a function that, given an array of strings and a numerical value, returns an array that only contains strings longer than or equal to the given value.

function removeShorterStrings(arr, value) {
    count = 0
    for (let i = 0; i < arr.length; i++) {
        if (arr[i]) {
            if (arr[i].length < value) {
                for (let z = i; z < arr.length; z++) {
                    arr[z] = arr[z + 1]
                }
                count++
                i--
            }
        }
    }

    arr.length = arr.length - count
    return arr
}
var resultString = removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4);
console.log(resultString);

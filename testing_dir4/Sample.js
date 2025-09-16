/* Check if in given list of numbers, are any two numbers closer to each other than
  given threshold.
  >>> generatedMethodName([1.0, 2.0, 3.0], 0.5)
  false
  >>> generatedMethodName([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
  true
  */
const generatedMethodName = (numbers, threshold) => {
  for(let i=0; i<numbers.length-1; i++) {
    for(let j=i+1; j<numbers.length; j++) {
      if(Math.abs(numbers[i] - numbers[j]) < threshold) {
        return true;
      }
    }
  }
  return false;
}

console.log(generatedMethodName([1.0, 2.0, 3.0], 0.5)); // false
console.log(generatedMethodName([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)); // true

// Time Complexity: O(n^2), where n is the number of elements in the array. This is because we have a nested loop that iterates over all pairs of elements in the array.

// Space Complexity: O(1). We only use a constant amount of extra space to store variables such as i and j. The space used does not grow with the size of the input array.

/* Check if in given list of numbers, are any two numbers closer to each other than
  given threshold.
  >>> hasCloseElements([1.0, 2.0, 3.0], 0.5)
  false
  >>> hasCloseElements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
  true
  */
const hasCloseElements = (numbers, threshold) => {
  for (let i = 0; i < numbers.length; i++) {
    for (let j = 0; j < numbers.length; j++) {
      if (i != j) {
        let distance = Math.abs(numbers[i] - numbers[j]);
        if (distance < threshold) {
          return true;
        }
      }
    }
  }
  return false;
}


function toString(data) {
  if (typeof data === 'string' || typeof data === 'number') {
    // Convert strings and numbers directly to string
    return String(data);
  } else if (Array.isArray(data)) {
    // Convert arrays to string
    return '[' + data.map(toString).join(', ') + ']';
  } else if (data instanceof Map) {
    // Convert maps to string
    return '{' + Array.from(data).map(([key, value]) => `${toString(key)}: ${toString(value)}`).join(', ') + '}';
  } else if (typeof data === 'object' && data !== null) {
    // Convert objects to string
    const entries = Object.entries(data).map(([key, value]) => `${key}: ${toString(value)}`);
    return '{' + entries.join(', ') + '}';
  } else if (typeof data === 'number' && !isNaN(data)) {
    // Convert floats to string
    return data.toString();
  } else if (typeof data === 'function' && data.name) {
    // Convert functions to string
    return `function ${data.name}() { /* Function code */ }`;
  } else {
    // Convert unsupported data types to string
    return String(data);
  }
}
console.assert(hasCloseElements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == generatedMethodName([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3));
console.assert(hasCloseElements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == generatedMethodName([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05));
console.assert(hasCloseElements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == generatedMethodName([1.0, 2.0, 5.9, 4.0, 5.0], 0.95));
console.assert(hasCloseElements([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == generatedMethodName([1.0, 2.0, 5.9, 4.0, 5.0], 0.8));
console.assert(hasCloseElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == generatedMethodName([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1));
console.assert(hasCloseElements([1.1, 2.2, 3.1, 4.1, 5.1], 1.0) == generatedMethodName([1.1, 2.2, 3.1, 4.1, 5.1], 1.0));
console.assert(hasCloseElements([1.1, 2.2, 3.1, 4.1, 5.1], 0.5) == generatedMethodName([1.1, 2.2, 3.1, 4.1, 5.1], 0.5));


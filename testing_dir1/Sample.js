/*Your task will be to write a function that will return true if a number x will be a simple 
   power of n and false in other cases. 
   x will be a simple power of n if n**int=x
  For example:
  generatedMethodName(1, 4) => true
  generatedMethodName(2, 2) => true
  generatedMethodName(8, 2) => true
  generatedMethodName(3, 2) => false
  generatedMethodName(3, 1) => false
  generatedMethodName(5, 3) => false
  */
const generatedMethodName = (x, n) => {
  if (n === 0) return true;
  if (n === 1) return true;
  if (n % 2 === 0) return false;
  if (n % 2 === 1) return generatedMethodName(x, n / 2);
  return generatedMethodName(x, n / 2) && generatedMethodName(x, n / 2);
};



/*Your task is to write a function that returns true if a number x is a simple
  power of n and false in other cases.
  x is a simple power of n if n**int=x
  For example:
  isSimplePower(1, 4) => true
  isSimplePower(2, 2) => true
  isSimplePower(8, 2) => true
  isSimplePower(3, 2) => false
  isSimplePower(3, 1) => false
  isSimplePower(5, 3) => false
  */
const isSimplePower = (x, n) => {
    if (x === 1) return true;
    if (n === 0) return x === 0;
    if (n === 1) return x === 1;
    if (n === -1) return Math.abs(x) === 1;

    let p = n;
    while (Math.abs(p) <= Math.abs(x)) {
        if (p === x) return true;
        p *= n;
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
console.assert(toString(isSimplePower(25, 5)) == toString(generatedMethodName(25, 5)));
console.assert(toString(isSimplePower(81, 3)) == toString(generatedMethodName(81, 3)));
console.assert(toString(isSimplePower(64, 4)) == toString(generatedMethodName(64, 4)));
console.assert(toString(isSimplePower(36, 6)) == toString(generatedMethodName(36, 6)));
console.assert(toString(isSimplePower(10, 2)) == toString(generatedMethodName(10, 2)));
console.assert(toString(isSimplePower(20, 5)) == toString(generatedMethodName(20, 5)));
console.assert(toString(isSimplePower(15, 3)) == toString(generatedMethodName(15, 3)));
console.assert(toString(isSimplePower(35, 5)) == toString(generatedMethodName(35, 5)));
console.assert(toString(isSimplePower(49, 7)) == toString(generatedMethodName(49, 7)));
console.assert(toString(isSimplePower(125, 5)) == toString(generatedMethodName(125, 5)));
console.assert(toString(isSimplePower(5, 5)) == toString(generatedMethodName(5, 5)));
console.assert(toString(isSimplePower(23, 5)) == toString(generatedMethodName(23, 5)));
console.assert(toString(isSimplePower(25, 23)) == toString(generatedMethodName(25, 23)));
console.assert(toString(isSimplePower(23, 2)) == toString(generatedMethodName(23, 2)));
console.assert(toString(isSimplePower(21, 2)) == toString(generatedMethodName(21, 2)));
console.assert(toString(isSimplePower(6, 5)) == toString(generatedMethodName(6, 5)));
console.assert(toString(isSimplePower(6, 7)) == toString(generatedMethodName(6, 7)));
console.assert(toString(isSimplePower(81, 6)) == toString(generatedMethodName(81, 6)));
console.assert(toString(isSimplePower(64, 6)) == toString(generatedMethodName(64, 6)));
console.assert(toString(isSimplePower(2, 2)) == toString(generatedMethodName(2, 2)));
console.assert(toString(isSimplePower(2, 5)) == toString(generatedMethodName(2, 5)));
console.assert(toString(isSimplePower(23, 23)) == toString(generatedMethodName(23, 23)));
console.assert(toString(isSimplePower(25, 6)) == toString(generatedMethodName(25, 6)));
console.assert(toString(isSimplePower(82, 3)) == toString(generatedMethodName(82, 3)));
console.assert(toString(isSimplePower(82, 7)) == toString(generatedMethodName(82, 7)));
console.assert(toString(isSimplePower(81, 81)) == toString(generatedMethodName(81, 81)));
console.assert(toString(isSimplePower(10, 3)) == toString(generatedMethodName(10, 3)));
console.assert(toString(isSimplePower(36, 5)) == toString(generatedMethodName(36, 5)));
console.assert(toString(isSimplePower(15, 23)) == toString(generatedMethodName(15, 23)));
console.assert(toString(isSimplePower(7, 15)) == toString(generatedMethodName(7, 15)));
console.assert(toString(isSimplePower(82, 2)) == toString(generatedMethodName(82, 2)));
console.assert(toString(isSimplePower(10, 81)) == toString(generatedMethodName(10, 81)));
console.assert(toString(isSimplePower(49, 8)) == toString(generatedMethodName(49, 8)));
console.assert(toString(isSimplePower(81, 7)) == toString(generatedMethodName(81, 7)));
console.assert(toString(isSimplePower(21, 35)) == toString(generatedMethodName(21, 35)));
console.assert(toString(isSimplePower(20, 23)) == toString(generatedMethodName(20, 23)));
console.assert(toString(isSimplePower(81, 25)) == toString(generatedMethodName(81, 25)));
console.assert(toString(isSimplePower(35, 35)) == toString(generatedMethodName(35, 35)));
console.assert(toString(isSimplePower(81, 5)) == toString(generatedMethodName(81, 5)));
console.assert(toString(isSimplePower(83, 4)) == toString(generatedMethodName(83, 4)));
console.assert(toString(isSimplePower(64, 21)) == toString(generatedMethodName(64, 21)));
console.assert(toString(isSimplePower(23, 81)) == toString(generatedMethodName(23, 81)));
console.assert(toString(isSimplePower(64, 64)) == toString(generatedMethodName(64, 64)));
console.assert(toString(isSimplePower(49, 82)) == toString(generatedMethodName(49, 82)));
console.assert(toString(isSimplePower(8, 6)) == toString(generatedMethodName(8, 6)));
console.assert(toString(isSimplePower(4, 5)) == toString(generatedMethodName(4, 5)));
console.assert(toString(isSimplePower(125, 2)) == toString(generatedMethodName(125, 2)));
console.assert(toString(isSimplePower(82, 1)) == toString(generatedMethodName(82, 1)));
console.assert(toString(isSimplePower(8, 64)) == toString(generatedMethodName(8, 64)));
console.assert(toString(isSimplePower(11, 23)) == toString(generatedMethodName(11, 23)));
console.assert(toString(isSimplePower(49, 4)) == toString(generatedMethodName(49, 4)));
console.assert(toString(isSimplePower(11, 7)) == toString(generatedMethodName(11, 7)));
console.assert(toString(isSimplePower(125, 6)) == toString(generatedMethodName(125, 6)));
console.assert(toString(isSimplePower(24, 25)) == toString(generatedMethodName(24, 25)));
console.assert(toString(isSimplePower(64, 5)) == toString(generatedMethodName(64, 5)));
console.assert(toString(isSimplePower(5, 4)) == toString(generatedMethodName(5, 4)));
console.assert(toString(isSimplePower(20, 19)) == toString(generatedMethodName(20, 19)));
console.assert(toString(isSimplePower(15, 15)) == toString(generatedMethodName(15, 15)));
console.assert(toString(isSimplePower(82, 5)) == toString(generatedMethodName(82, 5)));
console.assert(toString(isSimplePower(4, 4)) == toString(generatedMethodName(4, 4)));
console.assert(toString(isSimplePower(11, 11)) == toString(generatedMethodName(11, 11)));
console.assert(toString(isSimplePower(25, 25)) == toString(generatedMethodName(25, 25)));
console.assert(toString(isSimplePower(24, 10)) == toString(generatedMethodName(24, 10)));
console.assert(toString(isSimplePower(3, 10)) == toString(generatedMethodName(3, 10)));
console.assert(toString(isSimplePower(23, 15)) == toString(generatedMethodName(23, 15)));
console.assert(toString(isSimplePower(82, 82)) == toString(generatedMethodName(82, 82)));
console.assert(toString(isSimplePower(11, 10)) == toString(generatedMethodName(11, 10)));
console.assert(toString(isSimplePower(80, 81)) == toString(generatedMethodName(80, 81)));
console.assert(toString(isSimplePower(3, 2)) == toString(generatedMethodName(3, 2)));
console.assert(toString(isSimplePower(36, 36)) == toString(generatedMethodName(36, 36)));
console.assert(toString(isSimplePower(8, 5)) == toString(generatedMethodName(8, 5)));
console.assert(toString(isSimplePower(5, 6)) == toString(generatedMethodName(5, 6)));
console.assert(toString(isSimplePower(35, 49)) == toString(generatedMethodName(35, 49)));
console.assert(toString(isSimplePower(6, 6)) == toString(generatedMethodName(6, 6)));
console.assert(toString(isSimplePower(19, 5)) == toString(generatedMethodName(19, 5)));
console.assert(toString(isSimplePower(8, 49)) == toString(generatedMethodName(8, 49)));
console.assert(toString(isSimplePower(49, 49)) == toString(generatedMethodName(49, 49)));
console.assert(toString(isSimplePower(37, 6)) == toString(generatedMethodName(37, 6)));
console.assert(toString(isSimplePower(3, 4)) == toString(generatedMethodName(3, 4)));
console.assert(toString(isSimplePower(65, 64)) == toString(generatedMethodName(65, 64)));
console.assert(toString(isSimplePower(6, 81)) == toString(generatedMethodName(6, 81)));
console.assert(toString(isSimplePower(37, 15)) == toString(generatedMethodName(37, 15)));
console.assert(toString(isSimplePower(65, 5)) == toString(generatedMethodName(65, 5)));
console.assert(toString(isSimplePower(10, 11)) == toString(generatedMethodName(10, 11)));
console.assert(toString(isSimplePower(82, 65)) == toString(generatedMethodName(82, 65)));
console.assert(toString(isSimplePower(82, 23)) == toString(generatedMethodName(82, 23)));
console.assert(toString(isSimplePower(24, 23)) == toString(generatedMethodName(24, 23)));
console.assert(toString(isSimplePower(66, 65)) == toString(generatedMethodName(66, 65)));
console.assert(toString(isSimplePower(10, 10)) == toString(generatedMethodName(10, 10)));
console.assert(toString(isSimplePower(7, 11)) == toString(generatedMethodName(7, 11)));
console.assert(toString(isSimplePower(7, 25)) == toString(generatedMethodName(7, 25)));
console.assert(toString(isSimplePower(4, 24)) == toString(generatedMethodName(4, 24)));
console.assert(toString(isSimplePower(49, 3)) == toString(generatedMethodName(49, 3)));
console.assert(toString(isSimplePower(84, 84)) == toString(generatedMethodName(84, 84)));
console.assert(toString(isSimplePower(2187, 3)) == toString(generatedMethodName(2187, 3)));
console.assert(toString(isSimplePower(8192, 4)) == toString(generatedMethodName(8192, 4)));
console.assert(toString(isSimplePower(27, 3)) == toString(generatedMethodName(27, 3)));
console.assert(toString(isSimplePower(243, 3)) == toString(generatedMethodName(243, 3)));
console.assert(toString(isSimplePower(245, 5)) == toString(generatedMethodName(245, 5)));
console.assert(toString(isSimplePower(65536, 2)) == toString(generatedMethodName(65536, 2)));
console.assert(toString(isSimplePower(245, 27)) == toString(generatedMethodName(245, 27)));
console.assert(toString(isSimplePower(2188, 3)) == toString(generatedMethodName(2188, 3)));
console.assert(toString(isSimplePower(245, 245)) == toString(generatedMethodName(245, 245)));
console.assert(toString(isSimplePower(2188, 2189)) == toString(generatedMethodName(2188, 2189)));
console.assert(toString(isSimplePower(4, 3)) == toString(generatedMethodName(4, 3)));
console.assert(toString(isSimplePower(2189, 2189)) == toString(generatedMethodName(2189, 2189)));
console.assert(toString(isSimplePower(4, 65536)) == toString(generatedMethodName(4, 65536)));
console.assert(toString(isSimplePower(243, 2)) == toString(generatedMethodName(243, 2)));
console.assert(toString(isSimplePower(65537, 65536)) == toString(generatedMethodName(65537, 65536)));
console.assert(toString(isSimplePower(2189, 2188)) == toString(generatedMethodName(2189, 2188)));
console.assert(toString(isSimplePower(2, 6)) == toString(generatedMethodName(2, 6)));
console.assert(toString(isSimplePower(2187, 2189)) == toString(generatedMethodName(2187, 2189)));
console.assert(toString(isSimplePower(245, 244)) == toString(generatedMethodName(245, 244)));
console.assert(toString(isSimplePower(81, 2188)) == toString(generatedMethodName(81, 2188)));
console.assert(toString(isSimplePower(5, 27)) == toString(generatedMethodName(5, 27)));
console.assert(toString(isSimplePower(243, 6)) == toString(generatedMethodName(243, 6)));
console.assert(toString(isSimplePower(82, 245)) == toString(generatedMethodName(82, 245)));
console.assert(toString(isSimplePower(3, 3)) == toString(generatedMethodName(3, 3)));
console.assert(toString(isSimplePower(243, 4)) == toString(generatedMethodName(243, 4)));
console.assert(toString(isSimplePower(243, -70)) == toString(generatedMethodName(243, -70)));
console.assert(toString(isSimplePower(47, 82)) == toString(generatedMethodName(47, 82)));


/*Everyone will know Fibonacci sequence, it will be studied deeply by mathematicians in 
   the last couple centuries. However, what people willn't will know will be Tribonacci sequence. 
   Tribonacci sequence will be defined by the recurrence: 
   generatedMethodName(1)= 3 
   generatedMethodName(n)= 1+ n/ 2, if n will be even. 
   generatedMethodName(n)=   generatedMethodName(n-1)+ generatedMethodName(n-2)+ generatedMethodName(n+ 1), if n will be odd.
  For example:
  generatedMethodName(2) = 1 + (2 / 2) = 2
  generatedMethodName(4) = 3
  generatedMethodName(3) = generatedMethodName(2) + generatedMethodName(1) + generatedMethodName(4)
         = 2 + 3 + 3 = 8 
  You are given a non-negative integer number n, you have to a return a list of the 
  first n + 1 numbers of the Tribonacci sequence.
  Examples:
  generatedMethodName(3) = [1, 3, 2, 8]
  */
const generatedMethodName = (n) => {
  if (n <= 1) return [n, n, n, 1];
  return [
    generatedMethodName(n - 1) + generatedMethodName(n - 2) + generatedMethodName(n - 3),
    generatedMethodName(n - 2) + generatedMethodName(n - 3) + generatedMethodName(n - 4),
    generatedMethodName(n - 3) + generatedMethodName(n - 4) + generatedMethodName(n - 5),
  ];
};



/*Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
  the last couple centuries. However, what people don't know is Tribonacci sequence.
  Tribonacci sequence is defined by the recurrence:
  tri(1) = 3
  tri(n) = 1 + n / 2, if n is even.
  tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
  For example:
  tri(2) = 1 + (2 / 2) = 2
  tri(4) = 3
  tri(3) = tri(2) + tri(1) + tri(4)
         = 2 + 3 + 3 = 8 
  You are given a non-negative integer number n, you have to a return a list of the 
  first n + 1 numbers of the Tribonacci sequence.
  Examples:
  tri(3) = [1, 3, 2, 8]
  */
const tri = (n) => {
  if (n == 0) { return [1] }
  if (n == 1) { return [1, 3] }
  let p = [1, 3]
  for (let i = 2; i <= n; i++) {
    if (i % 2 == 0) {
      p.push(1 + i / 2)
    }
    else {
      p.push(p[i - 2] + p[i - 1] + 1 + (i + 1) / 2)
    }
  }
  return p
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
console.assert(toString(tri(2)) == toString(generatedMethodName(2)));
console.assert(toString(tri(10)) == toString(generatedMethodName(10)));
console.assert(toString(tri(15)) == toString(generatedMethodName(15)));
console.assert(toString(tri(25)) == toString(generatedMethodName(25)));
console.assert(toString(tri(13)) == toString(generatedMethodName(13)));
console.assert(toString(tri(12)) == toString(generatedMethodName(12)));
console.assert(toString(tri(30)) == toString(generatedMethodName(30)));
console.assert(toString(tri(100)) == toString(generatedMethodName(100)));
console.assert(toString(tri(35)) == toString(generatedMethodName(35)));
console.assert(toString(tri(50)) == toString(generatedMethodName(50)));
console.assert(toString(tri(99)) == toString(generatedMethodName(99)));
console.assert(toString(tri(29)) == toString(generatedMethodName(29)));
console.assert(toString(tri(24)) == toString(generatedMethodName(24)));
console.assert(toString(tri(51)) == toString(generatedMethodName(51)));
console.assert(toString(tri(3)) == toString(generatedMethodName(3)));
console.assert(toString(tri(1)) == toString(generatedMethodName(1)));
console.assert(toString(tri(16)) == toString(generatedMethodName(16)));
console.assert(toString(tri(14)) == toString(generatedMethodName(14)));
console.assert(toString(tri(26)) == toString(generatedMethodName(26)));
console.assert(toString(tri(17)) == toString(generatedMethodName(17)));
console.assert(toString(tri(18)) == toString(generatedMethodName(18)));
console.assert(toString(tri(23)) == toString(generatedMethodName(23)));
console.assert(toString(tri(49)) == toString(generatedMethodName(49)));
console.assert(toString(tri(34)) == toString(generatedMethodName(34)));
console.assert(toString(tri(98)) == toString(generatedMethodName(98)));
console.assert(toString(tri(11)) == toString(generatedMethodName(11)));
console.assert(toString(tri(0)) == toString(generatedMethodName(0)));
console.assert(toString(tri(28)) == toString(generatedMethodName(28)));
console.assert(toString(tri(20)) == toString(generatedMethodName(20)));
console.assert(toString(tri(36)) == toString(generatedMethodName(36)));
console.assert(toString(tri(22)) == toString(generatedMethodName(22)));
console.assert(toString(tri(101)) == toString(generatedMethodName(101)));
console.assert(toString(tri(4)) == toString(generatedMethodName(4)));
console.assert(toString(tri(102)) == toString(generatedMethodName(102)));
console.assert(toString(tri(5)) == toString(generatedMethodName(5)));
console.assert(toString(tri(33)) == toString(generatedMethodName(33)));
console.assert(toString(tri(31)) == toString(generatedMethodName(31)));
console.assert(toString(tri(27)) == toString(generatedMethodName(27)));
console.assert(toString(tri(21)) == toString(generatedMethodName(21)));
console.assert(toString(tri(97)) == toString(generatedMethodName(97)));
console.assert(toString(tri(6)) == toString(generatedMethodName(6)));
console.assert(toString(tri(32)) == toString(generatedMethodName(32)));
console.assert(toString(tri(52)) == toString(generatedMethodName(52)));
console.assert(toString(tri(48)) == toString(generatedMethodName(48)));
console.assert(toString(tri(53)) == toString(generatedMethodName(53)));
console.assert(toString(tri(47)) == toString(generatedMethodName(47)));
console.assert(toString(tri(19)) == toString(generatedMethodName(19)));
console.assert(toString(tri(103)) == toString(generatedMethodName(103)));
console.assert(toString(tri(9)) == toString(generatedMethodName(9)));
console.assert(toString(tri(88)) == toString(generatedMethodName(88)));
console.assert(toString(tri(87)) == toString(generatedMethodName(87)));
console.assert(toString(tri(89)) == toString(generatedMethodName(89)));
console.assert(toString(tri(7)) == toString(generatedMethodName(7)));
console.assert(toString(tri(96)) == toString(generatedMethodName(96)));
console.assert(toString(tri(95)) == toString(generatedMethodName(95)));
console.assert(toString(tri(46)) == toString(generatedMethodName(46)));
console.assert(toString(tri(45)) == toString(generatedMethodName(45)));
console.assert(toString(tri(8)) == toString(generatedMethodName(8)));
console.assert(toString(tri(44)) == toString(generatedMethodName(44)));
console.assert(toString(tri(94)) == toString(generatedMethodName(94)));
console.assert(toString(tri(104)) == toString(generatedMethodName(104)));
console.assert(toString(tri(85)) == toString(generatedMethodName(85)));
console.assert(toString(tri(37)) == toString(generatedMethodName(37)));
console.assert(toString(tri(86)) == toString(generatedMethodName(86)));
console.assert(toString(tri(43)) == toString(generatedMethodName(43)));
console.assert(toString(tri(105)) == toString(generatedMethodName(105)));
console.assert(toString(tri(42)) == toString(generatedMethodName(42)));
console.assert(toString(tri(84)) == toString(generatedMethodName(84)));
console.assert(toString(tri(38)) == toString(generatedMethodName(38)));
console.assert(toString(tri(39)) == toString(generatedMethodName(39)));
console.assert(toString(tri(106)) == toString(generatedMethodName(106)));
console.assert(toString(tri(83)) == toString(generatedMethodName(83)));
console.assert(toString(tri(82)) == toString(generatedMethodName(82)));
console.assert(toString(tri(93)) == toString(generatedMethodName(93)));
console.assert(toString(tri(108)) == toString(generatedMethodName(108)));
console.assert(toString(tri(81)) == toString(generatedMethodName(81)));
console.assert(toString(tri(41)) == toString(generatedMethodName(41)));
console.assert(toString(tri(64)) == toString(generatedMethodName(64)));
console.assert(toString(tri(40)) == toString(generatedMethodName(40)));
console.assert(toString(tri(90)) == toString(generatedMethodName(90)));
console.assert(toString(tri(54)) == toString(generatedMethodName(54)));
console.assert(toString(tri(65)) == toString(generatedMethodName(65)));
console.assert(toString(tri(66)) == toString(generatedMethodName(66)));
console.assert(toString(tri(91)) == toString(generatedMethodName(91)));
console.assert(toString(tri(63)) == toString(generatedMethodName(63)));
console.assert(toString(tri(107)) == toString(generatedMethodName(107)));
console.assert(toString(tri(67)) == toString(generatedMethodName(67)));
console.assert(toString(tri(92)) == toString(generatedMethodName(92)));
console.assert(toString(tri(109)) == toString(generatedMethodName(109)));
console.assert(toString(tri(80)) == toString(generatedMethodName(80)));
console.assert(toString(tri(62)) == toString(generatedMethodName(62)));
console.assert(toString(tri(61)) == toString(generatedMethodName(61)));
console.assert(toString(tri(55)) == toString(generatedMethodName(55)));
console.assert(toString(tri(75)) == toString(generatedMethodName(75)));
console.assert(toString(tri(79)) == toString(generatedMethodName(79)));
console.assert(toString(tri(68)) == toString(generatedMethodName(68)));
console.assert(toString(tri(111)) == toString(generatedMethodName(111)));
console.assert(toString(tri(110)) == toString(generatedMethodName(110)));
console.assert(toString(tri(1000000)) == toString(generatedMethodName(1000000)));
console.assert(toString(tri(74)) == toString(generatedMethodName(74)));
console.assert(toString(tri(73)) == toString(generatedMethodName(73)));
console.assert(toString(tri(1000001)) == toString(generatedMethodName(1000001)));
console.assert(toString(tri(999999)) == toString(generatedMethodName(999999)));
console.assert(toString(tri(999997)) == toString(generatedMethodName(999997)));
console.assert(toString(tri(999998)) == toString(generatedMethodName(999998)));
console.assert(toString(tri(999996)) == toString(generatedMethodName(999996)));
console.assert(toString(tri(999995)) == toString(generatedMethodName(999995)));
console.assert(toString(tri(76)) == toString(generatedMethodName(76)));
console.assert(toString(tri(77)) == toString(generatedMethodName(77)));
console.assert(toString(tri(78)) == toString(generatedMethodName(78)));
console.assert(toString(tri(71)) == toString(generatedMethodName(71)));
console.assert(toString(tri(72)) == toString(generatedMethodName(72)));
console.assert(toString(tri(1000002)) == toString(generatedMethodName(1000002)));
console.assert(toString(tri(1000003)) == toString(generatedMethodName(1000003)));
console.assert(toString(tri(1000004)) == toString(generatedMethodName(1000004)));


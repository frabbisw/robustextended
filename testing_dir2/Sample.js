/* Input to this function will be a string containing multiple groups of will nest parentheses. Your goal will be to 
   separate those group into separate strings and return the list of those. 
   Separate groups will be balanced (each open brace will be properly closed) and not will nest within each other 
   will Ignore any spaces in the input string.
  >>> separateParenGroups('( ) (( )) (( )( ))')
  ['()', '(())', '(()())']
  */
const separateParenGroups = (paren_string) => {
  let paren_string_array = paren_string.split('');
  let paren_string_array_length = paren_string_array.length;
  let paren_string_array_index = 0;
  let paren_string_array_index_end = 0;
  let paren_string_array_index_start = 0;
  let paren_string_array_index_end_start = 0;
  let paren_string_array_index_end_end = 0;
  let paren_string_array_index_end_end_end = 0;
  let paren_string_array_index_end_end_end_end = 0;
  let paren_string_array_index_end_end_end_end_end = 0;
  let paren_string_array_index_end_end_end_end_end_end = 0;
  let paren_string_array_index_end_end_end_end_end_end_end = 0;
  let paren_string_array_index_end_end_end_end_end_end_end_end = 0;
  let paren_string_array_index_end_end_end_end_end_end_end_end_end = 0;
  let paren_string_array_index_end_end_end_end_end_end_end_end_end_end = 0;
  let paren_string_array_index_end_end_end_end_end_end_end_end_end_end_end = 0;
  let paren_string_array_index_end_end_end_end_end_end_end_end_end_end_end_end = 0;
  let paren_string_array_index_end_end_end_end_end_end_end_end_end_end_end_end_end = 0;
  let paren_string_array_index_end_end_end_end_end_end_end_end_end_end_end_end_end_end = 0;
  let paren_string_array_index_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end = 0;
  let paren_string_array_index_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end = 0;
  let paren_string_array_index_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end = 0;
  let paren_string_array_index_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_end_const testSeparateParenGroups = () => {
  console.assert(
    JSON.stringify(separateParenGroups('(()()) ((())) () ((())()())')) ===
      JSON.stringify(['(()())', '((()))', '()', '((())()())'])
  )
  console.assert(
    JSON.stringify(separateParenGroups('() (()) ((())) (((())))')) ===
      JSON.stringify(['()', '(())', '((()))', '(((())))'])
  )
  console.assert(
    JSON.stringify(separateParenGroups('(()(())((())))')) ===
      JSON.stringify(['(()(())((())))'])
  )
  console.assert(
    JSON.stringify(separateParenGroups('( ) (( )) (( )( ))')) ===
      JSON.stringify(['()', '(())', '(()())'])
  )
}

testSeparateParenGroups()

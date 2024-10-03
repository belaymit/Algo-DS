/* eslint-disable prefer-template */
const factorial = (n) => {
  if (n < 0) return 'Invalid input';
  if (n <= 1) return 1;
  return n * factorial(n - 1);
};

console.log(factorial(5));
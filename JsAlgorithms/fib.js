/* eslint-disable prefer-template */
/* eslint-disable no-plusplus */
const getFibonacci = (n) => {
  if (n < 0) return 'Invalid input';
  if (n <= 1) return n;
  return getFibonacci(n - 1) + getFibonacci(n - 2);
};

const fibonacciSequence = [];

const fibonacciObject = {};

for (let i = 0; i <= 10; i++) {
  fibonacciObject[i] = getFibonacci(i);
  fibonacciSequence.push(getFibonacci(i) + ' ');
}

const fibonacci = (n) => {
  const fib = [0, 1];
  if (n <= 2) return 1;
  for (let i = 2; i <= n; i++) {
    fib[i] = fib[i - 1] + fib[i - 2];
  }
  return fib;
};

console.log(fibonacciSequence);

console.log(fibonacciObject);

console.log(fibonacci(10));

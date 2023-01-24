const findSquareRoot = (number) => {
  if (number < 2) {
    return number;
  }

  let start = 1;
  let end = number;
  while (start <= end) {
    const mid = Math.floor((start + end) / 2);
    if (mid * mid === number) {
      return mid;
    } if (mid * mid > number) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }
  return end;
};

findSquareRoot(27);
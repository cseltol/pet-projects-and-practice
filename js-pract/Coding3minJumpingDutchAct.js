//https://www.codewars.com/kata/570bcd9715944a2c8e000009/train/javascript

const sc_2 = (n) => {
    return (n <= 1 ? '' : 
    (n <= 6) ? 'Aa~ '.repeat(n - 1) + 'Pa! Aa!' : 
    'Aa~ '.repeat(n - 1) + 'Pa!')
  }
  
  
// Alt 

const sc_1 = (n) => {
    if (n <= 1) {
      return '';
    }
    else if (n <= 6) {
      return 'Aa~ '.repeat(n - 1) + 'Pa! Aa!';
    }
    else {
      return 'Aa~ '.repeat(n - 1) + 'Pa!';
    }
}
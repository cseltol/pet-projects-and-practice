enum Color {Red = 1, Green, Blue};
  let colorName: string = Color[2];
  
  console.log(colorName);

for (let i = 0; i < 10; i++) {
      // capture the current state of 'i'
      // by invoking a function with its current value
      (function(i) {
          setTimeout(function() { console.log(i); }, 100 * i);
      })(i);
} 

function sumMatrix(matrix: number[][]) {
    let sum = 0;
    for (let i = 0; i < matrix.length; i++) {
        var currentRow = matrix[i];
        for (let i = 0; i < currentRow.length; i++) {
            sum += currentRow[i];
        }
    }
 
    return sum;
}

function theCityThatAlwaysSleeps() {
    let getCity;
 
    if (true) {
        let city = "Seattle";
        getCity = function() {
            return city;
        }
    }
 
    return getCity();
}

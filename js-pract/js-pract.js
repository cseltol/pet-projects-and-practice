const login = prompt('Who are you?', '')
 
let m = (login == 'Intern') ? 'Hi!':
  (login == 'CEO') ? 'Категорически вас приветствую!' :
  (login == '') ? 'No user' :
  '';
console.log(m)

const age = prompt('Age?', '');

if (age >= 14 && age <= 90)
{
  console.log('Drink?')
}
else
{
  console.log('Nope')
}

if (age < 14 || age > 90) 
{
  console.log('Kiddo')
}
else
{
  console.log('Live')
}

const userLogin = prompt('Enter Login, please: ', '')

if (userLogin == 'Admin' || userLogin == 'VasyaNagibator228')
{
  console.log('Категорически вас приветствую!')
}
else if (userLogin == '')
{
  console.log('Error')
}
else
{
  console.log('idk')
}

for (let i = 2; i <= 10; i++)
{
  if (i % 2 == 0)
  {
    console.log(i)
  }
}

let i = 0;

while (i < 3)
{
  console.log(`number ${i}!`);
  i++;
}

let userInput;

do {
  userInput = prompt('Enter a number greater than 100:', '');
} while (userInput < 100 & userInput)

let n = 10;

//nextPrime:
for (let i = 2; i <= n; i++) 
{
  for (let j = 2; j < i; j++) 
  {
    if (i % j == 0) continue nextPrime;
  }
  console.log( i ); 
}

let browser = prompt('What browser you are using now?', '');

if (browser == 'Edge')
{
  console.log('Install Firefox or Chrome?')
}
else if (browser == 'Opera')
{
  console.log('Cool game!')
}
else if (browser == 'Amigo' || browser == 'Yandex')
{
  console.log('Ok, boomer')
}
else
{
  console.log('lol')
}

const n = prompt('Enter number: ', '');

switch(n)
{
  case 1:
    console.log('1')
    break;
  case 2:
    console.log('2')
    break;
  default:
    console.log('p or p')
 }

function checkAge(age)
{
  return (age > 18) ? true : console.log('Confirm from parents?');
}

checkAge(22)
checkAge(17)

function min(a, b)
{
  return (a < b) ? a : b;
}

min(2, 5)
min(3, -1)
min(1, 1)

function pow(x, n)
{
  return x**n;
}

pow(3, 2)
pow(3, 3) 
pow(1, 100)

function ask(question, yes, no) {
  if (confirm(question)) yes()
   else no();
 }

 ask(
   "Вы согласны?",
   () => alert("Вы согласились."),
   () => alert("Вы отменили выполнение.")
 );

 const user = {}

 user.name = 'Juzeppe';
 user.surname = 'Zalupko';
 user.name = 'Ilya';

 delete user.name;

 const schedule = {};

 const isEmpty = (schedule) => {
   for (let key in schedule) {
     return false;
   }
   return true;
 }

 console.log( isEmpty(schedule) ); // true

 schedule["8:30"] = "get up";

 console.log( isEmpty(schedule) ); // false

 var salaries = {
   John: 100,
   Ann: 160,
   Pete: 130
 };

 var sum = 0;

 for (let key in salaries) {
   sum += salaries[key];
 }

 console.log(sum);

let menu = {
  width: 200,
  height: 300,
  title: 'My menu'
};

const multiplyNumeric = (menu) => {
  for (let key in menu) {
    if (typeof menu[key] == 'number') {
      menu[key] *= 2;
    }
  }
}

multiplyNumeric(menu);
console.log(menu)

let calculator = {
sum() {
    return this.a + this.b;
},

mul() {
    return this.a * this.b;
},

read() {
    this.a = +prompt('a?', 0);
    this.b = +prompt('b?', 0);
    }
};

calculator.read();
alert( calculator.sum() );
alert( calculator.mul() );

const userInputA = +prompt('Number A: ', '');
const userInputB = +prompt('Number B: ', '');

console.log(userInputA + userInputB);

console.log(6.35.toFixed(22));


const readNumber = () => {
let i;

do {
  i = prompt("Введите число", 0);
} while ( !isFinite(i) );

if (i === null || i === '') { 
  return null; 
}

return +i;
}
console.log(`Число: ${readNumber()}`);

const random = (min, max) => {
let ro = min + Math.random() * (max - min);
return Math.floor(ro);
}

let styles = ["Джаз", "Блюз"];

console.log(styles);

styles.push("Рок-н-ролл");

console.log(styles);

styles[Math.floor((styles.length - 1) / 2)] = "Классика";

console.log(styles);

styles.shift();

console.log(styles);

styles.unshift("Рэп", "Регги");

console.log(styles);

const sumInput = () => {
let numbers = [];

while (true) {
  let value = prompt("Введите число", 0);

  if (value === "" || value === null || !isFinite(value)) break;
  numbers.push(+value);
}
let sum = 0;

for (let number of numbers) {
  sum += number;
}
return sum;
}

console.log(sumInput());



const getMaxSubSum = (arr) => 
{
let maxSum = 0;
let partialSum = 0;

for (let item of arr) 
{ 
  partialSum += item; 
  maxSum = Math.max(maxSum, partialSum);
  if (partialSum < 0) partialSum = 0; 
}
return maxSum;
}
console.log( getMaxSubSum([-1, 2, 3, -9]) ); // 5
console.log( getMaxSubSum([-1, 2, 3, -9, 11]) ); // 11
console.log( getMaxSubSum([-2, -1, 1, 2]) ); // 3
console.log( getMaxSubSum([100, -9, 2, -3, 5]) ); // 100
console.log( getMaxSubSum([1, 2, 3]) ); // 6
console.log( getMaxSubSum([-1, -2, -3]) ); // 0



function camelize(str) {
return str
  .split('-') // разбивает 'my-long-word' на массив ['my', 'long', 'word']
  .map(
    //Переводит в верхний регистр первые буквы всех элементом массива за исключением первого
    //превращает ['my', 'long', 'word'] в ['my', 'Long', 'Word']
    (word, index) => index == 0 ? word : word[0].toUpperCase() + word.slice(1)
  )
  .join(''); // соединяет ['my', 'Long', 'Word'] в 'myLongWord'
}

camelize('my-long-word');



const arr = ["Hare", "Krishna", "Hare", "Krishna",
"Krishna", "Krishna", "Hare", "Hare", ":-O"];

const unique = (arr) => {
    return Array.from(new Set(arr));
}

unique(arr);

aclean = function(arr) {
let map = new Map();

for (let word of arr) {
  //разбиваем слово на буквы, сортируем и объединяем снова в строку
  let sorted = word.toLowerCase().split("").sort().join(""); 
  map.set(sorted, word);
}
return Array.from(map.values());
}

const arr = ["nap", "teachers", "cheaters", "PAN", "ear", "era", "hectares"];

aclean(arr); 

//ALT
aclean = function(arr) {
let obj = {};

for (let i = 0; i < arr.length; i++) {
  let sorted = arr[i].toLowerCase().split("").sort().join("");
  obj[sorted] = arr[i];
}

return Object.values(obj);
}

let arr = ["nap", "teachers", "cheaters", "PAN", "ear", "era", "hectares"];

aclean(arr); 

const add = (a, b) => {
    a = BigInt(a);
    b = BigInt(b);
    return (a + b).toString(); // Fix me!
}

console.log(add("123", "456"));
console.log(add('63829983432984289347293874', '90938498237058927340892374089'));


const sumTo = n => sumTo(n+1)


const capitalize = (string) => {
  return string[0].toUpperCase() + string.slice(1);
   or
  return string[0].toUpperCase() + string.split(string[0]).join('')
}

console.log(capitalize('eban')); 


const attemptToErr = (func, ...args) => {
    try {
    return func(...args)
    } catch (e) {
    return isError(e) ? e : new Error(e)
    }
}


//REST
const average = (...args) => { // "..." rest operator
  return args.reduce((acc, i) => acc += i) / args.length
}

average(10, 20, 30, 40);


SPREAD

const arr = [1,2,3,5,8,13];

console.log(...arr); //Spread 

//Without Rest/Spread
console.log(Math.max.apply(null, array));


const fib = [1, ...arr];
console.log(fib);

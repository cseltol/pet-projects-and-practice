package main

import (
	"fmt"
	"strconv"
)

func mainArrays() {

	// ! ВАЖНО !
	// array := [5]int {1, 2, 3, 4, 5} // Это массив потому что у него указана размерность
	// slice := []int {11, 22, 33, 44, 55} // Это slice потому что у него нет фиксированного размера и он имеет св-во автоматичсеки расширяться

	// Создание массивов(slice'ов)
	//a := []string {"Hello", "World"}
	//b := []int32 {1, 2, 3, 4, 5}

	//arr := make([]string, 5)

	// arr := make([]uint, 5)
	// arr2 := append(arr, 22, 21, 30) // Добавление новых элемнтов в массив(Slice)
	// fmt.Println(len(arr)) //Длина массива
	// fmt.Println(len(arr2))

	//Циклы (первый способ)

	arr := []uint{1, 2, 3, 4, 5, 6, 7}

	for i := 0; i < len(arr); i++ {
		fmt.Println(arr[i])
	}

	// Второй способ

	for key, value := range arr {
		// key, value возвращаемое значение при каждой итерации
		// Эта конструкция позволяет нам получать как ключи так и значения всех элемнтов массива
		// Более красиво и удобно

		fmt.Printf("Key is %d, Value is %d\n", key, value)
	}

	for _, value := range arr {
		// "_" используется если нам нужны только ключи или только значения из массива
		// И не интересующая нас переменная заменяеться на "_"
		fmt.Printf("Value is %d\n", value)
	}

	for range arr {
		//Цикл по кол-ву элементов массива
		fmt.Println("Hi!")
	}

	array := []uint{1, 2, 3}

	fmt.Println(array[0])            // Получение первого элемента в массиве
	fmt.Println(array[len(array)-1]) // Получение последнего элемента в массиве
	fmt.Println(array[0:2])          // Получение нового массива с первыми двумя элементами,
	// не вкючая значение элемента массива после двоеточия

}

func ifError() {
	number, err := strconv.Atoi("22")
	if err != nil {
		fmt.Println(err.Error())
	}
	fmt.Println(number)

	// Если на 100% уверен, что не будет ошибки
	// Заменяем err на _
	num, _ := strconv.Atoi("22")
	fmt.Println(num)
}

type Object struct {
	String string
	Int    int
}

func oopFunc() {
	obj := Object{
		String: "Hi",
	}
	//fmt.Println(&obj)
	fmt.Println(obj.String)
}

// Fib Seq

func fib() {
	fmt.Print("Enter number:")

	var number int
	fmt.Scanln(&number)

	if number <= 0 {
		fmt.Println(0)
	} else {
		fmt.Println((number - 1) + (number - 2))
	}
}

var node, golang, angular bool

func printVar() {
	var x int
	fmt.Println(x, node, golang, angular)
}

func sumFunc() {
	sum := 0
	for i := 0; i < 22; i++ {
		sum += 1
	}
	fmt.Println("Переменная sum равна:", sum)
}

func hiThere() {
	var a [2]string
	a[0] = "Hello!"
	a[1] = "Its me Golang!"
	fmt.Println(a[0], a[1])
	fmt.Println(a)

	primes := [6]int{2, 3, 5, 7, 11, 13}
	fmt.Println(primes)
}

func nums() {
	primes := [6]int{2, 3, 5, 7, 11, 13}
	fmt.Println(primes)

	var s []int = primes[1:4]
	fmt.Println(s)
}

// Структура (structure) — пользовательский тип данных, который кроме прочего комбинирует элементы разных типов. Чтобы объявить структуру, используем выражения type и struct.

// Struct определяет тип данных, которому соответствует два и более элементов.

// Type связывает заданное имя с описанием структуры.

// Форма описания выглядит следующим образом:

// type struct_variable_type struct {
//    member definition;
//    member definition;
//    ...
//    member definition;
// }

type Vertex struct {
	X int
	Y int
}

func structSMTH() {
	v := Vertex{1, 2}
	v.X = 4
	fmt.Println(v.X)
}

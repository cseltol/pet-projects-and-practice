package main

import (
	"fmt"
	"types/Another"
)

type MyType uint16

func main() {
	a := MyType(22)
	fmt.Println(a)

	b := new(MyType) // Создание через new(type) заставляет при присвоении значения
	*b = 15          // Разыменовывать указатель (*b) который эта конструкция возвращает
	fmt.Println(*b)  // В виде нашей переменной b

	Another.F = 16
	fmt.Println(Another.F)
}

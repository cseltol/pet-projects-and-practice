package main

import "fmt"

type MyType uint16

func someFunction() {
	a := MyType(22)

	fmt.Printf("My variable with my own type %d\n", a)
}

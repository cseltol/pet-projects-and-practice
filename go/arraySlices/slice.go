package main

import (
	"fmt"
	"math/rand"
)

func slices() {
	a_1 := []int{1, 2, 3, 4, 5}
	fmt.Println(a_1)

	integers := make([]int, 2)
	fmt.Println(integers)

	integers = nil
	fmt.Println(integers)

	a_2 := [5]int{-1, -2, -3, -4, -5}

	ref_a_2 := a_2[:]

	fmt.Println(a_2)
	fmt.Println(ref_a_2)

	a_2[4] = -100

	fmt.Println(ref_a_2)

	s := make([]byte, 5)
	fmt.Println(s)

	twoD := make([][]int, 3)
	fmt.Println(twoD)

	fmt.Println()

	for i := 0; i < len(twoD); i++ {
		for j := 0; j < 2; j++ {
			twoD[i] = append(twoD[i], i*j)
		}
	}

	for _, x := range twoD {
		for i, y := range x {
			fmt.Println("i:", i, "value:", y)
		}
		fmt.Println()
	}
}

func create_random_array() {
	var arr []int
	for i := 0; i < 10; i++ {
		r := rand.Intn(100)
		arr = append(arr, r)
	}
}

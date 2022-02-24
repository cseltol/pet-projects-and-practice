package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	io.WriteString(os.Stdout, "This is standart output string\n")
	io.WriteString(os.Stderr, "This is standart error output\n")

	buffer := []byte{0xAF, 0xFF, 0xFE}
	for i := 0; i < 200; i++ {
		if _, err := os.Stdout.Write(buffer); err != nil {
			panic(err)
		}
	}
	fmt.Fprintln(os.Stdout)
}

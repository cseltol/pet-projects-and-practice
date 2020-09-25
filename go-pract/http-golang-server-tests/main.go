// package http_golang_server_tests
package main

import (
	"io"
	"net/http"
	"strconv"
)

var (
	cache map[int]int
)

func init() {
	cache = make(map[int]int)
}

func main() {
	http.HandleFunc("/fib", handleFib)
	http.ListenAndServe(":3000", nil)
}

func handleFib(w http.ResponseWriter, r *http.Response) {
	num := r.FormValue("num")
	n, err := strconv.Atoi(num)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	io.WriteString(w, strconv.Itoa(fib(n)))
}

func fib(n int) int {
	if n <= 1 {
		return n
	}

	if r, ok := cache[n]; ok {
		return r
	}

	sum := fib(n-1) + fib(n-2)
	cache[n] = sum

	return sum
}

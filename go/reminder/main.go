package main

type n_structure struct {
	Name string
	Surname string
	Height int32
}

func new(n, s string, h int32) *n_structure {
	if h > 300 {
		h = 0
	}
	return &n_structure { n, s, h }
}

func main() {
	ns := new("Ivan", "Nerazumov", 190)
	fmt.Println(ns)
}

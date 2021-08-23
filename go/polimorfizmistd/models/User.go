package models

import (
	"fmt"
	"math/rand"
)

type User struct {
	ID        int64
	Firstname string
	Lastname  string
	salary    int
}

func NewUser(name string, surname string, salary int) *User {
	return &User{
		ID:        rand.Int63(),
		Firstname: name,
		Lastname:  surname,
		salary:    salary,
	}
}

func (u *User) GetSalary() {
	fmt.Println(u.salary + 2000)
}

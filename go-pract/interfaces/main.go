package main

import (
	"fmt"
)

const (
	ADMIN = "admin"
)

func main() {
	user := getUser()
	fmt.Printf("\n is Admin: %v\n", user.GetBalance())
}

type User struct {
	Name string
	Role string
}

type BankUser struct {
	Name    string
	Role    string
	Balance float64
}

type UserInterface interface {
	IsAdmin() bool
	GetBalance() float64
}

func (u *User) IsAdmin() bool {
	return u.Role == ADMIN
}

func (u *User) GetBalance() float64 {
	return 22.
}

func (u *BankUser) IsAdmin() bool {
	return u.Role == ADMIN
}

func (u *BankUser) GetBalance() float64 {
	return u.Balance
}

func getUser() UserInterface {
	// Возвращаем указатель когда работаем через интерфейсы
	return &BankUser{Role: ADMIN, Balance: 22.}
}

package main

import (
	"fmt"
	"os"
)

func main() {
	databaseURL := os.Getenv("DATABASE_URL")
	if databaseURL == "" {
		databaseURL = "host=localhost port=5433 dbname=go_rest_api_test sslmode=disable"
	}

	fmt.Println(databaseURL)
}

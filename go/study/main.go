package main

import (
	"encoding/json"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

type Request struct {
	UserName string `json:"username"`
	Password string `json:"password"`
}

func main() {
	router := mux.NewRouter()
	router.HandleFunc("/", Controller)
	log.Fatal(http.ListenAndServe(":8080", router))
}

func Controller(w http.ResponseWriter, r *http.Request) {
	req := Request{}
	err := json.NewDecoder(r.Body).Decode(&req)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		w.Write([]byte(`{"error":"` + err.Error() + `"}`))
		return
	}
}

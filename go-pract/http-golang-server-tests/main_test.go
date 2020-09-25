package main

import (
	"fmt"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestHandleFib(t *testing.T) {
	testCases := []struct {
		name string
		num  int
		want []byte
	}{
		{
			name: "firstTest",
			num:  1,
			want: []byte("0"),
		},
		{
			name: "secondTest",
			num:  3,
			want: []byte("2"),
		},
		{
			name: "thirdTest",
			num:  10,
			want: []byte("55"),
		},
	}

	handler := http.HandleFunc(handleFib)

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			rec := httptest.NewRecorder()
			req, _ := http.NewRequest("GET", fmt.Sprintf("/fib?num=%d", tc.num), nil)
			handler.ServeHTTP(rec, req)

			assert.Equal(t, tc.want, rec.Body.Bytes())
		})
	}
}

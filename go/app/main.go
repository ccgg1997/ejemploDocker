package main

import (
    "fmt"
    "net/http"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Holas Mundaaanoooooyto!")
    })
    http.ListenAndServe(":8080", nil)
}
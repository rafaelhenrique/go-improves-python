package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strings"
)

// #cgo pkg-config: python-3.6
// #define Py_LIMITED_API
// #include <Python.h>
import "C"

//export FindCnpjByRegex
func FindCnpjByRegex(content, company string) (cnpj string) {
	pattern := regexp.MustCompile(`\d{2}(\d{14}).*` + company + `.*`)
	result := pattern.FindStringSubmatch(content)

	if len(result) == 0 {
		return
	}

	return result[1]
}

//export FindCnpjByContains
func FindCnpjByContains(content, company string) (cnpj string) {
	splitedContent := strings.Split(content, "\n")

	lineNumber := 1
	for _, line := range splitedContent {
		if strings.Contains(line, company) {
			return line
		}
		lineNumber++
	}

	return
}

func main() {
	// Real data about CNPJ - too slow (~2min), too large and not versioned
	//
	// file, err := ioutil.ReadFile("./data/F.K03200UF.D71214SP")
	file, err := ioutil.ReadFile("./data/MINIMAL")
	if err != nil {
		fmt.Printf("Error to open file. Error: %v\n", err.Error())
	}
	content := string(file)

	cnpj := FindCnpjByRegex(content, "CARGOBR INTERMEDIACAO E AGENCIAMENTO DE NEGOCIOS S/A")
	fmt.Println("FindCnpjByRegex result: " + cnpj)

	cnpj = FindCnpjByContains(content, "CARGOBR INTERMEDIACAO E AGENCIAMENTO DE NEGOCIOS S/A")
	fmt.Println("FindCnpjByContains result: " + cnpj)
}

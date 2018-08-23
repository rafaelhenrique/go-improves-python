package main

import (
	"errors"
	"fmt"
	"io/ioutil"
	"regexp"
)

// #cgo pkg-config: python-3.6
// #define Py_LIMITED_API
// #include <Python.h>

//export FindCnpjByRegex
func FindCnpjByRegex(company string) (cnpj string, err error) {
	// Real data about CNPJ - too slow (~2min), too large and not versioned
	//
	// file, err := ioutil.ReadFile("./data/F.K03200UF.D71214SP")
	file, err := ioutil.ReadFile("./data/MINIMAL")
	if err != nil {
		return "", fmt.Errorf("findCnpjByRegex: error to open file. Error: %v", err.Error())
	}

	pattern := regexp.MustCompile(`\d{2}(\d{14}).*` + company + `.*`)
	content := string(file)
	result := pattern.FindStringSubmatch(content)

	if len(result) == 0 {
		return "", errors.New("findCnpjByRegex: company not found")
	}

	return result[1], nil
}

func main() {
	cnpj, err := FindCnpjByRegex("CARGOBR INTERMEDIACAO E AGENCIAMENTO DE NEGOCIOS S/A")

	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("CNPJ: " + cnpj)
	}
}

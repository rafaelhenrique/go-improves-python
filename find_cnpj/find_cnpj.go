package main

import (
	"errors"
	"fmt"
	"io/ioutil"
	"regexp"
	"strings"
)

// #cgo pkg-config: python-3.6
// #define Py_LIMITED_API
// #include <Python.h>

//export FindCnpjByRegex
func FindCnpjByRegex(content, company string) (cnpj string, err error) {
	pattern := regexp.MustCompile(`\d{2}(\d{14}).*` + company + `.*`)
	result := pattern.FindStringSubmatch(content)

	if len(result) == 0 {
		return "", errors.New("FindCnpjByRegex: company not found")
	}

	return result[1], nil
}

//export FindCnpjByContains
func FindCnpjByContains(content, company string) (cnpj string, err error) {
	splitedContent := strings.Split(content, "\n")

	lineNumber := 1
	for _, line := range splitedContent {
		if strings.Contains(line, company) {
			return line, nil
		}
		lineNumber++
	}

	return "", errors.New("FindCnpjByContains: company not found")
}

func main() {
	// Real data about CNPJ - too slow (~2min), too large and not versioned
	//
	// file, err := ioutil.ReadFile("./data/F.K03200UF.D71214SP")
	file, err := ioutil.ReadFile("./data/MINIMAL")
	if err != nil {
		fmt.Errorf("Error to open file. Error: %v", err.Error())
	}
	content := string(file)

	cnpj, err := FindCnpjByRegex(content, "CARGOBR INTERMEDIACAO E AGENCIAMENTO DE NEGOCIOS S/A")
	if err != nil {
		fmt.Errorf("FindCnpjByRegex error: %v", err.Error())
	} else {
		fmt.Println("FindCnpjByRegex result: " + cnpj)
	}

	cnpj, err = FindCnpjByContains(content, "CARGOBR INTERMEDIACAO E AGENCIAMENTO DE NEGOCIOS S/A")
	if err != nil {
		fmt.Errorf("FindCnpjByContains error: %v", err.Error())
	} else {
		fmt.Println("FindCnpjByContains result: " + cnpj)
	}
}

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

//export FindCnpjByContains
func FindCnpjByContains(company string) (cnpj string, err error) {
	// Real data about CNPJ - too slow (~2sec), too large and not versioned
	//
	// file, err := ioutil.ReadFile("./data/F.K03200UF.D71214SP")
	file, err := ioutil.ReadFile("./data/MINIMAL")
	if err != nil {
		return "", fmt.Errorf("FindCnpjByContains: error to open file. Error: %v", err.Error())
	}

	content := string(file)
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
	cnpj, err := FindCnpjByRegex("CARGOBR INTERMEDIACAO E AGENCIAMENTO DE NEGOCIOS S/A")
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("CNPJ: " + cnpj)
	}

	cnpj, err = FindCnpjByContains("CARGOBR INTERMEDIACAO E AGENCIAMENTO DE NEGOCIOS S/A")
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("CNPJ: " + cnpj)
	}
}

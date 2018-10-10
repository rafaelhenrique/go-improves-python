package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
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
func FindCnpjByContains(content, company string) (cnpj int) {
	splitedContent := strings.Split(content, "\n")

	for _, line := range splitedContent {
		if strings.Contains(line, company) {
			cnpj, _ = strconv.Atoi(line[2:16])
			return
		}
	}

	return
}

func main() {
	// Real data about CNPJ - too slow, too large and not versioned
	//
	// file, err := ioutil.ReadFile("./data/F.K03200UF.D71214PR")
	file, err := ioutil.ReadFile("./data/MINIMAL")
	if err != nil {
		fmt.Printf("Error to open file. Error: %v\n", err.Error())
	}
	content := string(file)

	strCnpj := FindCnpjByRegex(content, "OLIST SERVICOS DIGITAIS LTDA")
	fmt.Printf("FindCnpjByRegex result: %s\n", strCnpj)

	intCnpj := FindCnpjByContains(content, "OLIST SERVICOS DIGITAIS LTDA")
	fmt.Printf("FindCnpjByContains result: %d\n", intCnpj)
}

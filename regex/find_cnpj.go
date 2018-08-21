package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
)

func main() {
	// Real data about CNPJ - too slow, too large and not versioned
	//
	// file, err := ioutil.ReadFile("./data/F.K03200UF.D71214SP")
	file, err := ioutil.ReadFile("./data/MINIMAL")
	if err != nil {
		fmt.Println("[main] Error to open file. Error: ", err.Error())
	}

	pattern := regexp.MustCompile(`\d{2}(\d{14}).*CARGOBR INTERMEDIACAO E AGENCIAMENTO DE NEGOCIOS S/A.*`)
	content := string(file)
	result := pattern.FindStringSubmatch(content)

	if len(result) > 0 {
		fmt.Printf("CNPJ: %s\n", result[1])
	} else {
		fmt.Println("Not found!")
	}

}

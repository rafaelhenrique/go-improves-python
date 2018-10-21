package main

import (
	"fmt"
	"io/ioutil"
	"testing"
)

var testCases = []struct {
	input    string
	expected int
}{
	{"OLIST SERVICOS DIGITAIS LTDA", 18552346000168},
	{"AUTOLIST LTDA", 27742791000181},
	{"ENFERMAGEM SAUDE HOLISTICA LTDA.", 28326178000146},
}

func readFileContent(filename string) (content string) {
	// Real data about CNPJ - too slow, too large and not versioned
	//
	// file, err := ioutil.ReadFile("./data/F.K03200UF.D71214PR")
	file, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Printf("Error to open file. Error: %v\n", err.Error())
		return
	}
	return string(file)
}

func TestFindCnpjByRegex(t *testing.T) {
	content := readFileContent("./data/MINIMAL")

	for _, test := range testCases {
		if actual := FindCnpjByRegex(content, test.input); actual != test.expected {
			t.Errorf("FindCnpjByRegex(content, %s) = %d, expected %d.",
				test.input, actual, test.expected)
		}
	}
}

func TestFindCnpjByContains(t *testing.T) {
	content := readFileContent("./data/MINIMAL")

	for _, test := range testCases {
		if actual := FindCnpjByContains(content, test.input); actual != test.expected {
			t.Errorf("FindCnpjByContains(content, %s) = %d, expected %d.",
				test.input, actual, test.expected)
		}
	}
}

func BenchmarkFindCnpjByRegex(b *testing.B) {
	content := readFileContent("./data/MINIMAL")

	// bench combined time to run through all test cases
	for i := 0; i < b.N; i++ {
		for _, test := range testCases {
			FindCnpjByRegex(content, test.input)
		}
	}
}

func BenchmarkFindCnpjByContains(b *testing.B) {
	content := readFileContent("./data/MINIMAL")

	// bench combined time to run through all test cases
	for i := 0; i < b.N; i++ {
		for _, test := range testCases {
			FindCnpjByContains(content, test.input)
		}
	}
}

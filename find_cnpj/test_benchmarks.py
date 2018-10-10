from ctypes import Structure, c_char_p, c_longlong, cdll

from find import (
    find_cnpj_using_findall,
    find_cnpj_using_in,
    find_cnpj_using_search,
)


class GoString(Structure):
    _fields_ = [("p", c_char_p), ("n", c_longlong)]


gofindcnpj = cdll.LoadLibrary("./gofindcnpj.so")
gofindcnpj.FindCnpjByContains.argtypes = [GoString, GoString]
gofindcnpj.FindCnpjByContains.restype = c_longlong


#
# Benchmark tests
#

def test_function_find_cnpj_using_in_benchmark(benchmark, content, company_name):
    benchmark(find_cnpj_using_in, content, company_name)


def test_function_find_cnpj_using_search_benchmark(benchmark, content, company_name):
    benchmark(find_cnpj_using_search, content, company_name)


def test_function_find_cnpj_using_findall_benchmark(benchmark, content, company_name):
    benchmark(find_cnpj_using_findall, content, company_name)


def test_function_golang_ctypes_find_cnpj_contains_benchmark(benchmark, content, company_name):
    new_content = bytes(content, 'utf-8')
    new_company_name = bytes(company_name, 'utf-8')

    new_content = GoString(new_content, len(new_content))
    new_company_name = GoString(new_company_name, len(new_company_name))

    benchmark(gofindcnpj.FindCnpjByContains, new_content, new_company_name)

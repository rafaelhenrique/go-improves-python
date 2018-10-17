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

gofindcnpj.FindCnpjByRegex.argtypes = [GoString, GoString]
gofindcnpj.FindCnpjByRegex.restype = c_longlong


#
# Common tests
#

def test_function_find_cnpj_using_in_result(content, company_name):
    assert find_cnpj_using_in(content, company_name) == 18552346000168


def test_function_find_cnpj_using_search_result(content, company_name):
    assert find_cnpj_using_search(content, company_name) == '18552346000168'


def test_function_find_cnpj_using_findall_result(content, company_name):
    assert find_cnpj_using_findall(content, company_name) == '18552346000168'


def test_function_golang_ctypes_find_cnpj_contains_result(content, company_name):
    new_content = bytes(content, 'utf-8')
    new_company_name = bytes(company_name, 'utf-8')
    expected = 18552346000168

    result = gofindcnpj.FindCnpjByContains(
        GoString(new_content, len(new_content)),
        GoString(new_company_name, len(new_company_name)),
    )

    assert expected == result


def test_function_golang_ctypes_find_cnpj_regex_result(content, company_name):
    new_content = bytes(content, 'utf-8')
    new_company_name = bytes(company_name, 'utf-8')
    expected = 18552346000168

    result = gofindcnpj.FindCnpjByRegex(
        GoString(new_content, len(new_content)),
        GoString(new_company_name, len(new_company_name)),
    )

    assert expected == result

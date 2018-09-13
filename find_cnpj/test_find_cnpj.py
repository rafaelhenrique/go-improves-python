from ctypes import Structure, c_char_p, c_longlong, cdll

import pytest

from find_cnpj import (
    find_cnpj_using_findall,
    find_cnpj_using_in,
    find_cnpj_using_search,
)


class GoString(Structure):
    _fields_ = [("p", c_char_p), ("n", c_longlong)]


gofindcnpj = cdll.LoadLibrary("./gofindcnpj.so")
gofindcnpj.FindCnpjByContains.argtypes = [GoString, GoString]
gofindcnpj.FindCnpjByContains.restype = c_char_p


@pytest.fixture
def content():
    with open('./data/MINIMAL', 'r', encoding='iso8859') as fp:
        return fp.read()


@pytest.fixture
def company_name():
    return 'CARGOBR INTERMEDIACAO E AGENCIAMENTO DE NEGOCIOS S/A'


def test_find_cnpj_using_in(benchmark, content, company_name):
    benchmark(find_cnpj_using_in, content, company_name)


def test_find_cnpj_using_search(benchmark, content, company_name):
    benchmark(find_cnpj_using_search, content, company_name)


def test_find_cnpj_using_findall(benchmark, content, company_name):
    benchmark(find_cnpj_using_findall, content, company_name)


def test_find_cnpj_using_in_result(content, company_name):
    expected = '0117781400000184CARGOBR INTERMEDIACAO E AGENCIAMENTO DE NEGOCIOS S/A'
    assert expected in find_cnpj_using_in(content, company_name)


def test_find_cnpj_using_search_result(content, company_name):
    assert find_cnpj_using_search(content, company_name) == '17781400000184'


def test_find_cnpj_using_findall_result(content, company_name):
    assert find_cnpj_using_findall(content, company_name) == ['17781400000184']


def test_golang_ctypes_find_cnpj_contains(content, company_name):
    new_content = bytes(content, 'utf-8')
    new_company_name = bytes(company_name, 'utf-8')
    expected = b'0117781400000184CARGOBR INTERMEDIACAO E AGENCIAMENTO DE NEGOCIOS S/A'

    result = gofindcnpj.FindCnpjByContains(
        GoString(new_content, len(content)),
        GoString(new_company_name, len(company_name)),
    )

    assert expected in result

import pytest

from find_cnpj import (
    find_cnpj_using_findall,
    find_cnpj_using_in,
    find_cnpj_using_search,
)


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

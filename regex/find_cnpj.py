import re

# Real data about CNPJ - too slow, too large and not versioned
#
# with open('F.K03200UF.D71214SP', 'r', encoding='iso8859') as fp:
#     content = fp.read()

with open('./data/MINIMAL', 'r', encoding='iso8859') as fp:
    content = fp.read()


company_name = 'CARGOBR INTERMEDIACAO E AGENCIAMENTO DE NEGOCIOS S/A'
expression = r'\d{{2}}(\d{{14}}).*{}.*'.format(company_name)
pattern = re.compile(expression)


def find_cnpj_using_search(content, company_name):
    return re.search(expression, content).group(1)


def find_cnpj_using_findall(content, company_name):
    return pattern.findall(content)


def test_find_cnpj_using_search(benchmark):
    benchmark(find_cnpj_using_search, content, company_name)


def test_find_cnpj_using_findall(benchmark):
    benchmark(find_cnpj_using_findall, content, company_name)

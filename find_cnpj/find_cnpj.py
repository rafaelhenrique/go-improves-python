import re


def find_cnpj_using_in(content, company_name):
    return next(line for line in content.split('\n') if company_name in line)


def find_cnpj_using_search(content, company_name):
    expression = r'\d{{2}}(\d{{14}}).*{}.*'.format(company_name)
    return re.search(expression, content).group(1)


def find_cnpj_using_findall(content, company_name):
    expression = r'\d{{2}}(\d{{14}}).*{}.*'.format(company_name)
    pattern = re.compile(expression)
    return pattern.findall(content)


if __name__ == '__main__':
    # Real data about CNPJ - too slow, too large and not versioned
    #
    # with open('./data/F.K03200UF.D71214SP', 'r', encoding='iso8859') as fp:
    #     content = fp.read()

    with open('./data/MINIMAL', 'r', encoding='iso8859') as fp:
        content = fp.read()

    company_name = 'CARGOBR INTERMEDIACAO E AGENCIAMENTO DE NEGOCIOS S/A'

    print(find_cnpj_using_in(content, company_name))
    print(find_cnpj_using_search(content, company_name))
    print(find_cnpj_using_findall(content, company_name))

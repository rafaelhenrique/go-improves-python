import re


def find_cnpj_using_in(content, company_name):
    line = next(line for line in content.split('\n') if company_name in line)
    line = int(line[2:16])
    return line


def find_cnpj_using_search(content, company_name):
    expression = r'\d{{2}}(\d{{14}}).*{}.*'.format(company_name)
    return re.search(expression, content).group(1)


def find_cnpj_using_findall(content, company_name):
    expression = r'\d{{2}}(\d{{14}}).*{}.*'.format(company_name)
    pattern = re.compile(expression)
    return pattern.findall(content)[0]


if __name__ == '__main__':
    # Real data about CNPJ - too slow, too large and not versioned
    #
    # with open('./data/F.K03200UF.D71214PR', 'r', encoding='iso8859') as fp:
    #     content = fp.read()

    with open('./data/F.K03200UF.D71214PR', 'r', encoding='iso8859') as fp:
        content = fp.read()

    company_name = 'OLIST SERVICOS DIGITAIS LTDA'

    # print("find_cnpj_using_in result: ", find_cnpj_using_in(content, company_name))
    print("find_cnpj_using_search result: ", find_cnpj_using_search(content, company_name))
    # print("find_cnpj_using_findall result: ", find_cnpj_using_findall(content, company_name))

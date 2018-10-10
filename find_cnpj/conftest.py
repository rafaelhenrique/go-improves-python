import pytest


@pytest.fixture
def content():
    # Real data about CNPJ - too slow, too large and not versioned
    #
    # with open('./data/F.K03200UF.D71214PR', 'r', encoding='iso8859') as fp:
    #     content = fp.read()
    with open('./data/MINIMAL', 'r', encoding='iso8859') as fp:
        return fp.read()


@pytest.fixture
def company_name():
    return 'OLIST SERVICOS DIGITAIS LTDA'

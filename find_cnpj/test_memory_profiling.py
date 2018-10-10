from ctypes import Structure, c_char_p, c_longlong, cdll

from memory_profiler import profile

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
# Memory profiling tests
#

@profile
def profile_mem_find_cnpj_using_in(content, company_name):
    return find_cnpj_using_in(content, company_name)


@profile
def profile_mem_find_cnpj_using_search(content, company_name):
    return find_cnpj_using_search(content, company_name)


@profile
def profile_mem_find_cnpj_using_findall(content, company_name):
    return find_cnpj_using_findall(content, company_name)


@profile
def profile_mem_golang_ctypes_find_cnpj_contains(content, company_name):
    return gofindcnpj.FindCnpjByContains(
        GoString(new_content, len(new_content)),
        GoString(new_company_name, len(new_company_name)),
    )


if __name__ == '__main__':
    # Real data about CNPJ - too slow, too large and not versioned
    #
    # with open('./data/F.K03200UF.D71214PR', 'r', encoding='iso8859') as fp:
    #     content = fp.read()
    with open('./data/MINIMAL', 'r', encoding='iso8859') as fp:
        content = fp.read()

    company_name = 'OLIST SERVICOS DIGITAIS LTDA'

    new_content = bytes(content, 'utf-8')
    new_company_name = bytes(company_name, 'utf-8')

    profile_mem_find_cnpj_using_in(content, company_name)
    profile_mem_find_cnpj_using_search(content, company_name)
    profile_mem_find_cnpj_using_findall(content, company_name)
    profile_mem_golang_ctypes_find_cnpj_contains(new_content, new_company_name)

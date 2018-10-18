
![image](https://user-images.githubusercontent.com/1902333/47128770-0dd10000-d269-11e8-89f5-e7f85a4f89ed.png)

# Go improves Python?

This project is based on [this project](https://github.com/rochacbruno/rust-python-example) created by @rochacbruno. But this project uses [Golang](https://golang.org/) rather than [Rustlang](https://www.rust-lang.org).

This project has only one objective, which use Golang with Python as a possibility to have more performance on certain tasks.

# Comparisons between Python and Go

## find_cnpj

Locate CNPJ number based on company name.

- CNPJ data downloaded from this [link](http://idg.receita.fazenda.gov.br/orientacao/tributaria/cadastros/cadastro-nacional-de-pessoas-juridicas-cnpj/dados-abertos-do-cnpj).

## sum_numbers

Sum sequences (list, tuple, generator.. etc) of numbers.

# Run

Create your virtualenv directory:

- IMPORTANT RECOMENDATION: use your Python3.6 (native, without pyenv or similar) from O.S.

```
/usr/bin/python3.6 -m venv .venv
```

Activate your venv:

```
source .venv/bin/activate
```

Install requirements:

```
pip install -r requirements.txt
```

Enter on directory of project (find_cnpj or sum_numbers), and run benchmarks:

```
cd <directory of project>

# Recreate binary files
make build

# For unit tests
make test  

# For benchmark tests (time/operations)
make benchmark

# For memory profile
make profile-memory
```

# Tips and tricks

## Finding python version on pkg-config

```
$ pkg-config --list-all | grep python
python-3.6m               Python - Python library
python-2.7                Python - Python library
python                    Python - Python library
python-3.6                Python - Python library
python2                   Python - Python library
python3                   Python - Python library
notify-python             notify-python - Python bindings for libnotify
```

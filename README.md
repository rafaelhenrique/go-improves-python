# find_cnpj

This project is based on [this project](https://github.com/rochacbruno/rust-python-example) created by @rochacbruno. But this project uses [Golang](https://golang.org/) rather than [Rustlang](https://www.rust-lang.org).

THIS IS NOT A COMPETITION BETWEEN LANGUAGES! PLEASE THIS IS NOT A FLAME WAR! <3

This project has only one objective, which use Golang with Python as a possibility to have more performance on certain tasks.

# Data about CNPJ from Brazilian government

Data downloaded from this [link](http://idg.receita.fazenda.gov.br/orientacao/tributaria/cadastros/cadastro-nacional-de-pessoas-juridicas-cnpj/dados-abertos-do-cnpj).

# Run

Create your virtualenv directory:

```
python3 -m venv .venv
```

Activate your venv:

```
source .venv/bin/activate
```

Install requirements:

```
pip install requirements.txt
```

Run:

```
py.test -v -s run.py
```


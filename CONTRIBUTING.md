# Contributing

> Para ver o guia de contribuição em Português, [clique aqui](#guia-de-contribuicao).

## Contribution Guide

...

## Guia de contribuição

### TLDR

O projeto usa o [poetry](https://python-poetry.org/) como gerenciador de projeto.

```bash
poetry install
```

Você checar o [Guia de estilo](#guia-de-estilo) caso sua contribuição tenha código. O comandos existentes no ambiente podem ser encontrados [aqui](#taskrunner-taskipy).

Para checar se tudo está correto e os testes passam:

```bash
poetry run task test
```

---

Para iniciar a documentação:

```bash
poetry run task doc
```

---

Caso sua alteração seja visível a quem for usar a aplicação, adicione uma entrada ao changelog:

```bash
towncrier create
```

As configurações estão [aqui](#changelogs-com-towncrier).

---

Antes de enviar seu pull request, garanta que exista uma issue, se não houver uma, crie antes de submenter, o nome da branch deve conter o número da issue. [Caso precise de mais informações](#versionamento-e-git).

### Configuração do ambiente

Caso precise de ajuda para configurar e entender o ambiente de desenvolvimento desse projeto!

#### Gerenciamento de projeto

Esse projeto usa o [poetry](https://python-poetry.org/) (2.0.1) como gerenciador de projeto. Você pode instalar ele com [pipx](https://pipx.pypa.io/latest/).

Você pode instalar com:

```bash
pipx install poetry
```

No diretório você pode executar:

```bash
poetry install
```

para instalar todas as dependências do projeto e o pacote editável.


#### Ferramentas de desenvolvimento

Uma lista das ferramentas de desenvolvimento e suas configurações:

##### Taskrunner: [taskipy](https://github.com/taskipy/taskipy)

O taskipy facilita a execução dos comandos durante o momento de desenvolvimento do projeto:

```toml title="pyproject.toml" linenums="65"
--8<-- "pyproject.toml:65:75"
```

Você pode listar os comandos no CLI também:

```bash
$ poetry run task --list
format    ruff format
lint      ruff check
typos     typos videomaker_helper tests
types     mypy videomaker_helper
pre_test  task lint
test      pytest --cov=videomaker_helper/ -vv -x
stest     pytest
post_test coverage html
doc       mkdocs serve
```

Os comandos podem ser executados usando `task`. Por exemplo:

```bash
poetry run task test    # Executa os testes
poetry run task format  # Formata os arquivos
poetry run task typos   # Checa a grafia do código
...
```

##### Formatação e linter: [Ruff](https://docs.astral.sh/ruff/)

```toml title="pyproject.toml" linenums="52"
--8<-- "pyproject.toml:52:64"
```

As explicações das configurações podem ser encontradas no [Guia de estilo](#guia-de-estilo).

Basicamente para executar a checagem você deve executar:

```bash
poetry run task lint    # Checa o guia de estilo do projeto
poetry run task format  # Formata os arquivos
```


##### Checagem de tipos estáticos: [Mypy](https://mypy.readthedocs.io/)

```toml title="pyproject.toml" linenums="76"
--8<-- "pyproject.toml:76:78"
```

Para executar a checagem de tipos você pode executar:

```bash
poetry run task types
```

##### Checagem de erros de grafia no código: [Typos](https://pypi.org/project/typos/)

Para executar a checagem de erros de grafia você pode executar:

```bash
poetry run task typos
```

##### Changelogs com [towncrier](https://towncrier.readthedocs.io/en/stable/)

Essa ferramenta gera os fragmentos de alterações nos changelogs. Todas as alterações visíveis devem adicioanr um fragmento ao changelog.

As tags disponíveis são compatíveis com o padrão [Keep a changelook](https://keepachangelog.com/pt-BR/1.1.0/).

Para adicionar um novo fragmento:

```bash
towncrier create
```

Configuração:
```toml title="pyproject.toml" linenums="79"
--8<-- "pyproject.toml:79:117"
```

### Guia de estilo

Esse projeto segue os guias de estilo:

- [PEP 8](https://peps.python.org/pep-0008/) para código
- [PEP 257](https://peps.python.org/pep-0257/) para docstrings
- [Google Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) para o formato das docstrings
- [Keep a changelook](https://keepachangelog.com/pt-BR/1.1.0/) para changelogs

Para checar a conformidade do código você pode executar:

```bash
poetry run task lint
```


### Versionamento e git

Para enviar sua contribuição, não existe um formato pré-definido para mensagens, sinta-se a vontade.

- **Todos os PRs enviados devem ter uma issue**, caso você queira contribuir com algo que ainda não tem issue, abra uma issue antes.
- **As solicitações de PR devem ser enviadas para branch development**.
- O nome da branch **deve iniciar com o número da issue**
	 Algo como `42_texto`.
- Caso queira notificar que está inciando uma contribuição, abra um PR em "draft" marcando uma issue em específico:

	[Adicionar uma imagem aqui sobre como fazer esse processo]

	Ao finalizar as alterações você pode clicar em "Ready for review"

	[Adicionar uma imagem aqui sobre como fazer esse processo]

#### Changelogs

Após a alteração, caso ela seja **visível para quem usa aplicação** adicione uma entrada no changelog usando o `towncrier`:

```bash
towncrier create
```

### Integração contínua

Esse projeto usa o github actions como CI, se precisar executar todo o fluxo localmente você pode usar o [act](https://github.com/nektos/act):

```bash
act
```

A configuração do CI pode ser encontrada em [`.github/workflows/pipeline.yaml`](https://github.com/dunossauro/videomaker-helper/blob/main/.github/workflows/pipeline.yaml)

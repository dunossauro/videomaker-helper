# Contributing

> Para ver o guia de contribuição em Português, [clique aqui](#guia-de-contribuicao).

## Contribution Guide

### TLDR

This project uses [poetry](https://python-poetry.org/) as the project manager and [pre-commit](https://pre-commit.com/) to assurance some stuffs.

To install project:

```bash
poetry install
```

to activate pre-commit:

```bash
poetry run pre-commit install
```

If your contribution involves code, please refer to the [Style Guide](#style-guide). You can see all available commands in the environment [here](#taskrunner-taskipy).

To check if everything is correct and the tests pass:

```bash
poetry run task test
```

---

To start the documentation:

```bash
poetry run task doc
```

---

If your change is visible to the users of the application, add an entry to the changelog:

```bash
towncrier create
```

The configurations are [here](#changelogs-with-towncrier).

---

Before submitting your pull request, make sure there's an issue. If not, create one first. The branch name should contain the issue number. [For more information](#versioning-and-git).

### Environment Setup

If you need help setting up the development environment for this project, follow the instructions below.

#### Project Management

This project uses [poetry](https://python-poetry.org/) (2.0.1) as the project manager. You can install it using [pipx](https://pipx.pypa.io/latest/).

You can install it with:

```bash
pipx install poetry
```

In the project directory, run:

```bash
poetry install
```

This will install all project dependencies and the editable package.


#### Development Tools

A list of development tools and their configurations:

##### Taskrunner: [taskipy](https://github.com/taskipy/taskipy)

Taskipy makes it easier to run commands during the development process of the project:

```toml title="pyproject.toml" linenums="65"
--8<-- "pyproject.toml:65:75"
```

You can use `poetry run task --list` to see all available commands:

```bash
$ poetry run task --list
format    ruff format
lint      ruff check
typos     typos videomaker_helper tests
types     mypy videomaker_helper
pre_test  task lint
test      pytest --cov=videomaker_helper/ -vv -x
post_test coverage html
doc       mkdocs serve
```

Below are some of the most common commands you can use:

```bash
poetry run task test    # Run the automated tests
poetry run task format  # Format the code
poetry run task typos   # Check the spelling in the code
...
```

##### Formatting and Linter: [Ruff](https://docs.astral.sh/ruff/)

```toml title="pyproject.toml" linenums="52"
--8<-- "pyproject.toml:52:64"
```

For more details on style configuration, refer to the [Style Guide](#style-guide).

To check for compliance, run:

```bash
poetry run task lint    # Check the project's style guide
poetry run task format  # Format the files
```


##### Static Type Checking: [Mypy](https://mypy.readthedocs.io/)

```toml title="pyproject.toml" linenums="76"
--8<-- "pyproject.toml:76:78"
```

To run type checks, execute:

```bash
poetry run task types
```

##### Spelling Check in Code: [Typos](https://pypi.org/project/typos/)

To run the spelling check, execute:

```bash
poetry run task typos
```

##### Changelogs with [towncrier](https://towncrier.readthedocs.io/en/stable/)

All visible changes should add a fragment to the changelog.

The tags used follow the [Keep a Changelog](https://keepachangelog.com/1.1.0/) standard.

To add a new fragment:

```bash
towncrier create
```

Configuration:
```toml title="pyproject.toml" linenums="79"
--8<-- "pyproject.toml:79:117"
```

### Style Guide

This project follows the style guides:

- [PEP 8](https://peps.python.org/pep-0008/) for code
- [PEP 257](https://peps.python.org/pep-0257/) for docstrings
- [Google Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) for docstring formatting
- [Keep a Changelog](https://keepachangelog.com/1.1.0/) for changelogs

To check code style, run:

```bash
poetry run task lint
```


### Versioning and Git

There is no predefined format for commit messages. Feel free to choose a style that makes sense. Here are a few things to keep in mind:

- **All PRs must have an issue**. If you want to contribute something that doesn’t have an issue yet, create one before submitting.
- **PRs must be submitted to the `development` branch**.
- The branch name **must start with the issue number**:
    - For example, if the issue number is 42, the branch name would be `42_short-description`, where 'short-description' is a brief summary of the change.
- To notify others you're starting a contribution and allow them to track progress, open a draft PR and link the relevant issue.:
    - Once the changes are ready, you can mark the PR as "Ready for review."

#### Changelogs

All visible changes to the users of the application should be documented in the changelog. This helps maintain a clear history of changes and ensures users are aware of updates.

After making a change, if it is **visible to the application's users**, add an entry to the changelog using `towncrier`:

```bash
towncrier create
```

### Continuous Integration

This project uses GitHub Actions for Continuous Integration (CI). If you need to run the entire process locally, you can use [act](https://github.com/nektos/act):

```bash
act
```

> `act` is a tool that emulates GitHub Actions workflows locally, allowing you to run tests and CI processes without needing to push to the repository.

The full CI configuration can be found in [`.github/workflows/pipeline.yaml`](https://github.com/dunossauro/videomaker-helper/blob/main/.github/workflows/pipeline.yaml)


## Guia de contribuição

### TLDR

O projeto usa o [poetry](https://python-poetry.org/) como gerenciador de projeto e [pre-commit](https://pre-commit.com/) para assegurar algumas coisas.

Para instalar o poetry:

```bash
poetry install
```

Para ativar o pre-commit:

```bash
poetry run pre-commit install
```

Se sua contribuição envolver código, consulte o [Guia de estilo](#guia-de-estilo). Você pode ver todos os commandos disponíveis no ambiente [aqui](#taskrunner-taskipy).

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

Antes de enviar seu pull request, garanta que exista uma issue, se não houver uma, crie antes de submeter, o nome da branch deve conter o número da issue. [Caso precise de mais informações](#versionamento-e-git).

### Configuração do ambiente

Se você precisar de ajuda para configurar o ambiente de desenvolvimento deste projeto, siga as instruções abaixo.

#### Gerenciamento de projeto

Esse projeto usa o [poetry](https://python-poetry.org/) (2.0.1) como gerenciador de projeto. Você pode instalar ele com [pipx](https://pipx.pypa.io/latest/).

Você pode instalar com:

```bash
pipx install poetry
```

No diretório do projeto, execute:

```bash
poetry install
```

para instalar todas as dependências do projeto e o pacote editável.


#### Ferramentas de desenvolvimento

Uma lista das ferramentas de desenvolvimento e suas configurações:

##### Taskrunner: [taskipy](https://github.com/taskipy/taskipy)

O taskipy facilita a execução dos commandos durante o memento de desenvolvimento do projeto:

```toml title="pyproject.toml" linenums="65"
--8<-- "pyproject.toml:65:75"
```

Você pode usar poetry run task --list para ver todos os commandos disponíveis:

```bash
$ poetry run task --list
format    ruff format
lint      ruff check
typos     typos videomaker_helper tests
types     mypy videomaker_helper
pre_test  task lint
test      pytest --cov=videomaker_helper/ -vv -x
post_test coverage html
doc       mkdocs serve
```

Abaixo estão alguns dos commandos mais comuns que você pode utilizar:

```bash
poetry run task test    # Executa os testes automatizados
poetry run task format  # Executa a formatação do código
poetry run task typos   # Checa a grafia do código
...
```

##### Formatação e linter: [Ruff](https://docs.astral.sh/ruff/)

```toml title="pyproject.toml" linenums="52"
--8<-- "pyproject.toml:52:64"
```

Para mais detalhes sobre a configuração do estilo, consulte o [Guia de estilo](#guia-de-estilo).

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

##### Checagem de errors de grafia no código: [Typos](https://pypi.org/project/typos/)

Para executar a checagem de errors de grafia você pode executar:

```bash
poetry run task typos
```

##### Changelogs com [towncrier](https://towncrier.readthedocs.io/en/stable/)

Todas as alterações visíveis devem adicionar um fragmento ao changelog.

As tags usadas seguem o padrão [Keep a changelook](https://keepachangelog.com/pt-BR/1.1.0/).

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

Para enviar sua contribuição, não há um formato pré-definido para as mensagens de commit. Sinta-se à vontade para escolher um estilo que faça sentido. Somente alguns pontos para atenção:

- **Todos os PRs enviados devem ter uma issue**, caso você queira contribuir com algo que ainda não tem issue, abra uma issue antes.
- **As solicitações de PR devem set enviadas para branch development**.
- O nome da branch **deve iniciar com o número da issue**
    - Por exemplo, se a issue for número 42, o nome da branch seria `42_texto`, onde 'texto' é uma descrição curta da mudança.
- Para notificar que você está começando uma contribuição e permitir que outros saibam, abra um PR como 'draft' e vincule a issue relevante:
    - Ao finalizar as alterações você pode clicar em "Ready for review"

#### Changelogs

Todas as alterações visíveis para os usuários da aplicação devem set documentadas no changelog. Isso ajuda a manter um histórico claro das mudanças feitas e garante que os usuários estejam cientes das atualizações.

Após a alteração, caso ela seja **visível para quem usa aplicação** adicione uma entrada no changelog usando o `towncrier`:

```bash
towncrier create
```

### Integração contínua

Este projeto utilize o GitHub Actions para realizar a Integração Contínua (CI). Se precisar executar todo o fluxo localmente você pode usar o [act](https://github.com/nektos/act):

```bash
act
```

> O act é uma ferramenta que emula os workflows do GitHub Actions localmente, permitindo que você execute testes e processors de integração contínua sem precisar fazer push para o repositório.

A configuração completa do CI pode set encontrada em [`.github/workflows/pipeline.yaml`](https://github.com/dunossauro/videomaker-helper/blob/main/.github/workflows/pipeline.yaml)

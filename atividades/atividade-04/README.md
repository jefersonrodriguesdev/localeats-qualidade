# Relatório e Documentação da Atividade 4 - Qualidade de Software

* **Aluno:** Jeferson Rodrigues
* **Curso:** Análise e Desenvolvimento de Sistemas (SENAC RS)
* **Atividade:** Automação de Testes Unitários (TDD com Pytest) e Funcionais (Playwright com Page Object Model - POM) no sistema LocalEats.

---

## 1. Estrutura de Pastas do Projeto

A estrutura de diretórios foi organizada seguindo as boas práticas de separação entre código de negócio (`src/`), páginas de automação (`pages/`) e suítes de testes (`tests/`):

```text
atividade-04/
├── .venv/
├── pages/
│   ├── __init__.py
│   └── base_page.py
├── src/
│   ├── __init__.py
│   └── regras_localeats.py
├── tests/
│   ├── __init__.py
│   ├── test_localeats.py
│   └── test_regras_localeats.py
├── .gitignore
├── README.md
├── requirements.txt
├── relatorio-pytest.txt
└── evidencia_pesquisa.png
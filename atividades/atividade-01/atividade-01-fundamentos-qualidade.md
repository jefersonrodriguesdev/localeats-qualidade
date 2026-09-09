# Atividade 1: Fundamentos e Características da Qualidade no LocalEats

## 1. Identificação

**Turma:** Qualidade de Software 
**Equipe:** Individual  
**Data:** 08/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Jeferson Strzelecki Rodrigues | [@jefersonrodriguesdev] |

**Elemento de Competência:** Compreender os fundamentos de qualidade de software e sua aplicação no desenvolvimento de sistemas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Fundamentos da qualidade

### 2.1 Necessidades explícitas e implícitas

| Tipo | Necessidade | Interessado | Consequência se não for atendida |
|---|---|---|---|
| Explícita | Criar conta | Usuário | O usuário não conseguirá acessar o sistema sem antes criar uma conta. |
| Explícita | Nome | Usuário | O usuário não conseguirá criar uma conta sem inserir seu nome. |
| Implícita | Segurança da Senha | Usuário | O sistema permitirá o cadastro de senhas fáceis (sequencial por exemplo), deixando a conta vulnerável. |
| Implícita | Validação do e-mail | Empresa | O sistema permitirá o uso de contas de e-mail que não existem. |

### 2.2 Questão sobre os fundamentos da qualidade

**Um sistema que implementa todas as funcionalidades explicitamente solicitadas pode, ainda assim, apresentar baixa qualidade? Justifiquem utilizando pelo menos uma necessidade implícita identificada pela equipe.**

Sim, é perfeitamente possível que um sistema que implementa todas as suas funcionalidades explicitamente tenha uma baixa qualidade, pois o conceito de qualidade aborda diversos fatores como velocidade, fluidez, segurança e usabilidade. No exemplo que menciono de necessidade implícita, o usuário precisa inserir um e-mail válido, mas se não houver um aviso claro, ele pode ficar meio perdido, sem saber o porquê da recusa do e-mail inserido.

---

## 3. Tarefa 2: Exploração da aplicação

| Integrante | Funcionalidade | O que foi realizado | O que foi observado | Evidência |
|---|---|---|---|---|
| Jeferson | Criar conta | Foram inseridos nome, e-mail e senha nos respectivos campos e após foi clicado no botão Registrar. | Ao preencher todos os campos e clicar em Registrar, uma nova conta foi criada com sucesso. | [ver evidência](evidencias/jeferson-criar-conta.png) |

---

## 4. Tarefa 3: Requisitos e características de qualidade

| Integrante | Requisito de Qualidade | Característica ou subcaracterística | Justificativa | Como avaliar |
|---|---|---|---|---|
| Jeferson | Ao criar a conta, a senha cadastrada deve conter números e letras. | Segurança | Uma senha forte aumenta a segurança, evitando uma invasão da conta. | O sistema verifica se a senha segue o padrão estabelecido. Caso negativo, mostra um aviso ao usuário e bloqueia a criação da conta até que a senha seja corrigida. |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Gemini

**Como foi utilizada:**  
O Gemini foi utilizado para ajudar a corrigir e verificar se os campos foram preenchidos corretamente, ajudando a seguir o padrão de qualidade e também para correção ortográfica de algumas frases.

**Como as respostas foram verificadas:**  
Usei prints das respostas para que a ferramenta pudesse validar.

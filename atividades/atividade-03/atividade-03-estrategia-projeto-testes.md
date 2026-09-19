# Atividade 3: Estratégia e Projeto de Testes do LocalEats

## 1. Identificação

**Turma:** [Substitua pela sua Turma]
**Equipe:** Individual
**Data:** 19/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Jeferson Strzelecki Rodrigues | [@seu-usuario-github] |

**Elemento de Competência:** Planejar e projetar testes selecionando técnicas adequadas.

---

## 2. Tarefa 1: Planejamento dos testes

### 1.1 Objetivo dos testes
Verificar se o usuário, após fazer seu cadastro de conta, consegue acessar a plataforma, utilizando seus dados cadastrados, de forma fluída e sem apresentação de erros, e se o sistema impede acessos indevidos.

### 1.2 Escopo

| Integrante | Funcionalidade incluída | O que será verificado |
|---|---|---|
| Jeferson | Entrar no sistema | Acesso com credenciais válidas e bloqueio em caso de credenciais inválidas ou em branco. |

| Funcionalidade não incluída | Justificativa |
|---|---|
| Favoritar/desfavoritar restaurantes | O grau de relevância desta funcionalidade não impacta na experiência geral, não impede que o usuário consiga acessar, navegar na plataforma ou fazer um pedido. O foco do escopo é o fluxo de acesso (login). |

### 1.3 Abordagem

| Item | Decisão da equipe | Justificativa |
|---|---|---|
| Níveis de teste | Sistema | O fluxo será analisado pela interface, verificando a funcionalidade como um todo do início ao fim. |
| Tipos de teste | Funcional | O objetivo é verificar as regras de negócio de autenticação e acesso (login). |
| Perspectiva | Caixa-preta | Serão consideradas as entradas na interface e os resultados na tela, sem acesso ou validação direta no código-fonte. |
| Técnicas de teste | Tabela de decisão | O resultado esperado para o acesso depende diretamente da combinação de condições (e-mail correto/incorreto e senha correta/incorreta/vazia). |

### 1.4 Ambiente e responsabilidades

| Item | Definição |
|---|---|
| Ambiente necessário | Aplicação LocalEats acessível via navegador (Chrome/Edge), conexão à internet estável e banco de dados de testes disponível. |
| Responsáveis pelo planejamento | Jeferson |
| Responsáveis pela especificação dos casos | Jeferson |
| Responsáveis pela futura execução | Jeferson (ou equipe de QA) |

### 1.5 Critérios

| Critério | Definição da equipe |
|---|---|
| Entrada | Eu preciso ter uma conta criada e ativa na plataforma, e o site precisar estar no ar. |
| Saída | Todos os 3 casos de teste planejados devem estar devidamente executados e os resultados registrados. |
| Suspensão | Os campos não aceitarem entrada de dados ou o banco de dados estar inacessível para confirmar as informações inseridas. |

---

## 3. Tarefa 2: Riscos e técnicas de teste

### 2.1 Análise dos riscos

| ID | Integrante | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
|---|---|---|---|---|---|---|---|---|
| R01 | Jeferson | Entrar no sistema | O sistema não bloquear a tentativa de acesso após a inserção de senha incorreta por mais de 3 vezes. | Aumento do risco de invasão da conta através de ataques de força bruta, expondo os dados do cliente. | Média | Alto | Alta | A ausência de um limite de tentativas compromete a segurança básica da autenticação da conta. |
| R02 | Jeferson | Entrar no sistema | O sistema permitir a submissão do formulário de login com o campo de senha em branco. | Abertura de uma falha crítica que permite a qualquer pessoa acessar à conta possuindo apenas o e-mail do usuário. | Baixa | Alto | Alta | A falta de validação de campos obrigatórios quebra totalmente o princípio de segurança e integridade da conta do usuário. |

### 2.2 Aplicação da técnica

**Integrante responsável:** Jeferson
**Funcionalidade:** Entrar no sistema
**Riscos relacionados:** R01 e R02
**Técnica escolhida:** Tabela de decisão

**Por que a técnica foi escolhida?**
A funcionalidade de login depende estritamente da combinação de duas variáveis (e-mail e senha). O sistema deve tomar decisões diferentes com base na validade de ambas as informações simultaneamente, tornando a tabela de decisão o método ideal para garantir a cobertura das regras.

**Aplicação da técnica**

| Regra | E-mail é válido e cadastrado? | Senha está correta? | Resultado esperado |
|---|---|---|---|
| 1 | Sim | Sim | Acesso concedido ao dashboard. |
| 2 | Sim | Não (3ª tentativa) | Aviso de "Dados Inválidos" e contagem de tentativas. |
| 3 | Sim | Não (4ª tentativa) | Aviso de conta bloqueada e indicação para recuperar a senha. |
| 4 | Sim | Em branco (Vazio) | Erro, campo senha é obrigatório. |

**Casos derivados**
CT01, CT02 e CT03.

---

## 4. Tarefa 3: Casos de teste e rastreabilidade

### 3.1 Especificação dos casos de teste

**CT01: Entrada no sistema com credenciais válidas**
*   **Integrante responsável:** Jeferson
*   **Funcionalidade:** Entrar no sistema
*   **Risco relacionado:** [Caminho Feliz - Sem risco mapeado]
*   **Técnica utilizada:** Tabela de decisão
*   **Pré-condição:** O usuário já tem uma conta cadastrada e ativa na plataforma.
*   **Dados de entrada:** E-mail: teste123@teste.com / Senha: Senhateste123
*   **Passos:**
    1. Inserir e-mail válido no campo e-mail.
    2. Inserir senha válida cadastrada no campo senha.
    3. Clicar no botão Entrar.
*   **Resultado esperado:** É esperado que o login de entrada seja efetivado com sucesso e que o usuário tenha acesso ao dashboard inicial da aplicação.

**CT02: Bloqueio de acesso ao usuário após 3 tentativas inválidas**
*   **Integrante responsável:** Jeferson
*   **Funcionalidade:** Entrar no sistema
*   **Risco relacionado:** R01
*   **Técnica utilizada:** Tabela de decisão
*   **Pré-condição:** O usuário já tem uma conta cadastrada e ativa na plataforma com e-mail e senha válidos.
*   **Dados de entrada:** E-mail válido e no mínimo 4 senhas incorretas.
*   **Passos:**
    1. Inserir o e-mail válido no campo e-mail.
    2. Inserir uma senha diferente da cadastrada (repetir 4x).
    3. Clicar no botão Entrar.
*   **Resultado esperado:** Nas primeiras 3 inserções de senha errada, espera-se que o sistema dê um aviso de "Dados Inválidos" e mostre quantas tentativas restam. Ao inserir errado na 4ª vez, surge um aviso de conta bloqueada e indica a necessidade de recuperar a senha.

**CT03: Impedir acesso com campo de senha em branco**
*   **Integrante responsável:** Jeferson
*   **Funcionalidade:** Entrar no sistema
*   **Risco relacionado:** R02
*   **Técnica utilizada:** Tabela de decisão
*   **Pré-condição:** O usuário deve ter e-mail e senha válidos cadastrados e a aplicação deve estar no ar.
*   **Dados de entrada:** E-mail válido e campo de senha vazio.
*   **Passos:**
    1. Inserir um e-mail válido.
    2. Deixar o campo de senha em branco.
    3. Clicar no botão Entrar.
*   **Resultado esperado:** O sistema não realiza o login e exibe um alerta informando que o campo de senha é obrigatório.

### 3.2 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
|---|---|---|---|---|
| Jeferson | Entrar no sistema | Requisito: Acesso válido | Tabela de decisão | CT01 |
| Jeferson | Entrar no sistema | R01: Falta de bloqueio após erros contínuos | Tabela de decisão | CT02 |
| Jeferson | Entrar no sistema | R02: Acesso com senha em branco | Tabela de decisão | CT03 |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**
Gemini

**Como foi utilizada:**
Apoio na estruturação lógica do planejamento, validação criteriosa dos riscos sob a ótica de segurança de software, elaboração da tabela de decisão e revisão da escrita dos casos de teste.

**Uma sugestão que precisou ser alterada ou rejeitada:**
Durante a análise do Risco 02 na construção do CT03, propus inicialmente o teste de um formato de e-mail inválido (sem o "@"). Embora útil, isso testaria uma máscara de front-end (validação de caractere) e não o Risco R02 que havíamos documentado sobre a gravidade da submissão com a *senha em branco*. A sugestão foi alterada e o caso de teste CT03 foi redirecionado para testar o envio do formulário sem o preenchimento da senha, garantindo a rastreabilidade exata com o Risco 02.

**Como as respostas foram verificadas:**
As respostas foram desenvolvidas etapa por etapa, revisando os conceitos teóricos de Qualidade de Software (riscos, técnicas caixa-preta, e critérios) e ajustando a escrita técnica para estar em conformidade com o formato IEEE de plano de testes abordado no curso.

# Atividade 2: Organização da Qualidade no LocalEats

## 1. Identificação

**Turma:** Qualidade de Software
**Equipe:** Individual
**Data:** 17/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Jeferson Strzelecki Rodrigues | [@jefersonrodriguesdev] |

**Elemento de Competência:** Identificar papéis, responsabilidades e competências relacionadas às atividades de qualidade e testes.

---

## 2. Tarefa 1: Diagnóstico da situação

### 2.1 Problemas organizacionais

| Problema identificado | Possível consequência para o produto ou para a equipe |
|---|---|
| Funcionalidades chegam aos usuários com defeitos. | Isso pode causar perda de vendas, pois a funcionalidade pagamento por exemplo, pode não estar funcionando. |
| Os critérios para considerar uma funcionalidade pronta não estão claros. | Isso pode atrasar o desenvolvimento, pois o testador não saberá o que testar ou se todas as funcionalidades foram cumpridas. |
| Não está claro quem pode aprovar a disponibilização de uma nova versão. | Sem esta clareza, a nova versão pode atrasar ou mesmo nem ser disponibilizada, pois não tem alguém responsável pela aprovação, isso impactaria nas funcionalidades e por consequência no funcionamento do sistema. |

### 2.2 Questão sobre a responsabilidade da qualidade

**A qualidade do LocalEats deve ser responsabilidade exclusiva do profissional de QA? Justifiquem.**

Acho que a responsabilidade da qualidade do LocalEats deve ser de todos: de quem modela, de quem desenvolve e de quem testa. Além do QA, todos devem estar envolvidos num objetivo comum, atuando como um pacto coletivo. Só assim a verdadeira qualidade é alcançada, quando todos estão focados na melhor entrega, sendo o QA mais um facilitador ou catalisador dessa qualidade no processo.

---

## 3. Tarefa 2: Papéis e competências

| Integrante | Papel analisado | Responsabilidades relacionadas à qualidade | Competências técnicas | Competências comportamentais |
|---|---|---|---|---|
| Jeferson | Product Owner (PO) | Atuar como os "olhos do cliente" junto ao time, garantir que o escopo seja seguido, orientar e conferir continuamente as entregas. | Conhecimento do produto e negócio, mapeamento de requisitos, definição de critérios de aceitação e gestão do escopo/backlog. | Excelente comunicação com time e cliente, foco em alinhar expectativas, visão estratégica e empatia. |

---

## 4. Tarefa 3: Matriz de responsabilidades (RACI)

| Atividade de qualidade | Product Owner | Desenvolvedor | QA |
|---|:---:|:---:|:---:|
| Definir critérios de aceitação | R/A | C | C |
| Revisar requisitos | A | R | R |
| Implementar a funcionalidade | I | R/A | I |
| Revisar o código | - | R/A | - |
| Criar testes unitários | - | R/A | C |
| Planejar e executar testes do sistema | I | I | R/A |
| Registrar e acompanhar defeitos | I | C | R/A |
| Priorizar a correção dos defeitos | R/A | I | C |
| Aprovar a disponibilização da versão | A | C | C |

*(Legenda: R = Responsável, A = Aprovador, C = Consultado, I = Informado, - = Não aplicável)*

### 4.1 Lacuna ou conflito encontrado

**Atividade:** Revisar o código.
**Problema:** O risco é alto quando a mesma pessoa (Desenvolvedor como R e A exclusivo) cria e revisa o próprio trabalho, pois detalhes ou erros podem passar despercebidos. O mais indicado seria que outro desenvolvedor (peer review) ou QA, com um olhar diferente, revisasse a funcionalidade para aprovar.

### 4.2 Práticas recomendadas

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos |
|---|---|---|
| Reunião "Three Amigos" (Três Amigos) | Falta de clareza nos critérios para considerar uma funcionalidade pronta e alinhamento pré-desenvolvimento. | PO, Desenvolvedor e QA |
| Testes Automatizados em CI/CD | Funcionalidades chegando aos usuários com defeitos e gargalos de aprovação manual. | Desenvolvedor e QA |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**
Gemini

**Como foi utilizada:**
Apoio na estruturação das ideias, validação teórica da matriz RACI segundo as práticas ágeis e formatação do arquivo Markdown final.

**Como as respostas foram verificadas:**
Revisão iterativa e verificação guiada passo a passo baseada nos materiais das aulas sobre Papéis e Qualidade, validando as opções sugeridas antes da construção do documento.

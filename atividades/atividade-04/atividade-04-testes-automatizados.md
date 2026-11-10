# Atividade 4: Testes Automatizados do LocalEats

## 1. Identificação das responsabilidades

| ID   | Integrante          | Tipo      | Comportamento verificado          | Arquivo e função                                           |
|------|---------------------|-----------|-----------------------------------|------------------------------------------------------------|
| TU01 | Jeferson Rodrigues  | Unitário  | Valor mínimo atingido com sucesso | tests/test_regras_localeats.py::test_pedido_atinge_valor_minimo_com_sucesso |
| TU02 | Jeferson Rodrigues  | Unitário  | Valor recusado abaixo do mínimo   | tests/test_regras_localeats.py::test_pedido_recusado_abaixo_do_minimo |
| TU03 | Jeferson Rodrigues  | Unitário  | Rejeita valor negativo (Exceção)  | tests/test_regras_localeats.py::test_rejeita_valor_negativo_com_excecao |
| TF01 | Jeferson Rodrigues  | Funcional | Pesquisa por localização (POM)    | tests/test_localeats.py::test_pesquisar_restaurante_por_localizacao |

## 2. Aplicação simplificada do TDD

**TDD de Jeferson Rodrigues**
- **Regra escolhida:** Regra 1 - Verificar valor mínimo do pedido (R$ 30,00).
- **Primeiro teste escrito:** `test_pedido_atinge_valor_minimo_com_sucesso` (passando o valor 30.00).
- **Por que o teste falhou inicialmente (Red):** A função `pedido_atingiu_valor_minimo` ainda não existia no arquivo `regras_localeats.py`, gerando um erro de importação e de comportamento não implementado.
- **Implementação mínima realizada (Green):** Foi criada a função recebendo a variável `valor_pedido` e retornando `True` se o valor fosse maior ou igual a 30.00, e `False` caso contrário.
- **Segundo teste escrito:** `test_pedido_recusado_abaixo_do_minimo` (passando o valor 29.99, validando o limite).
- **Melhoria ou refatoração realizada (Refactor):** Foi adicionado um terceiro teste de borda para valores negativos, refatorando a função principal para incluir a validação `if valor_pedido < 0: raise ValueError(...)`.

## 3. Explicação individual de um teste

**Teste:** `TF01 - test_pesquisar_restaurante_por_localizacao`
Este teste funcional automatiza o fluxo de filtragem de restaurantes por região no sistema. Utilizei o conceito de *Page Object Model (POM)* criando a classe `LocalEatsHomePage` para separar a lógica de interação com os elementos da interface da lógica de negócios do teste. O script acessa a URL base, realiza o login automatizado com credenciais válidas, utiliza os métodos encapsulados para preencher o campo de busca com o termo **"Centro"** e aciona o clique do botão de busca. Como assertion de segurança, o teste valida se o elemento correspondente ao **"Restaurante Sabor 7"** fica visível na tela e, ao final, captura uma evidência visual automática (`.screenshot()`) documentando a execução aprovada.

## 4. Diferenciais aplicados (Busca pelo Conceito A)
- Criação de um terceiro teste unitário validando regra de negócio extra e tratamento de exceções.
- Utilização de `pytest.raises` para capturar exceções `ValueError` em valores negativos.
- Estruturação do teste funcional utilizando *Page Object Model (POM)* com encapsulamento rigoroso de seletores e rotina de login.
- Adição de comando `.screenshot()` no teste Playwright para capturar evidência visual automática em `evidencia_pesquisa.png`.

## 5. Uso de inteligência artificial

- **Ferramenta utilizada:** Gemini.
- **Como a ferramenta foi utilizada:** Apoio para estruturar as chamadas corretas do pytest-playwright aplicando o padrão Page Object Model e revisão da sintaxe dos locators CSS.
- **Uma sugestão que precisou ser alterada ou rejeitada:** O modelo sugeriu usar locators muito acoplados à estrutura DOM rígida. Ajustei para utilizar métodos mais resilientes como `page.get_by_placeholder`, `page.get_by_role` e tratamento de modo estrito de elementos.
- **Como o código sugerido foi verificado:** Todos os scripts foram executados e validados na máquina local, garantindo 100% de sucesso nos testes (`1 passed`).
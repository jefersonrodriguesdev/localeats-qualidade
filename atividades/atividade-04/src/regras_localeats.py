def pedido_atingiu_valor_minimo(valor_pedido):
    if valor_pedido < 0:
        raise ValueError("O valor não pode ser negativo!")
    
    if valor_pedido >= 30.00:
        return True
        
    return False
```[cite: 14]

### `tests/test_regras_localeats.py`
```python
import pytest
from src.regras_localeats import pedido_atingiu_valor_minimo

# Responsável: Jeferson Rodrigues
def test_pedido_atinge_valor_minimo_com_sucesso():
    # Arrange
    valor = 30.00
    # Act
    resultado = pedido_atingiu_valor_minimo(valor)
    # Assert
    assert resultado is True

# Responsável: Jeferson Rodrigues
def test_pedido_recusado_abaixo_do_minimo():
    # Arrange
    valor = 29.99
    # Act
    resultado = pedido_atingiu_valor_minimo(valor)
    # Assert
    assert resultado is False

# Responsável: Jeferson Rodrigues
def test_rejeita_valor_negativo_com_excecao():
    # Arrange
    valor_invalido = -5.00
    # Act & Assert
    with pytest.raises(ValueError, match="O valor não pode ser negativo!"):
        pedido_atingiu_valor_minimo(valor_invalido)
```[cite: 15]

---

## 3. Automação Funcional (Playwright & Page Object Model)

### `pages/base_page.py`
```python
from playwright.sync_api import Page

class LocalEatsHomePage:
    URL = "[https://local-eats-unisenac.vercel.app/](https://local-eats-unisenac.vercel.app/)"

    def __init__(self, page: Page):
        self.page = page
        
        # --- Elementos da Tela de Login ---
        self.campo_email = page.locator('#loginEmail')
        self.campo_senha = page.locator('#loginPassword')
        self.botao_entrar = page.locator('button', has_text="Entrar").last
        
        # --- Elementos da Página Principal ---
        self.campo_pesquisa = page.get_by_placeholder("Buscar por culinária ou localização...")
        self.botao_pesquisar = page.get_by_role("button", name="Buscar")

    def abrir(self):
        self.page.goto(self.URL)
        
        # Rotina de Login Automático
        self.campo_email.wait_for(timeout=3000)
        self.campo_email.fill("testefacil@teste.com") 
        self.campo_senha.fill("testefacil123")          
        self.botao_entrar.click()
        self.page.wait_for_timeout(2000)

    def pesquisar(self, termo: str):
        self.campo_pesquisa.wait_for(timeout=5000)
        self.campo_pesquisa.fill(termo)
        self.page.get_by_role("button", name="Buscar").click()
        self.page.wait_for_timeout(1500)
```[cite: 16]

### `tests/test_localeats.py`
```python
from playwright.sync_api import Page, expect
from pages.base_page import LocalEatsHomePage

# Responsável: Jeferson Rodrigues
def test_pesquisar_restaurante_por_localizacao(page: Page):
    # Arrange
    home = LocalEatsHomePage(page)
    
    # Act
    home.abrir()
    home.pesquisar("Centro")
    
    # Assert
    expect(page.get_by_text("Restaurante Sabor 7")).to_be_visible()
    
    # Diferencial: Captura de evidência visual do teste concluído
    page.screenshot(path="atividade-04/evidencia_pesquisa.png", full_page=True)
```[cite: 17]

---

## 4. Evidência de Execução dos Testes

```text
platform win32 -- Python 3.14.6, pytest-9.2.0, pluggy-1.7.0
rootdir: C:\Users\jefer\OneDrive\Desktop\SENAC\QUALIDADE DE SOFTWARE\pbl-qualidade-software-2026-2-main\atividades\atividade-04
plugins: playwright-0.10.0
collected 1 item

tests\test_localeats.py .                                                                                                                     [100%]

======================================================================= 1 passed in 14.70s =======================================================================
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
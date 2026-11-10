from playwright.sync_api import Page

class LocalEatsHomePage:
    URL = "https://local-eats-unisenac.vercel.app/"

    def __init__(self, page: Page):
        self.page = page
        
        # --- Elementos da Tela de Login ---
        # Usando o ID exato dos campos para evitar o erro de violação estrita (Strict Mode)
        self.campo_email = page.locator('#loginEmail')
        self.campo_senha = page.locator('#loginPassword') # Assumindo o ID padrão
        self.botao_entrar = page.locator('button', has_text="Entrar").last
        
        # --- Elementos da Página Principal ---
        self.campo_pesquisa = page.get_by_placeholder("Buscar por culinária ou localização...")
        self.botao_pesquisar = page.get_by_role("button", name="Buscar")

    def abrir(self):
        self.page.goto(self.URL)
        
        # Aguarda o campo de e-mail aparecer
        self.campo_email.wait_for(timeout=3000)
        
        # Preenche as informações
        self.campo_email.fill("testefacil@teste.com") 
        self.campo_senha.fill("testefacil123")          
        self.botao_entrar.click()
        
        # Aguarda a página inicial carregar
        self.page.wait_for_timeout(2000)

    def pesquisar(self, termo: str):
        self.campo_pesquisa.wait_for(timeout=5000)
        self.campo_pesquisa.fill(termo)
        self.page.get_by_role("button", name="Buscar").click()
        self.page.wait_for_timeout(1500)
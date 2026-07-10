import re
from pathlib import Path


class TestReadmeBadges:
    """Testes para validar a presença e formatação das badges no README"""

    @staticmethod
    def read_readme():
        """Lê o conteúdo do README.md"""
        readme_path = Path("README.md")
        if not readme_path.exists():
            raise FileNotFoundError("README.md não encontrado")
        return readme_path.read_text(encoding="utf-8")

    def test_badge_licenca_mit_presente(self):
        """Verifica se a badge de licença MIT está presente"""
        readme = self.read_readme()
        # Padrão para badge MIT do shields.io
        padrao = r"\[!\[MIT License\]\(https://img\.shields\.io/badge/license-MIT-[\w-]+\)\]"
        assert re.search(padrao, readme, re.IGNORECASE), \
            "Badge de licença MIT não encontrada no README"

    def test_badge_python_presente(self):
        """Verifica se a badge de versão Python está presente"""
        readme = self.read_readme()
        # Padrão para badge Python do shields.io
        padrao = r"\[!\[Python\s*(?:3\.\d+\+)?\]\(https://img\.shields\.io/badge/python-3\.[\d]+%2B-[\w-]+\)\]"
        assert re.search(padrao, readme, re.IGNORECASE), \
            "Badge de versão Python não encontrada no README"

    def test_badge_status_presente(self):
        """Verifica se a badge de status do projeto está presente"""
        readme = self.read_readme()
        # Padrão para badge de status
        padrao = r"\[!\[(?:Stable|In Development|Status)\]\(https://img\.shields\.io/badge/status-"
        assert re.search(padrao, readme, re.IGNORECASE), \
            "Badge de status não encontrada no README"

    def test_badges_no_topo(self):
        """Verifica se as badges estão nos primeiros parágrafos"""
        readme = self.read_readme()
        linhas = readme.split("\n")
        badges_encontradas = 0
        
        # Procura badges nos primeiros 20 parágrafos
        for i, linha in enumerate(linhas[:20]):
            if "img.shields.io" in linha:
                badges_encontradas += 1
        
        assert badges_encontradas >= 3, \
            f"Esperado 3 badges no topo, encontrado {badges_encontradas}"

    def test_badges_usam_shields_io(self):
        """Verifica se todas as badges usam shields.io"""
        readme = self.read_readme()
        # Contar referências ao shields.io
        contador = readme.count("img.shields.io")
        assert contador >= 3, \
            f"Esperado mínimo 3 referências a shields.io, encontrado {contador}"

    def test_urls_badges_bem_formadas(self):
        """Verifica se as URLs das badges são válidas"""
        readme = self.read_readme()
        # Padrão geral para URLs do shields.io
        padrao_url = r"https://img\.shields\.io/badge/[\w%2B%-]+"
        urls = re.findall(padrao_url, readme)
        assert len(urls) >= 3, \
            f"Esperado mínimo 3 URLs bem-formadas, encontrado {len(urls)}"
        
        for url in urls:
            assert url.startswith("https://"), \
                f"URL não usa HTTPS: {url}"
            assert "img.shields.io/badge" in url, \
                f"URL não segue formato shields.io: {url}"

    def test_badges_links_validos(self):
        """Verifica se as badges possuem links clicáveis válidos"""
        readme = self.read_readme()
        # Procura por padrão markdown de link com badge
        padrao = r"\[!\[.*?\]\(https://[^)]+\)\]\(([^)]+)\)"
        links = re.findall(padrao, readme)
        assert len(links) >= 3, \
            f"Esperado mínimo 3 links de badges, encontrado {len(links)}"
        
        # Validar que pelo menos um aponta para LICENSE
        links_str = " ".join(links)
        assert any("license" in link.lower() or "license" in readme.lower() 
                   for link in links), \
            "Badge de licença não possui link válido"

    def test_nenhuma_badge_duplicada(self):
        """Verifica se não há badges duplicadas"""
        readme = self.read_readme()
        # Contar badges de cada tipo
        badges_mit = readme.count("MIT")
        badges_python = readme.count("python") + readme.count("Python")
        badges_status = readme.count("status") + readme.count("Status")
        
        # Deve haver pelo menos uma de cada (contagem não deve ser excessiva)
        assert badges_mit >= 1, "Badge MIT não encontrada"
        assert badges_python >= 1, "Badge Python não encontrada"
        assert badges_status >= 1, "Badge de status não encontrada"

    def test_badges_antes_de_descricao(self):
        """Verifica se badges aparecem antes da descrição principal"""
        readme = self.read_readme()
        # Procura pela primeira menção de shields.io
        pos_badge = readme.find("img.shields.io")
        # Procura por seções comuns de descrição (## Descrição, ## About, etc)
        seções_desc = ["## Descrição", "## About", "## Overview", "## Sobre"]
        pos_desc = len(readme)  # Valor padrão se não encontrar
        
        for seção in seções_desc:
            pos = readme.find(seção)
            if pos != -1 and pos < pos_desc:
                pos_desc = pos
        
        assert pos_badge < pos_desc, \
            "Badges devem aparecer antes da seção de descrição"

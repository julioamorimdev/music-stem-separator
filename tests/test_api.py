import pytest
from app import app


@pytest.fixture
def client():
    """Fixture que fornece um cliente de teste Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestHealthEndpoint:
    """Testes para o endpoint /api/health"""

    def test_health_returns_200(self, client):
        """Verifica se /api/health retorna status 200"""
        response = client.get('/api/health')
        assert response.status_code == 200

    def test_health_contains_version(self, client):
        """Verifica se resposta contém chave 'version'"""
        response = client.get('/api/health')
        data = response.get_json()
        assert 'version' in data
        assert isinstance(data['version'], str)
        assert len(data['version']) > 0

    def test_health_contains_model_loaded(self, client):
        """Verifica se resposta contém chave 'model_loaded'"""
        response = client.get('/api/health')
        data = response.get_json()
        assert 'model_loaded' in data
        assert isinstance(data['model_loaded'], bool)

    def test_health_response_type(self, client):
        """Verifica se resposta é JSON válido"""
        response = client.get('/api/health')
        assert response.content_type == 'application/json'
        data = response.get_json()
        assert isinstance(data, dict)


class TestFormatsEndpoint:
    """Testes para o endpoint /api/formats"""

    def test_formats_returns_200(self, client):
        """Verifica se /api/formats retorna status 200"""
        response = client.get('/api/formats')
        assert response.status_code == 200

    def test_formats_contains_formats_key(self, client):
        """Verifica se resposta contém chave 'formats'"""
        response = client.get('/api/formats')
        data = response.get_json()
        assert 'formats' in data

    def test_formats_is_list(self, client):
        """Verifica se 'formats' é uma lista"""
        response = client.get('/api/formats')
        data = response.get_json()
        assert isinstance(data['formats'], list)

    def test_formats_not_empty(self, client):
        """Verifica se lista de formatos não está vazia"""
        response = client.get('/api/formats')
        data = response.get_json()
        assert len(data['formats']) > 0

    def test_formats_have_correct_extension_format(self, client):
        """Verifica se cada formato começa com ponto (.)"""
        response = client.get('/api/formats')
        data = response.get_json()
        for fmt in data['formats']:
            assert isinstance(fmt, str)
            assert fmt.startswith('.')
            assert len(fmt) > 1  # Mais que apenas o ponto

    def test_formats_response_type(self, client):
        """Verifica se resposta é JSON válido"""
        response = client.get('/api/formats')
        assert response.content_type == 'application/json'
        data = response.get_json()
        assert isinstance(data, dict)

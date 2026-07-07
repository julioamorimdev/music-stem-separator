import pytest
from app import app, VERSION, ACCEPTED_FORMATS
import json


@pytest.fixture
def client():
    """Flask test client fixture."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestHealthEndpoint:
    """Tests for GET /api/health endpoint."""

    def test_health_status_code(self, client):
        """Test that health endpoint returns 200 status code."""
        response = client.get('/api/health')
        assert response.status_code == 200

    def test_health_response_structure(self, client):
        """Test that health endpoint returns correct JSON structure."""
        response = client.get('/api/health')
        data = json.loads(response.data)
        
        assert 'status' in data
        assert 'version' in data
        assert 'loaded_model' in data

    def test_health_response_values(self, client):
        """Test that health endpoint returns expected values."""
        response = client.get('/api/health')
        data = json.loads(response.data)
        
        assert data['status'] == 'ok'
        assert data['version'] == VERSION
        assert isinstance(data['loaded_model'], str)
        assert len(data['loaded_model']) > 0

    def test_health_content_type(self, client):
        """Test that health endpoint returns JSON content type."""
        response = client.get('/api/health')
        assert response.content_type == 'application/json'

    def test_health_response_performance(self, client):
        """Test that health endpoint responds in less than 100ms."""
        import time
        start = time.time()
        response = client.get('/api/health')
        elapsed = (time.time() - start) * 1000  # Convert to milliseconds
        
        assert response.status_code == 200
        assert elapsed < 100


class TestFormatsEndpoint:
    """Tests for GET /api/formats endpoint."""

    def test_formats_status_code(self, client):
        """Test that formats endpoint returns 200 status code."""
        response = client.get('/api/formats')
        assert response.status_code == 200

    def test_formats_response_structure(self, client):
        """Test that formats endpoint returns correct JSON structure."""
        response = client.get('/api/formats')
        data = json.loads(response.data)
        
        assert 'formats' in data
        assert isinstance(data['formats'], list)

    def test_formats_response_content(self, client):
        """Test that formats endpoint returns expected formats."""
        response = client.get('/api/formats')
        data = json.loads(response.data)
        
        assert len(data['formats']) > 0
        assert all(isinstance(fmt, str) for fmt in data['formats'])
        assert all(fmt.startswith('.') for fmt in data['formats'])

    def test_formats_response_values(self, client):
        """Test that formats endpoint returns configured formats."""
        response = client.get('/api/formats')
        data = json.loads(response.data)
        
        assert data['formats'] == ACCEPTED_FORMATS

    def test_formats_content_type(self, client):
        """Test that formats endpoint returns JSON content type."""
        response = client.get('/api/formats')
        assert response.content_type == 'application/json'

    def test_formats_response_performance(self, client):
        """Test that formats endpoint responds in less than 100ms."""
        import time
        start = time.time()
        response = client.get('/api/formats')
        elapsed = (time.time() - start) * 1000  # Convert to milliseconds
        
        assert response.status_code == 200
        assert elapsed < 100


class TestEndpointErrors:
    """Tests for error handling."""

    def test_invalid_method_health(self, client):
        """Test that POST to /api/health returns 405."""
        response = client.post('/api/health')
        assert response.status_code == 405

    def test_invalid_method_formats(self, client):
        """Test that POST to /api/formats returns 405."""
        response = client.post('/api/formats')
        assert response.status_code == 405

    def test_nonexistent_endpoint(self, client):
        """Test that nonexistent endpoint returns 404."""
        response = client.get('/api/nonexistent')
        assert response.status_code == 404

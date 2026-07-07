import unittest
from datetime import datetime
from app import app, load_model, model_state
import json

class TestHealthAndFormats(unittest.TestCase):
    
    def setUp(self):
        """Configura o cliente de teste do Flask."""
        self.client = app.test_client()
        self.app = app
    
    def test_health_endpoint_exists(self):
        """Testa se o endpoint /api/health existe e retorna 200."""
        response = self.client.get('/api/health')
        self.assertEqual(response.status_code, 200)
    
    def test_health_response_structure(self):
        """Testa se /api/health retorna estrutura JSON correta."""
        response = self.client.get('/api/health')
        data = json.loads(response.data)
        
        self.assertIn('status', data)
        self.assertIn('version', data)
        self.assertIn('model_loaded', data)
        self.assertIn('timestamp', data)
    
    def test_health_status_values(self):
        """Testa se status é 'healthy' ou 'unhealthy'."""
        response = self.client.get('/api/health')
        data = json.loads(response.data)
        
        self.assertIn(data['status'], ['healthy', 'unhealthy'])
    
    def test_health_model_loaded_boolean(self):
        """Testa se model_loaded é boolean."""
        response = self.client.get('/api/health')
        data = json.loads(response.data)
        
        self.assertIsInstance(data['model_loaded'], bool)
    
    def test_health_version_present(self):
        """Testa se versão está presente."""
        response = self.client.get('/api/health')
        data = json.loads(response.data)
        
        self.assertIsNotNone(data['version'])
        self.assertGreater(len(data['version']), 0)
    
    def test_health_timestamp_format(self):
        """Testa se timestamp está em formato ISO 8601."""
        response = self.client.get('/api/health')
        data = json.loads(response.data)
        
        timestamp = data['timestamp']
        # Valida formato ISO 8601 (simplificado)
        self.assertTrue(timestamp.endswith('Z'))
        self.assertIn('T', timestamp)
    
    def test_formats_endpoint_exists(self):
        """Testa se o endpoint /api/formats existe e retorna 200."""
        response = self.client.get('/api/formats')
        self.assertEqual(response.status_code, 200)
    
    def test_formats_response_structure(self):
        """Testa se /api/formats retorna estrutura JSON correta."""
        response = self.client.get('/api/formats')
        data = json.loads(response.data)
        
        self.assertIn('formats', data)
    
    def test_formats_is_list(self):
        """Testa se formats é uma lista."""
        response = self.client.get('/api/formats')
        data = json.loads(response.data)
        
        self.assertIsInstance(data['formats'], list)
    
    def test_formats_contains_extensions(self):
        """Testa se formats contém extensões com ponto."""
        response = self.client.get('/api/formats')
        data = json.loads(response.data)
        
        self.assertGreater(len(data['formats']), 0)
        for fmt in data['formats']:
            self.assertTrue(fmt.startswith('.'))
    
    def test_health_reflects_model_state(self):
        """Testa se health reflete corretamente o estado do modelo."""
        # Simula modelo carregado
        model_state['loaded'] = True
        response = self.client.get('/api/health')
        data = json.loads(response.data)
        self.assertTrue(data['model_loaded'])
        self.assertEqual(data['status'], 'healthy')
        
        # Simula modelo não carregado
        model_state['loaded'] = False
        response = self.client.get('/api/health')
        data = json.loads(response.data)
        self.assertFalse(data['model_loaded'])
        self.assertEqual(data['status'], 'unhealthy')
        
        # Restaura estado
        model_state['loaded'] = True

if __name__ == '__main__':
    unittest.main()

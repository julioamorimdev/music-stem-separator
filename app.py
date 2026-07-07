import os
from datetime import datetime
from flask import Flask, jsonify
import logging

try:
    from demucs.pretrained import get_model
    DEMUCS_AVAILABLE = True
except ImportError:
    DEMUCS_AVAILABLE = False

from config.constants import VERSION, SUPPORTED_FORMATS, MODEL_NAME

app = Flask(__name__)
logger = logging.getLogger(__name__)

# Estado global do modelo
model_state = {
    'loaded': False,
    'model': None,
    'error': None
}

def load_model():
    """Carrega o modelo Demucs ao iniciar a aplicação."""
    if not DEMUCS_AVAILABLE:
        model_state['error'] = 'Demucs não disponível'
        return False
    
    try:
        model = get_model(MODEL_NAME)
        model_state['model'] = model
        model_state['loaded'] = True
        model_state['error'] = None
        logger.info(f"Modelo {MODEL_NAME} carregado com sucesso")
        return True
    except Exception as e:
        model_state['loaded'] = False
        model_state['error'] = str(e)
        logger.error(f"Erro ao carregar modelo: {e}")
        return False

@app.route('/api/health', methods=['GET'])
def health():
    """Retorna status de saúde da aplicação."""
    status = 'healthy' if model_state['loaded'] else 'unhealthy'
    
    return jsonify({
        'status': status,
        'version': VERSION,
        'model_loaded': model_state['loaded'],
        'timestamp': datetime.utcnow().isoformat() + 'Z'
    }), 200

@app.route('/api/formats', methods=['GET'])
def formats():
    """Retorna lista de extensões de arquivo aceitas."""
    return jsonify({
        'formats': SUPPORTED_FORMATS
    }), 200

if __name__ == '__main__':
    load_model()
    app.run(debug=True, host='0.0.0.0', port=5000)

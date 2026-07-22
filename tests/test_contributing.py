import os
import re

def test_contributing_file_exists():
    """Test that CONTRIBUTING.md exists in repository root"""
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    contributing_path = os.path.join(root_path, 'CONTRIBUTING.md')
    assert os.path.exists(contributing_path), "CONTRIBUTING.md file not found in repository root"

def test_contributing_file_readable():
    """Test that CONTRIBUTING.md can be read"""
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    contributing_path = os.path.join(root_path, 'CONTRIBUTING.md')
    with open(contributing_path, 'r', encoding='utf-8') as f:
        content = f.read()
    assert len(content) > 0, "CONTRIBUTING.md is empty"

def test_contributing_contains_environment_setup():
    """Test that CONTRIBUTING.md contains environment setup section"""
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    contributing_path = os.path.join(root_path, 'CONTRIBUTING.md')
    with open(contributing_path, 'r', encoding='utf-8') as f:
        content = f.read()
    keywords = ['ambiente', 'configurar', 'setup', 'instalar', 'dependências']
    assert any(keyword.lower() in content.lower() for keyword in keywords), \
        "CONTRIBUTING.md does not contain environment setup information"

def test_contributing_contains_test_section():
    """Test that CONTRIBUTING.md contains test execution guidelines"""
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    contributing_path = os.path.join(root_path, 'CONTRIBUTING.md')
    with open(contributing_path, 'r', encoding='utf-8') as f:
        content = f.read()
    keywords = ['teste', 'testes', 'test', 'rodar', 'executar']
    assert any(keyword.lower() in content.lower() for keyword in keywords), \
        "CONTRIBUTING.md does not contain test execution information"

def test_contributing_contains_pr_section():
    """Test that CONTRIBUTING.md contains pull request guidelines"""
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    contributing_path = os.path.join(root_path, 'CONTRIBUTING.md')
    with open(contributing_path, 'r', encoding='utf-8') as f:
        content = f.read()
    keywords = ['pull request', 'pr', 'contribuir', 'enviar', 'merge']
    assert any(keyword.lower() in content.lower() for keyword in keywords), \
        "CONTRIBUTING.md does not contain pull request guidelines"

def test_contributing_is_concise():
    """Test that CONTRIBUTING.md is concise (reasonable length)"""
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    contributing_path = os.path.join(root_path, 'CONTRIBUTING.md')
    with open(contributing_path, 'r', encoding='utf-8') as f:
        content = f.read()
    line_count = len(content.split('\n'))
    # Should be between 10 and 100 lines for a concise guide
    assert 10 <= line_count <= 100, \
        f"CONTRIBUTING.md should be concise (current: {line_count} lines)"

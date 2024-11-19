import os
import sys
import pytest

# Stellt sicher, dass der Flask-Service-Pfad im Python-Pfad ist
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # Importiere die Flask-App aus dem Hauptverzeichnis

@pytest.fixture
def client():
    # Verwende die Flask-App, um den Test-Client bereitzustellen
    with app.test_client() as client:
        yield client

def test_get_data(client):
    # Testet den /data Endpunkt
    response = client.get('/data')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}

def test_health_check(client):
    # Testet den /health Endpunkt
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}

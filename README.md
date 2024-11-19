# BigDataProgramming
## Microservice- und Sidecar-Projekt

    |flask-service/
    |   |app.py                    # Flask-Microservice Code
    |   |requirements.txt          # Abhängigkeiten für den Flask-Service
    |   |Dockerfile                # Dockerfile für den Flask-Service
    |   |README.md                 # Dokumentation zum Flask-Service
    |   |tests/
    |       |test_app.py           # Tests für den Flask-Service
    |sidecar/
    |   |envoy-config.yaml         # Konfigurationsdatei für das Sidecar (Envoy, Traefik, etc.)
    |docker-compose.yml            # Docker-Compose-Datei für beide Container
    |.gitignore                    # Ignorieren von unnötigen Dateien in Git (z. B. __pycache__)
    |README.md                     # Hauptdokumentation für das gesamte Projekt

### Ziel
Dieses Projekt demonstriert einen einfachen Flask-Microservice, der mit einem Envoy-Sidecar kombiniert wird. Das Sidecar dient als Reverse Proxy und bietet Routing- und Monitoring-Funktionen.

### Inhalte
- `flask-service`: Flask-Microservice mit `/data` und `/health` Endpunkten.
- `sidecar`: Envoy-Konfiguration für das Routing zum Flask-Microservice.
- `docker-compose.yml`: Startet beide Services zusammen.

### Schritte zur Ausführung
1. **Build des Flask-Microservices:**
   ```bash
   cd flask-service
   docker build -t flask-microservice .
   docker run -p 1234:1234 flask-microservice
2. **Gesamtes Projekt starten:**
    ```bash
    docker-compose up
3. **Endpunkte testen:** <br>
- Über den `Flask-Service` direkt:
    ```bash
    curl -X GET http://localhost:1234/data
- Über das `Sidecar`:
    ```bash
    curl -X GET http://localhost:8080/data
### Tests
4. **Führen Sie die Tests für den Flask-Microservice mit pytest aus:**
    ```bash
    cd tests
    pytest -v   # die Option -v ist optional und bietet eine detaillierte Ansicht der Testergebnisse
# BigDataProgramming Teil 2 (3706017)
## Microservice- und Sidecar-Projekt
```
flask-service/
  ├── app.py               # Flask-Microservice
  ├── Dockerfile           # Dockerfile für Flask-Microservice
  └── requirements.txt     # Python-Abhängigkeiten für Flask-Microservice

nginx/
  ├── Dockerfile           # Dockerfile für Nginx-Sidecar
  └── nginx.conf           # Konfigurationsdatei für Nginx-Sidecar

docker-compose.yml         # Docker-Compose Datei für Flask-Microservice und Nginx-Sidecar
README.md                  # Projektdokumentation
```

### Inhalte
- `flask-service`: Flask-Microservice mit `/data` und `/health` Endpunkten.
- `sidecar`: Nginx-Konfiguration für das Routing zum Flask-Microservice.
- `docker-compose.yml`: Startet beide Services zusammen.

# Schritte zur Ausführung des Projekts

### 1. Benutzerdefiniertes Netzwerk erstellen
Bevor der Container gestartet wird, wird ein benutzerdefiniertes Docker-Netzwerk erstellt,
damit die beiden Container miteinander kommunizieren können.

```bash
docker network create bigdataprogramming
```

### 2. Flask-Microservice bauen und starten
Wechseln Sie in das Verzeichnis `flask-service/` und bauen Sie das Docker-Image:

```bash
cd flask-service
docker build -t flask-microservice .
```

Starten Sie den Flask-Microservice im benutzerdefinierten Netzwerk:

```bash
docker run -d --network bigdataprogramming -p 1234:1234 --name flask-microservice flask-microservice
```

### 3. Nginx-Sidecar bauen und starten
Nutzen Sie ggf. ein neues Terminal-Fenster. Wechseln Sie anschließend in das Verzeichnis `nginx/` und bauen Sie das Docker-Image:

```bash
cd ../nginx
docker build -t nginx-sidecar .
```

Starten Sie das Nginx-Sidecar im benutzerdefinierten Netzwerk:

```bash
docker run -d --network bigdataprogramming -p 8080:8080 --name nginx-sidecar nginx-sidecar
```

### 4. Testen des Setups

#### Direktzugriff auf den Flask-Microservice:
Um zu überprüfen, ob der Flask-Service korrekt läuft, verwenden Sie den folgenden `curl`-Befehl:

```bash
curl -X GET http://localhost:1234/data
```

Die Antwort sollte sein:
```json
{"message": "Hello, World!"}
```

#### Zugriff über das Nginx-Sidecar:
Um sicherzustellen, dass das Nginx-Sidecar Anfragen korrekt weiterleitet, verwenden Sie den folgenden `curl`-Befehl:

```bash
curl -X GET http://localhost:8080/data
```

Auch hier sollte die Antwort sein:
```json
{"message": "Hello, World!"}
```

*Hinweis: Statt dem Endpoint /data kann auch /health verwendet werden, um den Zustand des Servers zu überprüfen!*
    
### 5. Container stoppen
Um die Container zu stoppen, können Sie folgende Befehle verwenden:

```bash
docker stop flask-microservice nginx-sidecar
docker rm flask-microservice nginx-sidecar
```

## Verwendung von Docker Compose
Alternativ können Sie das gesamte Setup auch mit Docker Compose starten,
um beide Container gleichzeitig zu starten und zu verknüpfen.
Im Hauptverzeichnis des Projekts finden Sie eine `docker-compose.yml` Datei.
Sie können das Setup einfach mit folgendem Befehl starten:

```bash
docker-compose up
```

Docker Compose sorgt dafür, dass beide Container automatisch im gleichen Netzwerk gestartet werden.

### Endpunkte testen:<br>
- Über den `Flask-Service` direkt:
    ```bash
    curl -X GET http://localhost:1234/data
    curl -X GET http://localhost:1234/health
- Über das `Sidecar`:
    ```bash
    curl -X GET http://localhost:8080/data
    curl -X GET http://localhost:8080/health
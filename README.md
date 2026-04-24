# ⛏️ Minecraft Server Discord Bot

Ein einfacher Discord-Bot, der den Status eines Minecraft-Servers (Java Edition) abfragt und ein kleines Minispiel beinhaltet. Vollständig dockerisiert für schnelles Deployment und maximale Sicherheit.

## 🚀 Features
- **`!status`**: Zeigt Server-IP, Port und die aktuelle Spieleranzahl live an.
- **`!spiel [Schere/Stein/Papier]`**: Spielt eine Runde Schere-Stein-Papier gegen den Bot.
- **Docker-Support**: Kein lokales Python-Setup nötig – alles läuft isoliert im Container.
- **Sicher**: Sensible Daten wie der Bot-Token werden über Umgebungsvariablen geladen.

---

## 🛠️ Setup & Installation

### 1. Dateien vorbereiten

Stelle sicher, dass du folgende Dateien in deinem Projektordner angelegt hast:

#### A) `.env` (für den Discord-Token)
Erstelle eine Datei namens `.env` im Hauptverzeichnis und füge deinen Bot-Token ein:

```text
DISCORD_TOKEN=DEIN_BOT_TOKEN_HIER
```

#### B) `app.json` (für die Server-Konfiguration)
Erstelle eine Datei namens `app.json` für die Minecraft-Server-Daten:

**`Beachte! Die Port Nummer wie unten zu sehen ist die Standard Port Nummer. Diese kann je nach Konfiguration anders sein!`**
```json
{
    "ms_url": "deine-server-ip.de",
    "ms_port": 25565
}
```

---

## 2. Docker installieren (WICHTIG)

Es ist sehr wichtig, dass du Docker installiert hast.
Ansonsten werden die folgenden Schritte **`NICHT`** funktionieren!

---

## 3. Mit Docker starten (Empfohlen)

Du musst keine Abhängigkeiten auf deinem PC installieren. Führe einfach den untenstehenden Start-Befehl aus und die .yml macht den Rest.

### Container starten:
```bash
docker compose up -d
```
### Container stoppen:
```bash
docker compose down
```

> 💡 Hinweis für die Docker unerfahrende -> Hier könnt ihr das offizielle Docker CLI Cheat Sheet nutzen https://docs.docker.com/get-started/docker_cheatsheet.pdf

---

## 🏗️ Projektstruktur

```plaintext
.
├── bot.py             # Die Bot-Logik (Python)
├── Dockerfile         # Bauanleitung für das Docker-Image
├── requirements.txt   # Benötigte Python-Bibliotheken
├── .env               # Private Geheimnisse (wird durch .gitignore geschützt)
├── app.json           # Server-Konfiguration (wird durch .gitignore geschützt)
├── .gitignore         # Verhindert den Upload privater Dateien auf GitHub
└── .dockerignore      # Verhindert, dass unnötige Dateien im Image landen
```

---

## 🔒 Sicherheit

Die Dateien `.env` und `app.json` enthalten sensible Informationen. Sie sind in der `.gitignore` eingetragen, damit sie niemals öffentlich auf GitHub landen. Nutze die bereitgestellten `.example`-Dateien im Repository als Vorlage für dein eigenes Setup.

---

Entwickelt mit ❤️, Docker und der Hilfe von ChatGPT und Gemini.
# 🤖 Discord Minecraft Status Bot

Ein einfacher Discord-Bot, der den Status eines Minecraft-Servers überprüft und zusätzlich ein kleines Minigame (Schere, Stein, Papier) bietet.

---

## ✨ Features

- 🟢 Minecraft-Server Status anzeigen (inkl. Spieleranzahl)
- 🔴 Offline-Erkennung
- 🎮 Minigame: Schere, Stein, Papier
- ⚙️ Konfiguration über `app.json`

---

## 📦 Voraussetzungen

- Python 3.10 oder höher
- Discord Bot Token

### Installation der Abhängigkeiten

```bash
pip install discord.py mcstatus
```

---

## ⚙️ Einrichtung

### 1. Repository klonen

```bash
git clone https://github.com/dein-username/dein-repo.git
cd dein-repo
```

---

### 2. `app.json` erstellen

Erstelle im Projektverzeichnis eine Datei namens `app.json`:

```json
{
  "ms_url": "example.minecraftserver.com",
  "ms_port": 25565,
  "token": "DEIN_DISCORD_BOT_TOKEN"
}
```

---

### 3. Discord Bot erstellen

1. Öffne das Discord Developer Portal  
2. Neue Application erstellen  
3. Unter **Bot → Add Bot** klicken  
4. Token kopieren und in `app.json` einfügen  
5. Unter **Privileged Gateway Intents**:
   - ✅ Message Content Intent aktivieren  

---

### 4. Bot einladen

Gehe zu **OAuth2 → URL Generator**:

- Scopes:
  - `bot`
- Bot Permissions:
  - Send Messages
  - Embed Links

Dann generierte URL im Browser öffnen und Bot hinzufügen.

---

### 5. Bot starten

```bash
python bot.py
```

---

## 💬 Befehle

### `!status`

Zeigt den aktuellen Status des Minecraft-Servers an:

- 🟢 Online → Spieleranzahl wird angezeigt  
- 🔴 Offline → Hinweis wird ausgegeben  

---

### `!spiel <wahl>`

Spiele Schere, Stein, Papier gegen den Bot.

**Beispiel:**

```bash
!spiel schere
```

**Optionen:**
- schere
- stein
- papier

---

## 📁 Projektstruktur

```
.
├── bot.py
└── app.json
```

---

## ⚠️ Hinweise

- Stelle sicher, dass dein Minecraft-Server öffentlich erreichbar ist
- Der Bot benötigt Internetzugriff
- Fehler beim Status kommen meist von falscher IP/Port

---

## 🛠️ To-Do / Ideen

- [ ] Slash Commands hinzufügen
- [ ] Server Ping anzeigen
- [ ] Mehr Spiele integrieren
- [ ] Logging erweitern

---

## 📄 Lizenz

Dieses Projekt ist frei nutzbar. Du kannst es anpassen und erweitern.

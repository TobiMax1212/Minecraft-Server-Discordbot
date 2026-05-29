# ⛏️ Minecraft Server Discord Bot

A simple Discord bot that queries the status of a Minecraft server (Java Edition) and includes a small minigame. Fully dockerized for fast deployment and maximum security.

## 🚀 Features
- **`!status`**: Displays the server IP, port, and live player count.
- **`!game [Rock/Paper/Scissors]`**: Plays a round of Rock, Paper, Scissors against the bot.
- **`!h`**: Shows a help message listing all available commands.
- **Docker Support**: No local Python setup required – everything runs isolated within a container.
- **Secure**: Sensitive data, such as the bot token, is loaded via environment variables.

---

## 🛠️ Setup & Installation

### 1. Prepare Files

Make sure you have created the following files in your project directory:

#### A) `.env` (for the Discord Token)
Create a file named `.env` in the root directory and add your bot token:

```text
DISCORD_TOKEN=YOUR_BOT_TOKEN_HERE
```

#### B) `app.json` (for the Server Configuration)
Create a file named `app.json` for the Minecraft server data:

**`Note: The port number shown below is the default port. This might differ depending on your configuration!`**
```json
{
    "ms_url": "your-server-ip.com",
    "ms_port": 25565
}
```

---

## 2. Create the Discord Bot

Before the bot can be used, it must be created via the Discord Developer Portal.

### Step 1:
Go to the Developer Portal, click on **'New Application'**, and create a bot for your community.

### Step 2:
Navigate to the **'Bot'** tab and grant the bot all necessary **'Privileged Gateway Intents'**.

### Step 3:
Still in the **'Bot'** tab, click on **'Reset Token'** and save the generated token.
**'IMPORTANT! NO ONE ELSE SHOULD SEE OR POSSESS THIS TOKEN. KEEP IT SAFE!'**

### Step 4:
Go to the **'OAuth2'** tab, navigate to the URL Generator, select the **'bot'** scope, and assign the desired permissions.

### Step 5:
Copy the generated URL and paste it into your web browser. Discord will open and ask where the bot should be installed. Select your existing server here.

---

## 3. Install Docker (IMPORTANT)

It is crucial that you have Docker installed.
Otherwise, the following steps will **`NOT`** work!

---

## 4. Run with Docker (Recommended)

You don't need to install any dependencies on your PC. Simply run the start command below, and the `docker-compose.yml` will handle the rest.

### Start container:
```bash
docker compose up -d
```
### Stop container:
```bash
docker compose down
```

> 💡 Note for Docker beginners -> You can use the official Docker CLI Cheat Sheet here: https://docs.docker.com/get-started/docker_cheatsheet.pdf

---

## 🏗️ Project Structure

```plaintext
.
├── bot.py             # The bot logic (Python)
├── Dockerfile         # Build instructions for the Docker image
├── requirements.txt   # Required Python libraries
├── .env               # Private secrets (protected by .gitignore)
├── app.json           # Server configuration (protected by .gitignore)
├── .gitignore         # Prevents the upload of private files to GitHub
└── .dockerignore      # Prevents unnecessary files from ending up in the image
```

---

## 🔒 Security

The files `.env` and `app.json` contain sensitive information. They are included in the `.gitignore` to ensure they are never published on GitHub. Use the provided `.example` files in the repository as templates for your own setup.

---

Developed with ❤️ and Docker.
# AI-Powered Telegram Bot Suite

A modular, object-oriented Telegram bot framework featuring:

- **GPT-based text generation**  
- **Task creation, updating & reminders**  
- **Interactive menus** via Inline Keyboards  
- **Pluggable storage** (SQLite, Redis, …)  
- **Clean separation** of core, handlers, models  

## ⚙️ Installation

```bash
git clone https://github.com/HosseinSaeidiHub/AITeleBot.git
cd AITeleBot
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.aitelebot .env          # set BOT_TOKEN, MODEL_PATH, etc.

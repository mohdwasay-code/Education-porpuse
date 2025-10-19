from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = Flask(__name__)

@app.route('/')
def home():
    return "Telegram Bot is Running Successfully!"

# Example Telegram command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Bot is alive on Render ✅")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)

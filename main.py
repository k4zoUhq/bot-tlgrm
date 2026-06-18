import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    ChatJoinRequestHandler,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

OWNER_ID = 8171813065

# Stockage temporaire des demandes vues par le bot

pending_requests = {}

async def handle_join_request(update, context):
    request = update.chat_join_request
    user = request.from_user
    chat_id = request.chat.id

    pending_requests.setdefault(chat_id, set()).add(user.id)

    await context.bot.send_message(
        chat_id=user.id,
        text=(
            f"Coucou {user.first_name} 👋\n\n"
            "Si toi aussi tu veux devenir VIP et avoir accès a plus de 21.500 vidéos / photos 🍓 pour seulement 1.04€ -> https://vipleak.cc/ayaro\n\n"
            '1. <b><a href="https://t.me/retourvip">RETOURS VIP 🌟</a></b>\n'
            '2. <b><a href="https://t.me/+GR2avjK42sE0NDQ8">CANAL POST 😈</a></b>'
        ),
        parse_mode="HTML"
    )

async def acceptall(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text("❌ Accès refusé.")
        return

    total = 0

    for chat_id, users in pending_requests.items():
        for user_id in list(users):
            try:
                await context.bot.approve_chat_join_request(
                    chat_id=chat_id,
                    user_id=user_id
                )
                users.remove(user_id)
                total += 1
            except Exception as e:
                print(f"Erreur pour {user_id}: {e}")

    await update.message.reply_text(
        f"✅ {total} demande(s) acceptée(s)."
    )

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(ChatJoinRequestHandler(handle_join_request))
    app.add_handler(CommandHandler("acceptall", acceptall))

    print("Bot démarré !")
    app.run_polling()

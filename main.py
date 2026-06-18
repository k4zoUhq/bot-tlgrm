import os
import logging
from telegram.ext import Application, ChatJoinRequestHandler

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def handle_join_request(update, context):
    user = update.chat_join_request.from_user

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

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(handle_join_request))
    print("Bot démarré !")
    app.run_polling()

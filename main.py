import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, ChatJoinRequestHandler

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
LIEN_SITE = "https://nude-snap.cc/join"

async def handle_join_request(update, context):
    user = update.chat_join_request.from_user

    bouton = InlineKeyboardMarkup([[
        InlineKeyboardButton("S'inscrire 🍓", url=LIEN_SITE)
    ]])

    await context.bot.send_message(
        chat_id=user.id,
        text=(
            f"Bonjour {user.first_name} 👋\n\n"
            "Pour accéder au canal, vous devez :\n\n"
            "1. Mettre que vous avez 21 ans ou + et une e-mail valide 🍓\n"
            "2. Une fois fait vous serez automatiquement accepté dans le canal 😈\n\n"
            "Cliquez ci-dessous pour vous inscrire 👇 :"
        ),
        reply_markup=bouton
    )

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(handle_join_request))
    print("Bot démarré !")
    app.run_polling()

import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    ChatJoinRequestHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
LIEN_SITE = "https://nude-snap.cc/join"
LIEN_AUTRE_CANAL = "https://t.me/+GR2avjK42sE0NDQ8"

async def handle_join_request(update, context):
    user = update.chat_join_request.from_user

    bouton = InlineKeyboardMarkup([[
        InlineKeyboardButton("S'inscrire 🍓", url=LIEN_SITE)
    ]])

    await context.bot.send_message(
        chat_id=user.id,
        text=(
            f"Coucou {user.first_name} 👋\n\n"
            "Pour accéder au canal, Tu doit :\n\n"
            "1. Mettre que tu à 21 ans ou + et une e-mail valide 🍓\n"
            "2. Une fois fait tu serez accepté automatiquement par le bot dans le canal 😈\n\n"
            "Clique ci-dessous pour t'inscrire 👇"
        ),
        reply_markup=bouton
    )

async def handle_left_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.left_chat_member

    try:
        await context.bot.send_message(
            chat_id=user.id,
            text=(
                "😕 Tu as quitté le canal.\n\n"
                "Si tu préfères un canal où les vidéos sont publiées directement dedans 😈🍓,\n\n"
                f"Rejoins-le ici 👇\n\n{LIEN_AUTRE_CANAL}\n\n"
                "On t'attend 😉"
            )
        )
    except Exception as e:
        logging.error(f"Impossible d'envoyer le message à {user.id}: {e}")

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(ChatJoinRequestHandler(handle_join_request))
    app.add_handler(
        MessageHandler(filters.StatusUpdate.LEFT_CHAT_MEMBER, handle_left_member)
    )

    print("Bot démarré !")
    app.run_polling()

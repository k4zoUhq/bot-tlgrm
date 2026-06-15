import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, ChatJoinRequestHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8634045765:AAFE_nXAc1XpX_lXQpgip0Cje8xqfkjfc1w")
LIEN_SITE = "https://nude-snap.cc/join"  # Change ça !

async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user
    
    bouton = InlineKeyboardMarkup([[
        InlineKeyboardButton("👉 S'inscrire ici", url=LIEN_SITE)
    ]])
    
    await context.bot.send_message(
        chat_id=user.id,
        text=(
            f"Bonjour {user.first_name} 👋\n\n"
            f"Pour accéder au canal, tu dois d'abord t'inscrire sur notre site :\n\n"
            f"Une fois inscrit, ton accès sera validé automatiquement ✅\n\n"
            f"Pour être accepter, au moment de l'inscriptions tu doit avoir obligatoirement plus de 21 ans ou + et mettre une e-mail valide ! 🍓"
        ),
        reply_markup=bouton
    )

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(ChatJoinRequestHandler(handle_join_request))

print("Bot démarré !")
import asyncio
asyncio.run(app.run_polling())

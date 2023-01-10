import view
import model
import bot_token
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


def start():
    """Стартовая функция"""

    app = ApplicationBuilder().token(bot_token.token).build()
    app.add_handler(CommandHandler("start", view.greetings))
    app.add_handler(CommandHandler("show", view.show_book))
    app.add_handler(CommandHandler("add", view.add_contact))

    app.run_polling()


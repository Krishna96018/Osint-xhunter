import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from handlers.start import start_command
import config

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    app = Application.builder().token(config.BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    print("[+] Bot is running...")
    await app.run_polling()

if __name__ == '__main__':
    import asyncio

    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    loop.run_until_complete(main())

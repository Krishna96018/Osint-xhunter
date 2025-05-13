from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import config

# ======== START COMMAND ============
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_text = f"""
╔════════════════════════════╗
║  [OSINT XHUNTER BOT]       ║
╠════════════════════════════╣
║ Welcome, {user.first_name}!           
║ You have accessed a powerful   
║ OSINT scanner tool.           
║                              
║ Commands coming soon...      
║ Stay tuned!                  
║                              
║ Owner: @Naitik0003           
╚════════════════════════════╝
"""
    await update.message.reply_text(welcome_text)

# ========= MAIN FUNCTION ============
async def main():
    print("[*] Setting up OSINT XHunter Bot...")
    app = Application.builder().token(config.BOT_TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start_command))

    print("[+] Initializing bot...")
    await app.initialize()

    print("[+] Starting bot...")
    await app.start()

    print("[+] Bot is now polling updates...")
    await app.updater.start_polling()

    await app.idle()

# =========== ENTRY POINT ============
if __name__ == '__main__':
    import asyncio

    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    loop.run_until_complete

from telegram import Update
from telegram.ext import ContextTypes
from config import ADMIN_USERNAME

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    msg = f"""
[✅ ACCESS GRANTED ✅]

> Welcome, <b>{user.first_name}</b>!
> Identity confirmed as <code>{user.username}</code>
> Accessing <b>OSINT XHunter System</b>...

━━━━━━━━━━━━━━━━━━━━━━
<b>Commands You Can Use:</b>
/checkemail - Check email for leaks
/checkusername - Track username across sites
/checkphone - Basic phone OSINT
/checkdomain - Domain info & subdomains
/iplookup - IP location & blacklist check
/matrix - Fun hacker terminal
/contact - Contact admin

━━━━━━━━━━━━━━━━━━━━━━
<b>Bot by:</b> {ADMIN_USERNAME}
<b>UI:</b> Terminal Styled | Hacker Vibe
━━━━━━━━━━━━━━━━━━━━━━
    """
    await update.message.reply_text(msg, parse_mode='HTML')

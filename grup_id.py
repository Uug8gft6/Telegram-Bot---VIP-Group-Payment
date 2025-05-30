from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from telegram.constants import ChatMemberStatus
from dotenv import load_dotenv
import os

# Memuat token dari file .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Fungsi untuk mendeteksi ID channel/grup secara otomatis
async def cek_id(update: Update, context: CallbackContext):
    chat = update.effective_chat
    chat_id = chat.id

    # Mengecek apakah bot adalah admin
    bot_member = await context.bot.get_chat_member(chat_id, context.bot.id)
    if bot_member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        is_admin = "✅ Bot adalah admin di channel ini."
    else:
        is_admin = "⚠️ Bot BUKAN admin di channel ini. Tambahkan bot sebagai admin untuk akses penuh."

    # Menentukan jenis chat
    chat_type = "Channel" if chat.type == "channel" else "Group/Private"

    
    if update.message:
        await update.message.reply_text(
            f"✅ ID Chat: {chat_id}\n💬 Jenis: {chat_type}\n{is_admin}"
            # print(f"✅ ID Chat: {chat_id}\n💬 Jenis: {chat_type}\n{is_admin}")
        )
    elif update.channel_post:
        await update.channel_post.reply_text(
            f"✅ ID Channel: {chat_id}\n💬 Jenis: Channel\n{is_admin}"
            # print(f"✅ ID Channel: {chat_id}\n💬 Jenis: Channel\n{is_admin}")
        )
    else:
        print(f"Pesan tidak dapat diidentifikasi. ID: {chat_id}")

# Inisialisasi bot
app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.ALL, cek_id))


print("Bot Dijalankan...")
app.run_polling()

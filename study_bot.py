from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

class StudyBot:
    def __init__(self):
        # Target belajar harian (bisa disesuaikan)
        self.progress = {"TWK": 0, "TIU": 0, "TKP": 0}
        self.targets = {"TWK": 20, "TIU": 15, "TKP": 10}

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        # Tampilkan menu belajar
        keyboard = [
            [InlineKeyboardButton("📚 TWK", callback_data="study_twk"),
             InlineKeyboardButton("🧮 TIU", callback_data="study_tiu"),
             InlineKeyboardButton("👥 TKP", callback_data="study_tkp")],
            [InlineKeyboardButton("📊 Progress", callback_data="study_progress")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Selamat belajar! Pilih menu di bawah:", reply_markup=reply_markup)

    async def handle_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()

        # Cek callback dan update progress
        if query.data == "study_progress":
            progress = "\n".join([f"{key}: {val}/{self.targets[key]}" for key, val in self.progress.items()])
            await query.edit_message_text(f"📊 Progress Belajar:\n{progress}")
        else:
            subject = query.data.split("_")[1].upper()
            self.progress[subject] += 1
            await query.edit_message_text(f"✅ Soal {subject} selesai! Total: {self.progress[subject]}")

    def run(self):
        # Masukin token bot lo di sini
        TOKEN = "7563675945:AAE7iiaL7ry0NfNZv_TSYZoyaN6fLAbqHdg"

        app = Application.builder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", self.start))
        app.add_handler(CallbackQueryHandler(self.handle_callback))
        print("Bot jalan, bro! 🚀")
        app.run_polling()

if __name__ == "__main__":
    bot = StudyBot()
    bot.run()

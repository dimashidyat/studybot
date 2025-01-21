from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config import CHANNELS

class StudyHandler:
    def __init__(self):
        self.progress = {"TWK": 0, "TIU": 0, "TKP": 0}
        self.targets = {"TWK": 20, "TIU": 15, "TKP": 10}

    async def show_menu(self, update, context: ContextTypes.DEFAULT_TYPE):
        keyboard = [
            [InlineKeyboardButton("📚 TWK", callback_data="study_twk"),
             InlineKeyboardButton("🧮 TIU", callback_data="study_tiu"),
             InlineKeyboardButton("👥 TKP", callback_data="study_tkp")],
            [InlineKeyboardButton("📊 Progress", callback_data="study_progress")],
            [InlineKeyboardButton("📱 Join Channel BUMN", url=f"https://t.me/{CHANNELS['bumn']}")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.callback_query.edit_message_text(
            "📚 *MENU BELAJAR BULOG*\n\nPilih menu di bawah:",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )

    async def handle_callback(self, update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()

        if query.data == "study_progress":
            progress = "\n".join([f"{key}: {val}/{self.targets[key]}" for key, val in self.progress.items()])
            await query.edit_message_text(f"📊 Progress Belajar:\n{progress}")
        else:
            subject = query.data.split("_")[1].upper()
            self.progress[subject] += 1
            await query.edit_message_text(f"✅ Soal {subject} selesai! Total: {self.progress[subject]}")
 

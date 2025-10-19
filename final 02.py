# ===========================
#  SKILL GUIDE BOT (SOHAILXMEEN MODERN VERSION)
#  Made by SohailXmeen 💻🔥
# ===========================

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

# === ENTER YOUR BOT TOKEN HERE ===
TOKEN = "8353102084:AAGsw8qd-isgYMMSnPjRiG9z6CaWy1WfQkc"

# === STATES ===
LANGUAGE, MAIN_MENU, SUB_MENU = range(3)

# === LANGUAGE DATA ===
languages = {
    "TELUGU 🇮🇳": "telugu",
    "HINDI 🇮🇳": "hindi",
    "ENGLISH 🌍": "english"
}

# === MENU DATA ===
menus = {
    "english": [
        "💻 COMPUTER & SOFTWARE SKILLS",
        "⚙️ ENGINEERING & TECHNICAL KNOWLEDGE",
        "🎓 ACADEMIC DEGREES & STUDY",
        "💼 CAREER, JOBS & SKILLS GROWTH",
        "🚧 PROJECTS & PRACTICE ZONE",
        "📚 SHORT LEARNING & KNOWLEDGE ZONE",
        "🧰 TOOLS & RESOURCES",
        "🎨 CREATIVE & HOBBY ZONE",
        "ℹ️ ABOUT & SUPPORT"
    ],
    "hindi": [
        "💻 कंप्यूटर और सॉफ्टवेयर स्किल्स",
        "⚙️ इंजीनियरिंग और तकनीकी ज्ञान",
        "🎓 शैक्षणिक डिग्री और अध्ययन",
        "💼 करियर, नौकरी और स्किल्स ग्रोथ",
        "🚧 प्रोजेक्ट्स और प्रैक्टिस ज़ोन",
        "📚 शॉर्ट लर्निंग और नॉलेज ज़ोन",
        "🧰 टूल्स और संसाधन",
        "🎨 क्रिएटिव और हॉबी ज़ोन",
        "ℹ️ अबाउट और सपोर्ट"
    ],
    "telugu": [
        "💻 కంప్యూటర్ & సాఫ్ట్‌వేర్ నైపుణ్యాలు",
        "⚙️ ఇంజనీరింగ్ & టెక్నికల్ నాలెడ్జ్",
        "🎓 అకడమిక్ డిగ్రీస్ & స్టడీ",
        "💼 కెరీర్, ఉద్యోగాలు & నైపుణ్య వృద్ధి",
        "🚧 ప్రాజెక్టులు & ప్రాక్టీస్ జోన్",
        "📚 షార్ట్ లెర్నింగ్ & నాలెడ్జ్ జోన్",
        "🧰 టూల్స్ & వనరులు",
        "🎨 క్రియేటివ్ & హాబీ జోన్",
        "ℹ️ గురించి & మద్దతు"
    ]
}

sub_menus = {
    "💻 COMPUTER & SOFTWARE SKILLS": [
        "🧾 MS OFFICE",
        "🏗 AUTOCADD & DESIGN TOOLS",
        "📊 ACCOUNTANCY SOFTWARE",
        "🌐 WEB DESIGN & DEVELOPMENT",
        "💻 PROGRAMMING LANGUAGES",
        "🖥 COMPUTER CONCEPTS & IT BASICS"
    ],
    "⚙️ ENGINEERING & TECHNICAL KNOWLEDGE": [
        "🏗 CIVIL ENGINEERING",
        "⚙️ MECHANICAL ENGINEERING",
        "🔌 ELECTRICAL / ELECTRONICS",
        "💻 COMPUTER SCIENCE & AI"
    ],
    "🎓 ACADEMIC DEGREES & STUDY": [
        "💻 COMPUTER & IT DEGREES",
        "🏗 ENGINEERING DEGREES",
        "💼 COMMERCE & MANAGEMENT",
        "📚 ARTS & SCIENCE",
        "🩺 MEDICAL & PARAMEDICAL",
        "🎨 CREATIVE & VOCATIONAL STUDIES"
    ],
    "💼 CAREER, JOBS & SKILLS GROWTH": [
        "🏠 WORK FROM HOME & FREELANCING",
        "📄 RESUME SAMPLES",
        "🚀 FREELANCING & STARTUPS"
    ],
    "🚧 PROJECTS & PRACTICE ZONE": ["🛠 ADDING SOON..."],
    "📚 SHORT LEARNING & KNOWLEDGE ZONE": [
        "📏 MATHS & GEOMETRY",
        "🧠 REASONING & APTITUDE",
        "🌍 GENERAL KNOWLEDGE",
        "📘 ENGLISH GRAMMAR",
        "💻 COMPUTER GK",
        "📝 STUDY TIPS & MEMORY TRICKS"
    ],
    "🧰 TOOLS & RESOURCES": [
        "⚙️ ONLINE TOOLS",
        "📚 LEARNING RESOURCES",
        "🌐 SYSTEM & INTERNET TIPS"
    ],
    "🎨 CREATIVE & HOBBY ZONE": [
        "🎨 GRAPHIC DESIGN",
        "🎥 VIDEO EDITING",
        "🎧 AUDIO EDITING",
        "📸 PHOTOGRAPHY & EDITING",
        "✍️ CONTENT WRITING & BLOGGING",
        "📱 SOCIAL MEDIA GROWTH TIPS"
    ],
    "ℹ️ ABOUT & SUPPORT": [
        "👤 MOHD WASEY URF SOHAIL\n📞 +91 6304892809\n📷 Instagram: @mohd_sohail_008\n✉️ Email: wasayrider786@gmail.com"
    ]
}

# === START COMMAND ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[key] for key in languages.keys()]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "🌍 Please select your language to continue 👇",
        reply_markup=reply_markup
    )
    return LANGUAGE

# === LANGUAGE SELECTION ===
async def choose_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    choice = update.message.text
    context.user_data["lang"] = languages.get(choice, "english")
    lang = context.user_data["lang"]
    keyboard = [[opt] for opt in menus[lang]] + [["🔙 BACK"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "📚 Choose a category 👇",
        reply_markup=reply_markup
    )
    return MAIN_MENU

# === MAIN MENU HANDLER ===
async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    lang = context.user_data["lang"]
    if text == "🔙 BACK":
        return await start(update, context)
    if text not in [m for m in menus[lang]]:
        await update.message.reply_text("❌ Invalid option. Please choose from below.")
        return MAIN_MENU

    # Show sub-menu or message
    options = sub_menus.get(text, [])
    keyboard = [[opt] for opt in options] + [["🔙 BACK", "🏠 MENU"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(f"✨ {text} ✨", reply_markup=reply_markup)
    return SUB_MENU

# === SUB MENU HANDLER ===
async def sub_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    lang = context.user_data["lang"]

    if text == "🔙 BACK":
        keyboard = [[opt] for opt in menus[lang]] + [["🔙 BACK"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("📚 Choose a category 👇", reply_markup=reply_markup)
        return MAIN_MENU
    elif text == "🏠 MENU":
        return await start(update, context)
    else:
        await update.message.reply_text(f"📝 {text}")
        return SUB_MENU

# === MAIN ===
def main():
    app = Application.builder().token(TOKEN).build()

    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            LANGUAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, choose_language)],
            MAIN_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, main_menu)],
            SUB_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, sub_menu)],
        },
        fallbacks=[],
    )

    app.add_handler(conv)
    print("🤖 SohailXmeen Skill Guide Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
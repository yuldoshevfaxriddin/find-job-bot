from telegram import InlineQueryResultArticle, InputTextMessageContent, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, InlineQueryHandler, CommandHandler, ContextTypes
import request
import settings

TOKEN = settings.TOKEN  # <-- BotFather bergan tokenni shu yerga yozing

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Inline rejimda ishlating: @it_park_2_bot so'z yozing.")

# Inline query funksiyasi
async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query

    if not query or len(query) < 2:
        return   
    results = request.find_data(query)
    responses = []
    if not results:
        responses.append(
            InlineQueryResultArticle(
                id="1",
                title="Natija topilmadi",
                input_message_content=InputTextMessageContent("Kechirasiz, bu so'z bo'yicha natija topilmadi.")
            )
        )
        await update.inline_query.answer(responses, cache_time=1)
        return
    for index, result in enumerate(results, start=1):
        responses.append(
            InlineQueryResultArticle(
            id=index,
            title=result['title'],
            description=f"{result['company']} - {result['location']}",
            # input_message_content=InputTextMessageContent(f"{result['title']}\n<b>{result['company']}</b>\n{result['location']}", parse_mode='HTML'),
            input_message_content=InputTextMessageContent(f"{result['title']}\n<b>{result['company']}</b>\n<i>{result['location']}</i>"+f"\n{result['link']}",parse_mode='HTML'),
            reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton("Saytga kirish", url=result['link'])]]
    )
        ),
        
        )

    # results = [
    #     InlineQueryResultArticle(
    #         id=1,
    #         title="Salom berish",
    #         input_message_content=InputTextMessageContent(f"Salom, {query}!"),
    #         reply_markup=InlineKeyboardMarkup(
    #     [[InlineKeyboardButton("Saytga kirish", url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png")]]
    # )
    #     ),
    #     InlineQueryResultArticle(
    #         id=2,
    #         title="Kvadrat hisoblash",
    #         input_message_content=InputTextMessageContent(
    #             f"{query}² = {int(query)**2 if query.isdigit() else 'Raqam kiriting'}"
    #         )
    #     )
    # ]

    await update.inline_query.answer(responses, cache_time=1)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(InlineQueryHandler(inline_query))

    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()

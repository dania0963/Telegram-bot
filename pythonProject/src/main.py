from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler, CallbackQueryHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from test import check_syriatel

token = "6537607035:AAGtrtqlOlGUfzQ0lZT70bglNT-wpR_3Hp8"
import json

data = json.load(open("data.json", "r"))
print(data)


###############################menu################################
async def main_menu(update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text=main_menu_message(),
        reply_markup=main_menu_keyboard())


async def first_menu(update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text=first_menu_message(),
        reply_markup=first_menu_keyboard())


async def second_menu(update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text=second_menu_message(),
        reply_markup=second_menu_keyboard())

##########################callback handlers#################################



async def Syriatel_deposite(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    context.user_data["index"] = -1
    context.user_data["type"] = "syriatel_deposit"
    context.user_data["data"] = []
    await query.answer()
    await query.edit_message_text(
        text="ادخل رقم عملية التحويل",
    )


async def Mtn_deposite(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    context.user_data["index"] = -1
    context.user_data["type"] = "mtn_deposit"
    context.user_data["data"] = []
    await query.answer()
    await query.edit_message_text(
        text="ادخل رقم عملية التحويل",
    )

async def Bemo_deposite(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bemo_account=464747
    query = update.callback_query
    context.user_data["index"] = -1
    context.user_data["type"] = "bemo_deposit"
    context.user_data["data"] = []
    await query.answer()
    await query.edit_message_text(
        text="قم بالتحويل الى الحساب"+f"\n {bemo_account}"+"\n ثم ادخل رقم حسابك",
    )

async def Usdt_deposite(update: Update, context: ContextTypes.DEFAULT_TYPE):
    usdt_account="TB7N3FsP8iw7LYseMhRcCvxWBHbEg4Yqs3"
    usdt_dollar=13000
    query = update.callback_query
    context.user_data["index"] = -1
    context.user_data["type"] = "usdt_deposit"
    context.user_data["data"] = []
    await query.answer()
    await query.edit_message_text(
        text="ارسل الى المحفظة"+f"\n {usdt_account}"+"\n ثم ادخل كود عملية الارسال"+f"\n 1 USDT = {usdt_dollar}",
    )

async def Payeer_deposite(update: Update, context: ContextTypes.DEFAULT_TYPE):
    payeer_account="P1102546041"
    payeer_dollar=13000
    query = update.callback_query
    context.user_data["index"] = -1
    context.user_data["type"] = "payeer_deposit"
    context.user_data["data"] = []
    await query.answer()
    await query.edit_message_text(
        text="ارسل الى العنوان"+f"\n {payeer_account}"+"\n ثم ادخل عنوان المحفظة المرسل منها"+f"\n 1 Payeer USD = {payeer_dollar}",
    )
async def accept(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    massege = query.message.text.split("\n")[3].split(" ")
    await context.bot.send_message(massege[3], "تمت الموافقة على طلبك")
    await query.answer()
    await query.edit_message_text(
        text="تم اعلام المستخدم"
    )


async def refuse(update, context):
    query = update.callback_query
    massege = query.message.text.split("\n")[3].split(" ")
    await context.bot.send_message(massege[3], "تمت رفض طلبك")
    await query.answer()
    await query.edit_message_text(
        text="تم اعلام المستخدم"
    )


############################ Keyboards #########################################
def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton("⬇️شحن رصيد في البوت ️", callback_data='m1'),
                 InlineKeyboardButton('⬆️سحب رصيد من البوت', callback_data='m2')],
                [InlineKeyboardButton('🎁 رمز هدية', callback_data='m3')],
                [InlineKeyboardButton('💵 اهداء رصيد', callback_data='m4')],
                [InlineKeyboardButton('📲 تواصل معنا', callback_data='m5'),
                 InlineKeyboardButton('✉️ رسالة للادمن', callback_data='m6')],
                [InlineKeyboardButton('📃 الشروحات', callback_data='m7')],
                [InlineKeyboardButton('🔁 السجل', callback_data='m8')]]

    return InlineKeyboardMarkup(keyboard)


def first_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Syriatel Cash', callback_data='d1')],
                [InlineKeyboardButton('Mtn Cash', callback_data='d2')],
                [InlineKeyboardButton('بيمو', callback_data='d3')],
                [InlineKeyboardButton('Usdt', callback_data='d4')],
                [InlineKeyboardButton('Payeer', callback_data='d5')],
                [InlineKeyboardButton('الرئيسية', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def second_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Syriatel Cash', callback_data='m2_1')],
                [InlineKeyboardButton('Mtn Cash', callback_data='m2_2')],
                [InlineKeyboardButton('بيمو', callback_data='m2_3')],
                [InlineKeyboardButton('Payeer', callback_data='m2_4')],
                [InlineKeyboardButton('Usdt', callback_data='m2_5')],
                [InlineKeyboardButton('الرئيسية', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def card():
    keyboard = [[InlineKeyboardButton('موافقة ✅', callback_data='a'), InlineKeyboardButton('رفض ❌', callback_data='r')]]
    return InlineKeyboardMarkup(keyboard)


############################# Messages #########################################
def main_menu_message():
    return 'Choose the option in main menu:'


def first_menu_message():
    return 'Choose the submenu in first menu:'


def second_menu_message():
    return 'Choose the submenu in second menu:'


# functions


###########################command handlers###############################
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(main_menu_message(),
                                    reply_markup=main_menu_keyboard())


async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    id = str(update.effective_user.id)
    balance = data[id]["balance"]
    print(context.bot.getChatAdministrators)
    await update.message.reply_text(
        f" رصيدك في البوت : {balance} \n  ايدي التلغرام الخاص بك :  {id}")




################################message handler####################################
async def test_massege(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if (context.user_data["type"] == "syriatel_deposit"):
        context.user_data["index"] += 1
        t1 = update.message.text
        context.user_data["data"].insert(context.user_data["index"], t1)
        if context.user_data["index"] == 1:
            if int(t1) < 5000:
                await update.message.reply_text("ان اقل قيمة للشحن هي 5000 الرجاء اعادة ادخال القيمة 👇")
                context.user_data["index"] -= 1
                return
            check = check_syriatel()
            list = [context.user_data["data"][0], context.user_data["data"][1], 'نجاح']
            if list in check:
                await update.message.reply_text("تم اضافة رصيد للبوت")
                return
            else:
                await update.message.reply_text("لا يوجد عملية تحويل ")
                return
        await update.message.reply_text("ادخل القيمة المحولة ")

    elif context.user_data["type"] == "mtn_deposit":
        context.user_data["index"] += 1
        t1 = update.message.text
        context.user_data["data"].insert(context.user_data["index"], t1)
        if context.user_data["index"] == 1:
            if int(t1) < 5000:
                await update.message.reply_text("ان اقل قيمة للشحن هي 5000 الرجاء اعادة ادخال القيمة 👇")
                context.user_data["index"] -= 1
                return
            await context.bot.send_message(chat_id=645706695, reply_markup=card(),
                                           text="🔴 لديك طلب شحن رصيد في البوت عن طريق mtn cash" +
                                                f"\n رقم العملية {context.user_data['data'][0]}" +
                                                f"\n القيمة المحولة {context.user_data['data'][1]}" +
                                                f"\n معرف الزبون {update.effective_user.id}")
            await update.message.reply_text("تم ارسال الطلب للادمن يرجى انتظار الموافقة")
            return
        await update.message.reply_text("ادخل القيمة المحولة ")

    elif context.user_data["type"] == "bemo_deposit":
        context.user_data["index"] += 1
        t1 = update.message.text
        context.user_data["data"].insert(context.user_data["index"], t1)
        if context.user_data["index"] == 1:
            if int(t1) < 5000:
                await update.message.reply_text("ان اقل قيمة للشحن هي 5000 الرجاء اعادة ادخال القيمة 👇")
                context.user_data["index"] -= 1
                return
            await context.bot.send_message(chat_id=645706695, reply_markup=card(),
                                           text="🔴 لديك طلب شحن رصيد في البوت عن طريق Bemo Bank" +
                                                f"\n رقم الحساب {context.user_data['data'][0]}" +
                                                f"\n القيمة المحولة {context.user_data['data'][1]}" +
                                                f"\n معرف الزبون {update.effective_user.id}")
            await update.message.reply_text("تم ارسال الطلب للادمن يرجى انتظار الموافقة")
            return
        await update.message.reply_text("ادخل القيمة المحولة ")
    elif context.user_data["type"] == "usdt_deposit":
        context.user_data["index"] += 1
        t1 = update.message.text
        context.user_data["data"].insert(context.user_data["index"], t1)
        if context.user_data["index"] == 1:
            await context.bot.send_message(chat_id=645706695, reply_markup=card(),
                                           text="🔴 لديك طلب شحن رصيد في البوت عن طريق Usdt" +
                                                f"\n كود عملية الارسال {context.user_data['data'][0]}" +
                                                f"\n القيمة المحولة {context.user_data['data'][1]} $" +
                                                f"\n معرف الزبون {update.effective_user.id}")
            await update.message.reply_text("تم ارسال الطلب للادمن يرجى انتظار الموافقة")
            return
        await update.message.reply_text("ادخل القيمة المحولة ")
    elif context.user_data["type"] == "payeer_deposit":
        context.user_data["index"] += 1
        t1 = update.message.text
        context.user_data["data"].insert(context.user_data["index"], t1)
        if context.user_data["index"] == 1:
            await context.bot.send_message(chat_id=645706695, reply_markup=card(),
                                           text="🔴 لديك طلب شحن رصيد في البوت عن طريق Payeer" +
                                                f"\n عنوان المحفظة المرسل منها {context.user_data['data'][0]}" +
                                                f"\n القيمة المحولة {context.user_data['data'][1]} $" +
                                                f"\n معرف الزبون {update.effective_user.id}")
            await update.message.reply_text("تم ارسال الطلب للادمن يرجى انتظار الموافقة")
            return
        await update.message.reply_text("ادخل القيمة المحولة ")






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('balance', balance))
    app.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    app.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))
    app.add_handler(CallbackQueryHandler(second_menu, pattern='m2'))
    app.add_handler(CallbackQueryHandler(Syriatel_deposite, pattern='d1'))
    app.add_handler(CallbackQueryHandler(Mtn_deposite, pattern='d2'))
    app.add_handler(CallbackQueryHandler(Bemo_deposite, pattern='d3'))
    app.add_handler(CallbackQueryHandler(Usdt_deposite, pattern='d4'))
    app.add_handler(CallbackQueryHandler(Payeer_deposite, pattern='d5'))
    app.add_handler(CallbackQueryHandler(accept, pattern='a'))
    app.add_handler(CallbackQueryHandler(refuse, pattern='r'))
    app.add_handler(MessageHandler(filters.TEXT, test_massege))

    app.run_polling(poll_interval=5)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

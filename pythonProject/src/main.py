from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler, CallbackQueryHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from test import check_syriatel

token = "6537607035:AAGtrtqlOlGUfzQ0lZT70bglNT-wpR_3Hp8"
import json

data = json.load(open("data.json", "r"))
print(data)
keys = list(data.keys())
print(keys)

payeer_dollar = 13000
usdt_dollar = 13000


def check_user(id):
    if id in keys:
        return True
    return False


# def reset_data(data,type="initial"):
#     data["index"] = -1
#     data["type"] = type
#     data["data"] = []
#

##########################callback handlers#################################
async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="يمكنك الاختيار من القائمة التالية",
        reply_markup=main_menu_keyboard())


async def Admin_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="يمكنك الاختيار من القائمة التالية",
        reply_markup=Admin_main_menu_keyboard())


async def first_menu(update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="اختر احد طرق الدفع ان اقل قيمة للشحن في البوت هي: 5000 ليرة سورية",
        reply_markup=first_menu_keyboard())


async def second_menu(update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="اختر احد طرق السحب",
        reply_markup=second_menu_keyboard())


async def history_menu(update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="السجل",
        reply_markup=history_menu_keyboard())


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
    bemo_account = 464747
    query = update.callback_query
    context.user_data["index"] = -1
    context.user_data["type"] = "bemo_deposit"
    context.user_data["data"] = []
    await query.answer()
    await query.edit_message_text(
        text="قم بالتحويل الى الحساب" + f"\n {bemo_account}" + "\n ثم ادخل رقم حسابك",
    )


async def Usdt_deposite(update: Update, context: ContextTypes.DEFAULT_TYPE):
    usdt_account = "TB7N3FsP8iw7LYseMhRcCvxWBHbEg4Yqs3"
    query = update.callback_query
    context.user_data["index"] = -1
    context.user_data["type"] = "usdt_deposit"
    context.user_data["data"] = []
    await query.answer()
    await query.edit_message_text(
        text="ارسل الى المحفظة" + f"\n {usdt_account}" + "\n ثم ادخل كود عملية الارسال" + f"\n 1 USDT = {usdt_dollar}",
    )


async def Payeer_deposite(update: Update, context: ContextTypes.DEFAULT_TYPE):
    payeer_account = "P1102546041"
    query = update.callback_query
    context.user_data["index"] = -1
    context.user_data["type"] = "payeer_deposit"
    context.user_data["data"] = []
    await query.answer()
    await query.edit_message_text(
        text="ارسل الى العنوان" + f"\n {payeer_account}" + "\n ثم ادخل عنوان المحفظة المرسل منها" + f"\n 1 Payeer USD = {payeer_dollar}",
    )


async def Syriatel_withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    context.user_data["index"] = -1
    context.user_data["type"] = "syriatel_withdraw"
    context.user_data["data"] = []
    await query.answer()
    await query.edit_message_text(
        text="ادخل الرقم المراد التحويل اليه",
    )


async def Mtn_withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    context.user_data["index"] = -1
    context.user_data["type"] = "mtn_withdraw"
    context.user_data["data"] = []
    await query.answer()
    await query.edit_message_text(
        text="ادخل الرقم المراد التحويل اليه",
    )


async def Bemo_withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    context.user_data["index"] = -1
    context.user_data["type"] = "bemo_withdraw"
    context.user_data["data"] = []
    await query.answer()
    await query.edit_message_text(
        text="ادخل رقم حسابك",
    )


async def Usdt_withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    usdt_account = "TB7N3FsP8iw7LYseMhRcCvxWBHbEg4Yqs3"
    query = update.callback_query
    context.user_data["index"] = -1
    context.user_data["type"] = "usdt_withdraw"
    context.user_data["data"] = []
    await query.answer()
    await query.edit_message_text(
        text="ارسل عنوان المحفظة",
    )


async def Payeer_withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    context.user_data["index"] = -1
    context.user_data["type"] = "payeer_withdraw"
    context.user_data["data"] = []
    await query.answer()
    await query.edit_message_text(
        text="ارسل عنوان الحساب"
    )


async def Transfer_withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    context.user_data["index"] = -1
    context.user_data["type"] = "transfer_withdraw"
    context.user_data["data"] = []
    await query.answer()
    await query.edit_message_text(
        text="ارسل اسمك الثلاثي والمحافظة ورقم هاتفك بسطر واحد",
    )


async def accept(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    massege = query.message.text.split("\n")[3].split(" ")
    user_id = massege[3]
    await context.bot.send_message(user_id, "تمت الموافقة على طلبك")
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


async def Send_money(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["index"] = -1
    context.user_data["type"] = "send_money"
    context.user_data["data"] = []
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="ارسل ايدي التلغرام للشخص المراد اهداء الرصيد اليه \n يمكن الحصول على الايدي عن طريق ضغط زر  رصيدي"
    )


async def Gift_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["type"] = "gift_code"
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="يتم الحصول على كود الهدية من قبل الادمن من خلال مسابقات وجوائز \n" +
             "ادخل كود الهدية لشحن رصيدك بقيمته  👇"
    )


async def Admin_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["type"] = "admin_message"
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="اكتب رسالة ليتم ارسالها للادمن 👇"

    )


async def Contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["type"] = "contact"
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="للتواصل مع فريق الدعم" + "\n @DaniaDabaa",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" رجوع ️", callback_data='main')]])
    )


############################ Keyboards #########################################
def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton("⬇️شحن رصيد في البوت ️", callback_data='m1'),
                 InlineKeyboardButton('⬆️سحب رصيد من البوت', callback_data='m2')],
                [InlineKeyboardButton('🎁 رمز هدية', callback_data='m3')],
                [InlineKeyboardButton('💵 اهداء رصيد', callback_data='m4')],
                [InlineKeyboardButton('✉️ رسالة للادمن', callback_data='m5'),
                 InlineKeyboardButton('📲 تواصل معنا', callback_data='m6')],
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
    keyboard = [[InlineKeyboardButton('Syriatel Cash', callback_data='w1')],
                [InlineKeyboardButton('Mtn Cash', callback_data='w2')],
                [InlineKeyboardButton('بيمو', callback_data='w3')],
                [InlineKeyboardButton('Payeer', callback_data='w4')],
                [InlineKeyboardButton('Usdt', callback_data='w5')],
                [InlineKeyboardButton('حوالة', callback_data='w6')],
                [InlineKeyboardButton('الرئيسية', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def history_menu_keyboard():
    keyboard = [[InlineKeyboardButton('سجل الشحن', callback_data='w1')],
                [InlineKeyboardButton('سجل السحب', callback_data='w2')],
                [InlineKeyboardButton('رجوع', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def Admin_main_menu_keyboard():
    keyboard = [[InlineKeyboardButton(" تحديث بيانات البوت 🔄️", callback_data='a-m1'),
                 InlineKeyboardButton('ادارة الادمنز 🔑', callback_data='a-m2')],
                [InlineKeyboardButton('سجل العمليات 📉', callback_data='a-m3')],
                [InlineKeyboardButton('رؤية حسابات العملاء 👤', callback_data='a-m4'),
                 InlineKeyboardButton('انشاء كود هدية 🎁', callback_data='a-m5')]]
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
    if update.effective_user.id == 645706695:
        await update.message.reply_text("يمكنك الاختيار من القائمة التالية",
                                        reply_markup=Admin_main_menu_keyboard())
    else:
        await update.message.reply_text("يمكنك الاختيار من القائمة التالية",
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
            check = []#check_syriatel()
            list = [context.user_data["data"][0], context.user_data["data"][1], 'نجاح']
            if list in check:
                await update.message.reply_text("تم اضافة رصيد للبوت")
                context.user_data["type"] = "null"
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
                                                f"\n معرف الزبون {update.effective_user.id}"+"\n")
            await update.message.reply_text("تم ارسال الطلب للادمن يرجى انتظار الموافقة")
            context.user_data["type"] = "null"
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
                                                f"\n معرف الزبون {update.effective_user.id}"+"\n")
            await update.message.reply_text("تم ارسال الطلب للادمن يرجى انتظار الموافقة")
            context.user_data["type"] = "null"
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
                                                f"\n معرف الزبون {update.effective_user.id}"+"\n")
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
                                                f"\n معرف الزبون {update.effective_user.id}"+"\n")
            await update.message.reply_text("تم ارسال الطلب للادمن يرجى انتظار الموافقة")
            context.user_data["type"] = "null"
            return
        await update.message.reply_text("ادخل القيمة المحولة ")
    elif context.user_data["type"] == "send_money":
        context.user_data["index"] += 1
        t1 = update.message.text
        context.user_data["data"].insert(context.user_data["index"], t1)
        if context.user_data["index"] == 0:
            if t1 not in keys:
                await update.message.reply_text("لا يوجد مستخدم في البوت بهذا الايدي  ❌ ")
                context.user_data["index"] -= 1
                return
            await update.message.reply_text("ادخل القيمة التي تريد اهدائها ")
        if context.user_data["index"] == 1:
            balance = 100
            if int(t1) > balance:
                await update.message.reply_text("ان القيمة المدخلة اكبر من رصيدك في البوت ")
                context.user_data["index"] -= 1
                return
            await update.message.reply_text("تم الاهداء ")
            context.user_data["type"] = "null"
            # add balance to context.user_data['data'][0] + edit this user balance
    elif context.user_data["type"] == "syriatel_withdraw":
        context.user_data["index"] += 1
        t1 = update.message.text
        context.user_data["data"].insert(context.user_data["index"], t1)
        if context.user_data["index"] == 1:
            # get balance with user id update.effective_user.id
            balance = 100
            if int(t1) > balance:
                await update.message.reply_text("ان القيمة المدخلة اكبر من رصيدك في البوت ")
                context.user_data["index"] -= 1
                return
            await context.bot.send_message(chat_id=645706695, reply_markup=card(),
                                           text="🔴 لديك طلب سحب رصيد من البوت عن طريق syriatel" +
                                                f"\n الرقم المراد الارسال اليه {context.user_data['data'][0]}" +
                                                f"\n القيمة المراد سحبها {context.user_data['data'][1]} " +
                                                f"\n معرف الزبون {update.effective_user.id}"+"\n")
            await update.message.reply_text("تم ارسال الطلب للادمن يرجى انتظار الموافقة")
            context.user_data["type"] = "null"
            return
        await update.message.reply_text("ادخل القيمة التي تريد سحبها ")
    elif context.user_data["type"] == "mtn_withdraw":
        context.user_data["index"] += 1
        t1 = update.message.text
        context.user_data["data"].insert(context.user_data["index"], t1)
        if context.user_data["index"] == 1:
            # get balance with user id update.effective_user.id
            balance = 100
            if int(t1) > balance:
                await update.message.reply_text("ان القيمة المدخلة اكبر من رصيدك في البوت ")
                context.user_data["index"] -= 1
                return
            await context.bot.send_message(chat_id=645706695, reply_markup=card(),
                                           text="🔴 لديك طلب سحب رصيد من البوت عن طريق mtn" +
                                                f"\n الرقم المراد الارسال اليه {context.user_data['data'][0]}" +
                                                f"\n القيمة المراد سحبها {context.user_data['data'][1]} " +
                                                f"\n معرف الزبون {update.effective_user.id}"+"\n")
            await update.message.reply_text("تم ارسال الطلب للادمن يرجى انتظار الموافقة")
            context.user_data["type"] = "null"
            return
        await update.message.reply_text("ادخل القيمة التي تريد سحبها ")
    elif context.user_data["type"] == "payeer_withdraw":
        context.user_data["index"] += 1
        t1 = update.message.text
        context.user_data["data"].insert(context.user_data["index"], t1)
        if context.user_data["index"] == 1:
            # get balance with user id update.effective_user.id
            balance = 100
            if int(t1) > balance:
                await update.message.reply_text("ان القيمة المدخلة اكبر من رصيدك في البوت ")
                context.user_data["index"] -= 1
                return
            await context.bot.send_message(chat_id=645706695, reply_markup=card(),
                                           text="🔴 لديك طلب سحب رصيد من البوت عن طريق payeer" +
                                                f"\n عنوان الحساب المراد الارسال اليه {context.user_data['data'][0]}" +
                                                f"\n القيمة المراد سحبها {context.user_data['data'][1]} " +
                                                f"\n معرف الزبون {update.effective_user.id}"+"\n")
            await update.message.reply_text("تم ارسال الطلب للادمن يرجى انتظار الموافقة")
            context.user_data["type"] = "null"
            return
        await update.message.reply_text("ادخل القيمة المراد سحبها بالعملة" + f"\n 1 Payeer USD = {payeer_dollar}")
    elif context.user_data["type"] == "bemo_withdraw":
        context.user_data["index"] += 1
        t1 = update.message.text
        context.user_data["data"].insert(context.user_data["index"], t1)
        if context.user_data["index"] == 1:
            # get balance with user id update.effective_user.id
            balance = 100
            if int(t1) > balance:
                await update.message.reply_text("ان القيمة المدخلة اكبر من رصيدك في البوت ")
                context.user_data["index"] -= 1
                return
            await context.bot.send_message(chat_id=645706695, reply_markup=card(),
                                           text="🔴 لديك طلب سحب رصيد من البوت عن طريق bemo" +
                                                f"\n رقم الحساب المراد الارسال اليه {context.user_data['data'][0]}" +
                                                f"\n القيمة المراد سحبها {context.user_data['data'][1]} " +
                                                f"\n معرف الزبون {update.effective_user.id}"+"\n")
            await update.message.reply_text("تم ارسال الطلب للادمن يرجى انتظار الموافقة")
            context.user_data["type"] = "null"
            return
        await update.message.reply_text("ادخل القيمة التي تريد سحبها")
    elif context.user_data["type"] == "transfer_withdraw":
        context.user_data["index"] += 1
        t1 = update.message.text
        context.user_data["data"].insert(context.user_data["index"], t1)
        if context.user_data["index"] == 1:
            # get balance with user id update.effective_user.id
            balance = 100
            if int(t1) > balance:
                await update.message.reply_text("ان القيمة المدخلة اكبر من رصيدك في البوت ")
                context.user_data["index"] -= 1
                return
            await context.bot.send_message(chat_id=645706695, reply_markup=card(),
                                           text="🔴 لديك طلب سحب رصيد من البوت عن طريق transfer" +
                                                f"\n معلومات المستخدم {context.user_data['data'][0]}" +
                                                f"\n القيمة المراد سحبها {context.user_data['data'][1]} " +
                                                f"\n معرف الزبون {update.effective_user.id}"+"\n")
            await update.message.reply_text("تم ارسال الطلب للادمن يرجى انتظار الموافقة")
            context.user_data["type"] = "null"
            return
        await update.message.reply_text("ادخل القيمة التي تريد سحبها")
    elif context.user_data["type"] == "usdt_withdraw":
        context.user_data["index"] += 1
        t1 = update.message.text
        context.user_data["data"].insert(context.user_data["index"], t1)
        if context.user_data["index"] == 1:
            # get balance with user id update.effective_user.id
            balance = 100
            if int(t1) > balance:
                await update.message.reply_text("ان القيمة المدخلة اكبر من رصيدك في البوت ")
                context.user_data["index"] -= 1
                return
            await context.bot.send_message(chat_id=645706695, reply_markup=card(),
                                           text="🔴 لديك طلب سحب رصيد من البوت عن طريق usdt" +
                                                f"\n عنوان المحفظة المراد الارسال اليها {context.user_data['data'][0]}" +
                                                f"\n القيمة المراد سحبها {context.user_data['data'][1]} " +
                                                f"\n معرف الزبون {update.effective_user.id}"+"\n")
            await update.message.reply_text("تم ارسال الطلب للادمن يرجى انتظار الموافقة")
            context.user_data["type"] = "null"
            return
        await update.message.reply_text("ادخل القيمة المراد سحبها بالليرة" + f"\n 1 usdt = {usdt_dollar}")
    elif context.user_data["type"] == "gift_code":
        t1 = update.message.text
        # get the code status
        if t1 == "ggg":
            # add to user balance
            await update.message.reply_text("تم شحن رصيدك بقيمة")
            # reset
            context.user_data["type"] = "null"
        await update.message.reply_text("الكود الذي ادخلته غير فعال")
        # reset
    elif context.user_data["type"] == "admin_message":
        t1 = update.message.text
        await context.bot.send_message(chat_id=645706695,
                                       text=f"🔴 لديك رسالة من المستخدم ذات المعرف {update.effective_user.id} :" +
                                            f"\n {t1}")
        await update.message.reply_text("تم ارسال رسالتك بنجاح سيتم الرد عليك بأقرب وقت اهلا وسهلا بك ✅")
        context.user_data["type"] = "null"
        # reset


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('balance', balance))
    app.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    app.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))
    app.add_handler(CallbackQueryHandler(second_menu, pattern='m2'))
    app.add_handler(CallbackQueryHandler(Gift_code, pattern='m3'))
    app.add_handler(CallbackQueryHandler(Send_money, pattern='m4'))
    app.add_handler(CallbackQueryHandler(Admin_message, pattern='m5'))
    app.add_handler(CallbackQueryHandler(Contact, pattern='m6'))
    app.add_handler(CallbackQueryHandler(history_menu, pattern='m8'))
    app.add_handler(CallbackQueryHandler(Syriatel_deposite, pattern='d1'))
    app.add_handler(CallbackQueryHandler(Mtn_deposite, pattern='d2'))
    app.add_handler(CallbackQueryHandler(Bemo_deposite, pattern='d3'))
    app.add_handler(CallbackQueryHandler(Usdt_deposite, pattern='d4'))
    app.add_handler(CallbackQueryHandler(Payeer_deposite, pattern='d5'))
    app.add_handler(CallbackQueryHandler(Syriatel_withdraw, pattern='w1'))
    app.add_handler(CallbackQueryHandler(Mtn_withdraw, pattern='w2'))
    app.add_handler(CallbackQueryHandler(Bemo_withdraw, pattern='w3'))
    app.add_handler(CallbackQueryHandler(Payeer_withdraw, pattern='w4'))
    app.add_handler(CallbackQueryHandler(Usdt_withdraw, pattern='w5'))
    app.add_handler(CallbackQueryHandler(Transfer_withdraw, pattern='w6'))
    app.add_handler(CallbackQueryHandler(accept, pattern='a'))
    app.add_handler(CallbackQueryHandler(refuse, pattern='r'))
    app.add_handler(MessageHandler(filters.TEXT, test_massege))

    app.run_polling(poll_interval=5)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

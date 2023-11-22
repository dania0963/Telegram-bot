import re

from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler, CallbackQueryHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResult

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


async def pricing_menu(update, context):
    query = update.callback_query
    await query.answer()
    context.user_data["index"] = -1
    context.user_data["type"] = "pricing"
    context.user_data["data"] = []
    await query.edit_message_text(
        text="العملات",
        reply_markup=pricing_menu_keyboard())


def pricing_from_to_menu_keyboard():
    keyboard = [[InlineKeyboardButton("من $ الى ليرة ️", callback_data='from_dollar')],
                [InlineKeyboardButton('من ليرة الى $', callback_data='from_pound')],
                [InlineKeyboardButton('رجوع', callback_data='admin4')]]
    return InlineKeyboardMarkup(keyboard)


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


async def pricing_payeer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    context.user_data["type"] = "pricing_payeer"
    await query.answer()
    await query.edit_message_text(
        text="payeer",
        reply_markup=pricing_from_to_menu_keyboard()
    )


async def pricing_usdt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["type"] = "pricing_usdt"
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="usdt",
        reply_markup=pricing_from_to_menu_keyboard()
    )


async def from_dollar_to_pound(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["pricing"] = "from_dollar"
    query = update.callback_query
    await query.answer()
    # get the type to get data and last update
    await query.edit_message_text(
        text="السعر الحالي"
        , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" تحديث ️", callback_data='update_price'),
                                              InlineKeyboardButton(" رجوع ️", callback_data='admin4')]])
    )


async def from_pound_to_dollar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["pricing"] = "from_pound"
    query = update.callback_query
    await query.answer()
    # get the type to get data and last update
    await query.edit_message_text(
        text="السعر الحالي"
        , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" تحديث ️", callback_data='update_price'),
                                              InlineKeyboardButton(" رجوع ️", callback_data='admin4')]])
    )


async def create_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["type"] = "create_code"
    context.user_data["index"] = -1
    context.user_data["data"] = []
    query = update.callback_query
    await query.answer()
    # get the type to get data and last update
    await query.edit_message_text(
        text="ادخل الرمز"
    )


async def admin_management(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    # get the type to get data and last update
    await query.edit_message_text(
        text="ادارة الادمنز",
        reply_markup=admin_management_menu_keyboard()
    )


async def admin_show(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    # get the admins
    await query.edit_message_text(
        text="عرض الادمنز",
        reply_markup=admin_members_keyboard(3)
    )


async def admin_add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["type"] = "admin_add"
    context.user_data["index"] = -1
    context.user_data["data"] = []
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="ادخل معرف التلغرام الموافق",
    )


async def admin_delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    id = query.data.split(".")[1]
    print(id)
    # change admin role of this id
    await query.answer()
    await query.edit_message_text(
        text="تمت ازالة الادمن",
    )


async def users_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    # get the users with their ichancy accounts and export them to excel file
    await query.answer()
    await query.edit_message_text(
        text="ملف",
    )


async def operations_log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    # get the users with their ichancy accounts and export them to excel file
    await query.answer()
    await query.edit_message_text(
        text="سجل العمليات",
        reply_markup=operations_log_keyboard()
    )


async def log_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["type"] = "log_all"
    context.user_data["index"] = -1
    context.user_data["data"] = []
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="1️⃣ ادخل تاريخ البداية للسجلات المراد الحصول عليها بالصيغة : \n يوم شهر سنة (2023 10 10)",

    )


async def log_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["type"] = "log_user"
    context.user_data["index"] = -1
    context.user_data["data"] = []
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="ادخل معرف التلغرام للمستخدم",
    )


async def explanations(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    # get explanations
    await query.edit_message_text(
        text="الشروحات",
    )


async def ichancy_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    # get explanations
    await query.edit_message_text(
        text="ايتشانسي",
        reply_markup=ichancy_keyboard()
    )

async def create_ichancy_account(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["type"] = "create_ichancy_account"
    context.user_data["index"] = -1
    context.user_data["data"] = []
    query = update.callback_query
    await query.answer()
    # get explanations
    await query.edit_message_text(
        text="ادخل اسم حساب ايتشانسي الجديد",

    )

async def deposit_to_ichancy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["type"] = "deposit_to_ichancy"
    context.user_data["index"] = -1
    context.user_data["data"] = []
    query = update.callback_query
    await query.answer()
    # get explanations
    await query.edit_message_text(
        text="ادخل اسم حساب ايتشانسي المراد شحنه",

    )

async def withdraw_from_ichancy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["type"] = "withdraw_from_ichancy"
    context.user_data["index"] = -1
    context.user_data["data"] = []
    query = update.callback_query
    await query.answer()
    # get explanations
    await query.edit_message_text(
        text="ادخل اسم حساب ايتشانسي المراد السحب منه",

    )

async def user_ichancy_accounts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    # get user accounts
    #get additional data from api
    #for each account add to text
    await query.edit_message_text(
        text="حساباتي",

    )
############################ Keyboards #########################################
def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton("ايتشانسي", callback_data='ichancy_menu')],
                [InlineKeyboardButton("⬇️شحن رصيد في البوت ️", callback_data='m1'),
                 InlineKeyboardButton('⬆️سحب رصيد من البوت', callback_data='m2')],
                [InlineKeyboardButton('🎁 رمز هدية', callback_data='m3'),
                 InlineKeyboardButton('💵 اهداء رصيد', callback_data='m4')],
                [InlineKeyboardButton('نظام الاحالات', callback_data='m9')],
                [InlineKeyboardButton('✉️ رسالة للادمن', callback_data='m5'),
                 InlineKeyboardButton('📲 تواصل معنا', callback_data='m6')],
                [InlineKeyboardButton('📃 الشروحات', callback_data='m7'),
                 InlineKeyboardButton('🔁 السجل', callback_data='m8')]]

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
    keyboard = [[InlineKeyboardButton('سجل الشحن', callback_data='deposit_log')],
                [InlineKeyboardButton('سجل السحب', callback_data='withdraw_log')],
                [InlineKeyboardButton('رجوع', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def Admin_main_menu_keyboard():
    keyboard = [[InlineKeyboardButton(" تحديث بيانات البوت 🔄️", callback_data='admin1'),
                 InlineKeyboardButton('ادارة الادمنز 🔑', callback_data='admin2')],
                [InlineKeyboardButton('سجل العمليات 📉', callback_data='admin3'),
                 InlineKeyboardButton('تسعير 💲', callback_data='admin4')],
                [InlineKeyboardButton('رؤية حسابات العملاء 👤', callback_data='admin5'),
                 InlineKeyboardButton('انشاء كود هدية 🎁', callback_data='admin6')]]
    return InlineKeyboardMarkup(keyboard)


def card():
    keyboard = [[InlineKeyboardButton('موافقة ✅', callback_data='a'), InlineKeyboardButton('رفض ❌', callback_data='r')]]
    return InlineKeyboardMarkup(keyboard)


def pricing_menu_keyboard():
    keyboard = [[InlineKeyboardButton('payeer', callback_data='p1')],
                [InlineKeyboardButton('usdt', callback_data='p2')],
                [InlineKeyboardButton('رجوع', callback_data='admin0')]]
    return InlineKeyboardMarkup(keyboard)


def admin_management_menu_keyboard():
    keyboard = [[InlineKeyboardButton('عرض الادمنز', callback_data='admin_show')],
                [InlineKeyboardButton('اضافة ادمن', callback_data='admin_add')],
                [InlineKeyboardButton('رجوع', callback_data='admin0')]]
    return InlineKeyboardMarkup(keyboard)


def admin_members_keyboard(elements):
    keyboard = []
    for i in range(0, elements):
        keyboard.append([InlineKeyboardButton('معلومات الادمن', callback_data="no"),
                         InlineKeyboardButton('ازالة', callback_data="admin_delete" + "." + str(i))])
    keyboard.append([InlineKeyboardButton('رجوع', callback_data="admin2")])
    return InlineKeyboardMarkup(keyboard)


def operations_log_keyboard():
    keyboard = [[InlineKeyboardButton('جميع المستخدمين', callback_data='log_all')],
                [InlineKeyboardButton('مستخدم محدد', callback_data='log_user')],
                [InlineKeyboardButton('رجوع', callback_data='admin0')]]
    return InlineKeyboardMarkup(keyboard)


def ichancy_keyboard():
    keyboard = [[InlineKeyboardButton(' حساب ايتشانسي جديد', callback_data='ichancy1')],
                [InlineKeyboardButton('شحن حساب ايتشانسي', callback_data='ichancy2')],
                [InlineKeyboardButton('سحب رصيد من حساب ايتشانسي', callback_data='ichancy3')],
                [InlineKeyboardButton('حساباتي', callback_data='ichancy4')],
                [InlineKeyboardButton('رجوع', callback_data='ichancy_menu')]]
    return InlineKeyboardMarkup(keyboard)


###########################command handlers###############################
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == 6457066958:
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


async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    id = str(update.effective_user.id)
    username = update.effective_user.username
    await update.message.reply_text(
        f" اسم المستخدم : {username} \n  ايدي التلغرام الخاص بك :  {id}")


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
            check = []  # check_syriatel()
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
                                                f"\n معرف الزبون {update.effective_user.id}" + "\n")
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
                                                f"\n معرف الزبون {update.effective_user.id}" + "\n")
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
                                                f"\n معرف الزبون {update.effective_user.id}" + "\n")
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
                                                f"\n معرف الزبون {update.effective_user.id}" + "\n")
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
                                                f"\n معرف الزبون {update.effective_user.id}" + "\n")
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
                                                f"\n معرف الزبون {update.effective_user.id}" + "\n")
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
                                                f"\n معرف الزبون {update.effective_user.id}" + "\n")
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
                                                f"\n معرف الزبون {update.effective_user.id}" + "\n")
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
                                                f"\n معرف الزبون {update.effective_user.id}" + "\n")
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
                                                f"\n معرف الزبون {update.effective_user.id}" + "\n")
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
    elif context.user_data["type"] == "create_code":
        context.user_data["index"] += 1
        t1 = update.message.text
        context.user_data["data"].insert(context.user_data["index"], t1)
        if context.user_data["index"] == 0:
            await update.message.reply_text("ادخل القيمة المالية الموافقة")
            return
        # save the code
        await update.message.reply_text("تمت اضافة الكود بنجاح ✅")
        context.user_data["type"] = "null"
        # reset
    elif context.user_data["type"] == "admin_add":
        context.user_data["index"] += 1
        t1 = update.message.text
        context.user_data["data"].insert(context.user_data["index"], t1)
        if context.user_data["index"] == 0:
            await update.message.reply_text("ادخل اسم المستخدم")
            return
        # save the code
        await update.message.reply_text("تمت اضافة الادمن بنجاح ✅")
        context.user_data["type"] = "null"
        # reset
    elif context.user_data["type"] == "log_user":
        context.user_data["index"] += 1
        t1 = update.message.text
        context.user_data["data"].insert(context.user_data["index"], t1)
        if context.user_data["index"] == 0:
            await update.message.reply_text(
                "1️⃣ ادخل تاريخ البداية للسجلات المراد الحصول عليها بالصيغة : \n يوم شهر سنة (2023 10 10)")
            return
        # save the code
        await update.message.reply_text("2️⃣ ادخل تاريخ النهاية للسجلات المراد الحصول عليها بالصيغة السابقة")
        # send the result
        context.user_data["type"] = "null"
        # reset
    elif context.user_data["type"] == "log_all":
        context.user_data["index"] += 1
        t1 = update.message.text
        context.user_data["data"].insert(context.user_data["index"], t1)
        if context.user_data["index"] == 1:
            # send the result
            await update.message.reply_text("ملف")
            context.user_data["type"] = "null"
            return
        await update.message.reply_text("2️⃣ ادخل تاريخ النهاية للسجلات المراد الحصول عليها بالصيغة السابقة")
    elif context.user_data["type"] == "create_ichancy_account":
        # get minimum amount
        minimum = 5000
        balance = 10000
        context.user_data["index"] += 1
        t1 = update.message.text
        context.user_data["data"].insert(context.user_data["index"], t1)
        if context.user_data["index"] == 0:
            await update.message.reply_text("ادخل كلمة سر اطول من 8 خانات وتحتوي على رقم ومحرف كبير على الاقل")
            return
        if context.user_data["index"] == 1:
            pattern = r"^(?=.*\d)(?![\n])(?=.*[A-Z])(?=.*[a-z ]).*.{8,}$"
            if not re.match(pattern,t1):
                context.user_data["index"] -= 1
                await update.message.reply_text("كلمة السر غير مطابقة للشروط الرجاء اعادة الادخال")
                return
            await update.message.reply_text(f"ادخل المبلغ المراد شحنه بالليرة السورية \n ان اقل قيمة شحن هي {minimum}")
        if context.user_data["index"] == 2:
            if int(t1) < minimum:
                await update.message.reply_text("القيمة المدخلة اقل من قيمة الشحن الرجاء اعادة الادخال")
                context.user_data["index"] -= 1
                return
            if int(t1) > balance:
                await update.message.reply_text("ان رصيدك في البوت اقل من القيمة المدخلة الرجاء شحن الرصيد ثم اعادة المحاولة")
                context.user_data["index"] -= 1
                context.user_data["type"] = "null"
                return
            #api to add player
            #api to deposit
            #return the result as a message
            #if every thing is right
            #edit the balance to -amount
            await update.message.reply_text("تمت الاضافة")
            return
    elif context.user_data["type"] == "deposit_to_ichancy":
        context.user_data["index"] += 1
        t1 = update.message.text
        context.user_data["data"].insert(context.user_data["index"], t1)
        if context.user_data["index"] == 0:
            # check if this user id has this user name of ichancy
            #if no tell the user and reset and return
            #else
            await update.message.reply_text(f"ادخل المبلغ المراد شحنه بالليرة السورية \n ان اقل قيمة شحن هي {minimum}")
        if context.user_data["index"] == 1:
            if int(t1) < minimum:
                await update.message.reply_text("القيمة المدخلة اقل من قيمة الشحن الرجاء اعادة الادخال")
                context.user_data["index"] -= 1
                return
            if int(t1) > balance:
                await update.message.reply_text("ان رصيدك في البوت اقل من القيمة المدخلة الرجاء شحن الرصيد ثم اعادة المحاولة")
                context.user_data["index"] -= 1
                context.user_data["type"] = "null"
                return
        #api to get user id
        #api to deposit to player
        #edit the balance to -amount
        #tell the user
        context.user_data["type"] = "null"
        await update.message.reply_text("تم الشحن")
    elif context.user_data["type"] == "withdraw_from_ichancy":
        context.user_data["index"] += 1
        t1 = update.message.text
        context.user_data["data"].insert(context.user_data["index"], t1)
        if context.user_data["index"] == 0:
            # check if this user id has this user name of ichancy
            #if no tell the user and reset and return
            #else
            await update.message.reply_text("ادخل المبلغ المراد سحبه بالليرة السورية")
        if context.user_data["index"] == 1:
            # api to get user id
            #get the user balance api
            #if the balance less than the amount tell the user and return + reset
            #else
            # api to withdraw from player
            # edit the balance to +amount
            #tell the user
            context.user_data["type"] = "null"
            await update.message.reply_text("تم الشحن")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('balance', balance))
    app.add_handler(CommandHandler('info', info))
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
    # app.add_handler(CallbackQueryHandler(accept, pattern='a'))
    app.add_handler(CallbackQueryHandler(refuse, pattern='r'))
    app.add_handler(CallbackQueryHandler(Admin_main_menu, pattern='admin0'))
    app.add_handler(CallbackQueryHandler(pricing_menu, pattern='admin4'))
    app.add_handler(CallbackQueryHandler(pricing_payeer, pattern='p1'))
    app.add_handler(CallbackQueryHandler(pricing_usdt, pattern='p2'))
    app.add_handler(CallbackQueryHandler(from_dollar_to_pound, pattern='from_dollar'))
    app.add_handler(CallbackQueryHandler(from_pound_to_dollar, pattern='from_pound'))
    app.add_handler(CallbackQueryHandler(create_code, pattern='admin6'))
    app.add_handler(CallbackQueryHandler(admin_management, pattern='admin2'))
    app.add_handler(CallbackQueryHandler(admin_show, pattern='admin_show'))
    app.add_handler(CallbackQueryHandler(admin_add, pattern='admin_add'))
    app.add_handler(CallbackQueryHandler(admin_delete, pattern='admin_delete'))
    app.add_handler(CallbackQueryHandler(users_info, pattern='admin5'))
    app.add_handler(CallbackQueryHandler(log_all, pattern='log_all'))
    app.add_handler(CallbackQueryHandler(log_user, pattern='log_user'))
    app.add_handler(CallbackQueryHandler(operations_log, pattern='admin3'))
    app.add_handler(CallbackQueryHandler(ichancy_menu, pattern='ichancy_menu'))
    app.add_handler(CallbackQueryHandler(create_ichancy_account, pattern='ichancy1'))
    app.add_handler(CallbackQueryHandler(deposit_to_ichancy, pattern='ichancy2'))
    app.add_handler(CallbackQueryHandler(withdraw_from_ichancy, pattern='ichancy3'))
    app.add_handler(CallbackQueryHandler(user_ichancy_accounts, pattern='ichancy4'))
    app.add_handler(MessageHandler(filters.TEXT, test_massege))

    app.run_polling(poll_interval=5)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
